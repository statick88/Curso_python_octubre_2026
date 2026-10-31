"""The game controller: rules, scoring, levels, lives and states.

The controller owns the board and the falling piece and exposes small actions
that return whether they changed something. It never imports a UI toolkit; the
renderer reads state and the sound layer drains the emitted events.
"""

from __future__ import annotations

import random
from enum import Enum, auto
from typing import Protocol

from src.core.board import Board
from src.core.piece import Piece
from src.core.tetrominos import TETROMINO_KINDS
from src.utils.constants import (
    HARD_DROP_POINTS_PER_CELL,
    LEVEL_SPEEDS_MS,
    LINE_SCORES,
    LINES_PER_LEVEL,
    SOFT_DROP_POINTS_PER_CELL,
    STARTING_LEVEL,
    STARTING_LIVES,
    TOTAL_LEVELS,
)


class GameState(Enum):
    """Lifecycle state of one match."""

    PLAYING = auto()
    PAUSED = auto()
    GAME_OVER = auto()


class GameEvent(Enum):
    """Rule-level facts the sound layer reacts to."""

    MOVE = auto()
    ROTATE = auto()
    SOFT_DROP = auto()
    HARD_DROP = auto()
    LOCK = auto()
    LINE_CLEAR = auto()
    LEVEL_UP = auto()
    LIFE_LOST = auto()
    GAME_OVER = auto()


class KindSource(Protocol):
    """A deterministic or randomized supplier of tetromino kinds."""

    def next_kind(self) -> str:
        """Return the kind of the piece to deal next."""


class SevenBag:
    """Deal each of the seven kinds once per shuffled batch."""

    def __init__(self, rng: random.Random | None = None) -> None:
        """Prepara una bolsa vacía con una fuente aleatoria opcional."""
        self._rng = rng if rng is not None else random.Random()
        self._pending: list[str] = []

    def next_kind(self) -> str:
        """Extrae el siguiente tipo, renovando la bolsa cuando se agota."""
        if not self._pending:
            batch = list(TETROMINO_KINDS)
            self._rng.shuffle(batch)
            self._pending.extend(batch)
        return self._pending.pop()


class _RepeatingSequence:
    """Deterministic source that cycles a fixed tuple of kinds in order."""

    def __init__(self, kinds: tuple[str, ...]) -> None:
        """Guarda la secuencia que se repetirá en las pruebas deterministas."""
        self._kinds = kinds
        self._index = 0

    def next_kind(self) -> str:
        """Entrega el siguiente tipo y vuelve al inicio al llegar al final."""
        kind = self._kinds[self._index % len(self._kinds)]
        self._index += 1
        return kind


class Game:
    """One match: board, current piece, score, level, lives and state."""

    def __init__(
        self,
        rng: random.Random | None = None,
        kind_sequence: tuple[str, ...] | None = None,
    ) -> None:
        """Inicializa una partida con aleatoriedad o secuencia de piezas opcional."""
        if kind_sequence is not None:
            if not kind_sequence:
                raise ValueError("kind_sequence needs at least one tetromino kind")
            unknown = [kind for kind in kind_sequence if kind not in TETROMINO_KINDS]
            if unknown:
                raise ValueError(f"unknown tetromino kinds: {unknown!r}")
        self._rng = rng
        self._kind_sequence = kind_sequence
        self._board = Board()
        self._source: KindSource = SevenBag(rng)
        self._current: Piece | None = None
        self._next_kind = TETROMINO_KINDS[0]
        self._score = 0
        self._lines = 0
        self._level = STARTING_LEVEL
        self._lives = STARTING_LIVES
        self._state = GameState.PLAYING
        self._events: list[GameEvent] = []
        self.start()

    @property
    def board(self) -> Board:
        """Expone el tablero que contiene únicamente piezas fijadas."""
        return self._board

    @property
    def current(self) -> Piece | None:
        """Expone la pieza en caída o ``None`` tras el final de partida."""
        return self._current

    @property
    def next_kind(self) -> str:
        """Expone el tipo reservado para la siguiente pieza."""
        return self._next_kind

    @property
    def state(self) -> GameState:
        """Expone el estado actual del ciclo de vida de la partida."""
        return self._state

    @property
    def score(self) -> int:
        """Expone la puntuación acumulada en la partida."""
        return self._score

    @property
    def lines(self) -> int:
        """Expone la cantidad total de líneas eliminadas."""
        return self._lines

    @property
    def level(self) -> int:
        """Expone el nivel activo, limitado al máximo configurado."""
        return self._level

    @property
    def lives(self) -> int:
        """Expone las vidas restantes de la partida."""
        return self._lives

    @property
    def drop_interval_ms(self) -> int:
        """Devuelve la demora de gravedad correspondiente al nivel activo."""
        return LEVEL_SPEEDS_MS[self._level]

    def start(self) -> None:
        """Reset the whole match and deal the first two pieces."""
        self._board.reset()
        self._score = 0
        self._lines = 0
        self._level = STARTING_LEVEL
        self._lives = STARTING_LIVES
        self._state = GameState.PLAYING
        self._events.clear()
        self._source = (
            SevenBag(self._rng)
            if self._kind_sequence is None
            else _RepeatingSequence(self._kind_sequence)
        )
        self._next_kind = self._source.next_kind()
        self._spawn_next()

    def restart(self) -> bool:
        """Start a new match, but only after the previous one ended."""
        if self._state is not GameState.GAME_OVER:
            return False
        self.start()
        return True

    def drain_events(self) -> tuple[GameEvent, ...]:
        """Return and clear the events produced since the last drain."""
        events = tuple(self._events)
        self._events.clear()
        return events

    def tick(self) -> bool:
        """Advance one gravity step, locking the piece when it cannot fall."""
        if not self._can_act():
            return False
        candidate = self._current.moved(d_row=1)
        if self._board.can_place(candidate):
            self._current = candidate
            return True
        self._lock_current()
        return False

    def move_left(self) -> bool:
        """Intenta desplazar la pieza una columna a la izquierda."""
        return self._move(d_column=-1)

    def move_right(self) -> bool:
        """Intenta desplazar la pieza una columna a la derecha."""
        return self._move(d_column=1)

    def rotate(self, clockwise: bool = True) -> bool:
        """Turn the piece, rejecting the turn when the target cells are taken."""
        if not self._can_act():
            return False
        candidate = self._current.rotated(clockwise=clockwise)
        if not self._board.can_place(candidate):
            return False
        self._current = candidate
        self._events.append(GameEvent.ROTATE)
        return True

    def soft_drop(self) -> bool:
        """Move down one row and score a point; the floor rejects the move."""
        if not self._can_act():
            return False
        candidate = self._current.moved(d_row=1)
        if not self._board.can_place(candidate):
            return False
        self._current = candidate
        self._score += SOFT_DROP_POINTS_PER_CELL
        self._events.append(GameEvent.SOFT_DROP)
        return True

    def hard_drop(self) -> int:
        """Drop to the floor, score it and lock; returns the rows travelled."""
        if not self._can_act():
            return 0
        distance = self._board.drop_distance(self._current)
        if distance:
            self._current = self._current.moved(d_row=distance)
            self._score += distance * HARD_DROP_POINTS_PER_CELL
        self._events.append(GameEvent.HARD_DROP)
        self._lock_current()
        return distance

    def toggle_pause(self) -> bool:
        """Pause a running match or resume a paused one."""
        if self._state is GameState.PLAYING:
            self._state = GameState.PAUSED
            return True
        if self._state is GameState.PAUSED:
            self._state = GameState.PLAYING
            return True
        return False

    def _can_act(self) -> bool:
        """Indica si existe una pieza activa que puede recibir acciones."""
        return self._state is GameState.PLAYING and self._current is not None

    def _move(self, d_column: int) -> bool:
        """Desplaza horizontalmente la pieza si el tablero acepta el destino."""
        if not self._can_act():
            return False
        candidate = self._current.moved(d_column=d_column)
        if not self._board.can_place(candidate):
            return False
        self._current = candidate
        self._events.append(GameEvent.MOVE)
        return True

    def _lock_current(self) -> None:
        """Fija la pieza, calcula recompensas y genera la siguiente pieza."""
        piece = self._current
        if piece is None:
            return
        cleared = self._board.lock(piece)
        self._events.append(GameEvent.LOCK)
        if cleared:
            self._score += LINE_SCORES[len(cleared)] * self._level
            self._lines += len(cleared)
            next_level = min(
                STARTING_LEVEL + self._lines // LINES_PER_LEVEL,
                TOTAL_LEVELS,
            )
            self._events.append(GameEvent.LINE_CLEAR)
            if next_level != self._level:
                self._level = next_level
                self._events.append(GameEvent.LEVEL_UP)
        self._spawn_next()

    def _spawn_next(self) -> None:
        """Convierte la pieza reservada en actual y comprueba la zona de aparición."""
        kind = self._next_kind
        self._next_kind = self._source.next_kind()
        self._current = Piece.spawn(kind, self._board.columns)
        if not self._board.can_place(self._current):
            self._lose_life()

    def _lose_life(self) -> None:
        """Consume una vida, limpia el tablero y termina al llegar a cero."""
        self._board.reset()
        self._lives -= 1
        self._events.append(GameEvent.LIFE_LOST)
        if self._lives <= 0:
            self._lives = 0
            self._current = None
            self._state = GameState.GAME_OVER
            self._events.append(GameEvent.GAME_OVER)
            return
        if self._current is not None:
            self._current = Piece.spawn(self._current.kind, self._board.columns)
