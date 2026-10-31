"""Tests for the game controller: bag, scoring, levels, lives and states."""

from __future__ import annotations

import random

import pytest

from src.core.board import Board
from src.core.game import Game, GameEvent, GameState, SevenBag
from src.core.tetrominos import TETROMINO_KINDS
from src.utils.constants import (
    BOARD_COLUMNS,
    BOARD_ROWS,
    HARD_DROP_POINTS_PER_CELL,
    LEVEL_SPEEDS_MS,
    LINE_SCORES,
    LINES_PER_LEVEL,
    SOFT_DROP_POINTS_PER_CELL,
    STARTING_LIVES,
    STARTING_LEVEL,
    TOTAL_LEVELS,
)


def _fill_row(board: Board, row: int, columns: int = BOARD_COLUMNS, kind: str = "J") -> None:
    """Completa una fila para preparar escenarios de puntuación."""
    for column in range(columns):
        board.set_cell(row, column, kind)


def _clear_one_line_with_an_i(game: Game) -> int:
    """Prepara y elimina una línea con una pieza I de forma determinista."""
    _fill_row(game.board, BOARD_ROWS - 1, BOARD_COLUMNS - 4)
    for _ in range(BOARD_COLUMNS - 7):
        assert game.move_right() is True
    return game.hard_drop()


def _drop_o_into_the_last_row_gap(game: Game) -> int:
    """Completa el hueco final con una pieza O para eliminar una línea."""
    occupied = {column for _, column in game.current.cells()}
    for column in range(BOARD_COLUMNS):
        if column not in occupied:
            game.board.set_cell(BOARD_ROWS - 1, column, "J")
    return game.hard_drop()


def _sacrifice_a_life(game: Game) -> None:
    """Fuerza una colisión de aparición para comprobar la pérdida de vida."""
    for _ in range(4):
        assert game.soft_drop() is True
    for row in range(4):
        for column in range(BOARD_COLUMNS - 1):
            game.board.set_cell(row, column, "I")
    assert game.hard_drop() > 0


def test_new_game_starts_with_the_documented_state() -> None:
    """Una partida nueva inicia con las métricas y piezas documentadas."""
    game = Game(kind_sequence=("T", "I"))

    assert game.state is GameState.PLAYING
    assert game.score == 0
    assert game.lines == 0
    assert game.level == STARTING_LEVEL
    assert game.lives == STARTING_LIVES
    assert game.current is not None
    assert game.current.kind == "T"
    assert game.next_kind == "I"
    assert game.drop_interval_ms == LEVEL_SPEEDS_MS[STARTING_LEVEL]


def test_start_clears_a_previous_board() -> None:
    """Iniciar otra partida elimina las piezas fijadas anteriormente."""
    game = Game(kind_sequence=("T",))
    game.board.set_cell(5, 5, "I")

    game.start()

    assert all(
        game.board.cell(row, column) is None
        for row in range(BOARD_ROWS)
        for column in range(BOARD_COLUMNS)
    )


def test_empty_kind_sequence_is_rejected() -> None:
    """Una secuencia determinista sin piezas se rechaza explícitamente."""
    with pytest.raises(ValueError):
        Game(kind_sequence=())


def test_seven_bag_deals_each_kind_once_per_batch() -> None:
    """Cada bolsa contiene exactamente los siete tetrominós."""
    bag = SevenBag(random.Random(20261027))

    batch = [bag.next_kind() for _ in range(7)]

    assert sorted(batch) == sorted(TETROMINO_KINDS)


def test_seven_bag_repeats_kinds_across_batches() -> None:
    """Dos bolsas consecutivas conservan una aparición por tipo."""
    bag = SevenBag(random.Random(20261027))

    draws = [bag.next_kind() for _ in range(14)]

    assert sorted(draws) == sorted(TETROMINO_KINDS * 2)


def test_soft_drop_moves_one_row_and_scores_one_point() -> None:
    """La caída suave avanza una fila y suma el punto definido."""
    game = Game(kind_sequence=("O",))
    start_row = game.current.row

    assert game.soft_drop() is True

    assert game.current.row == start_row + 1
    assert game.score == SOFT_DROP_POINTS_PER_CELL


def test_soft_drop_is_blocked_by_the_floor_without_scoring() -> None:
    """El suelo bloquea una caída suave sin modificar la puntuación."""
    game = Game(kind_sequence=("O",))
    for _ in range(18):
        assert game.soft_drop() is True
    score = game.score

    assert game.soft_drop() is False

    assert game.score == score


def test_hard_drop_scores_two_points_per_row_and_locks() -> None:
    """La caída rápida suma por distancia real y fija la pieza."""
    game = Game(kind_sequence=("O",))
    distance = game.board.drop_distance(game.current)

    dropped = game.hard_drop()

    assert dropped == distance
    assert distance == 18
    assert game.score == distance * HARD_DROP_POINTS_PER_CELL + 0
    assert game.board.cell(19, 4) == "O"


def test_hard_drop_stops_on_top_of_stacked_cells() -> None:
    """La caída rápida se detiene sobre celdas fijadas, sin atravesarlas."""
    game = Game(kind_sequence=("O",))
    for column in range(5):
        game.board.set_cell(15, column, "J")

    distance = game.hard_drop()

    assert distance == 13
    assert game.board.cell(13, 4) == "O"
    assert game.board.cell(14, 4) == "O"
    assert game.board.cell(15, 4) == "J"


def test_move_left_and_right_respect_the_walls() -> None:
    """El movimiento lateral respeta ambos límites del tablero."""
    game = Game(kind_sequence=("T",))

    for _ in range(BOARD_COLUMNS):
        game.move_left()

    assert game.current.column == 0
    assert game.move_left() is False

    for _ in range(BOARD_COLUMNS):
        game.move_right()

    assert game.current.column == BOARD_COLUMNS - 3
    assert game.move_right() is False


def test_rotate_changes_the_orientation_and_can_be_undone() -> None:
    """Una rotación válida cambia la forma y admite su inversa."""
    game = Game(kind_sequence=("T",))
    cells_before = game.current.cells()

    assert game.rotate() is True

    assert game.current.rotation == 1
    assert game.current.cells() != cells_before
    assert game.rotate(clockwise=False) is True
    assert game.current.rotation == 0


def test_rotation_is_rejected_when_the_target_cells_are_locked() -> None:
    """No se acepta rotar hacia una celda ya fijada."""
    game = Game(kind_sequence=("T",))
    new_cells = set(game.current.rotated().cells()) - set(game.current.cells())
    row, column = sorted(new_cells)[0]
    game.board.set_cell(row, column, "I")

    assert game.rotate() is False

    assert game.current.rotation == 0


def test_single_line_scores_one_hundred_times_the_current_level() -> None:
    """Una línea usa el multiplicador del nivel activo."""
    game = Game(kind_sequence=("O",))
    distance = game.board.drop_distance(game.current)

    _drop_o_into_the_last_row_gap(game)

    assert game.lines == 1
    assert game.score == distance * HARD_DROP_POINTS_PER_CELL + LINE_SCORES[1] * STARTING_LEVEL


def test_four_lines_score_eight_hundred_times_the_current_level() -> None:
    """Un Tetris de cuatro líneas usa la tabla de puntuación exacta."""
    game = Game(kind_sequence=("I",))
    for row in range(BOARD_ROWS - 4, BOARD_ROWS):
        _fill_row(game.board, row, BOARD_COLUMNS - 1)
    assert game.rotate() is True
    for _ in range(6):
        assert game.move_right() is True
    distance = game.board.drop_distance(game.current)

    game.hard_drop()

    assert game.lines == 4
    assert game.score == distance * HARD_DROP_POINTS_PER_CELL + LINE_SCORES[4] * STARTING_LEVEL


def test_level_rises_every_ten_lines_and_caps_at_three() -> None:
    """El nivel aumenta cada diez líneas y nunca supera tres."""
    game = Game(kind_sequence=("I",))

    for cleared in range(1, LINES_PER_LEVEL * TOTAL_LEVELS + 1):
        if cleared == LINES_PER_LEVEL:
            level_before = game.level
            score_before = game.score
            distance = game.board.drop_distance(game.current)
            _clear_one_line_with_an_i(game)
            assert game.score - score_before == (
                distance * HARD_DROP_POINTS_PER_CELL + LINE_SCORES[1] * level_before
            )
            assert game.level == STARTING_LEVEL + 1
            assert GameEvent.LEVEL_UP in game.drain_events()
            continue
        _clear_one_line_with_an_i(game)

    assert game.lines == LINES_PER_LEVEL * TOTAL_LEVELS
    assert game.level == TOTAL_LEVELS
    assert game.drop_interval_ms == LEVEL_SPEEDS_MS[TOTAL_LEVELS]


def test_losing_a_life_resets_the_playfield() -> None:
    """Perder una vida limpia el tablero y permite continuar."""
    game = Game(kind_sequence=("O",))

    _sacrifice_a_life(game)

    assert game.lives == STARTING_LIVES - 1
    assert game.state is GameState.PLAYING
    assert game.current is not None
    assert all(
        game.board.cell(row, column) is None
        for row in range(BOARD_ROWS)
        for column in range(BOARD_COLUMNS)
    )


def test_three_life_losses_end_the_game() -> None:
    """La tercera pérdida deja el juego en Game Over definitivo."""
    game = Game(kind_sequence=("O",))
    for _ in range(STARTING_LIVES):
        _sacrifice_a_life(game)

    assert game.lives == 0
    assert game.state is GameState.GAME_OVER
    assert game.current is None
    assert game.tick() is False
    assert game.move_left() is False
    assert game.soft_drop() is False
    assert game.hard_drop() == 0
    assert game.rotate() is False
    assert game.toggle_pause() is False


def test_pause_freezes_gravity_and_rejects_actions() -> None:
    """La pausa bloquea gravedad y entradas hasta reanudar."""
    game = Game(kind_sequence=("O",))
    row = game.current.row

    assert game.toggle_pause() is True
    assert game.state is GameState.PAUSED
    assert game.tick() is False
    assert game.current.row == row
    assert game.move_left() is False
    assert game.hard_drop() == 0

    assert game.toggle_pause() is True
    assert game.state is GameState.PLAYING
    assert game.tick() is True
    assert game.current.row == row + 1


def test_restart_is_only_allowed_after_game_over() -> None:
    """El reinicio solo está disponible al finalizar una partida."""
    game = Game(kind_sequence=("O",))
    game.soft_drop()

    assert game.restart() is False
    assert game.score == SOFT_DROP_POINTS_PER_CELL

    for _ in range(STARTING_LIVES):
        _sacrifice_a_life(game)
    assert game.restart() is True

    assert game.state is GameState.PLAYING
    assert game.lives == STARTING_LIVES
    assert game.score == 0
    assert game.lines == 0
    assert game.level == STARTING_LEVEL
    assert game.current is not None


def test_events_report_the_actions_for_sound_effects() -> None:
    """Las acciones exitosas emiten eventos para los efectos de sonido."""
    game = Game(kind_sequence=("O",))
    game.drain_events()

    assert game.move_left() is True
    assert game.drain_events() == (GameEvent.MOVE,)
    assert game.rotate() is True
    assert game.drain_events() == (GameEvent.ROTATE,)

    distance = game.board.drop_distance(game.current)
    assert game.hard_drop() == distance
    assert game.drain_events() == (GameEvent.HARD_DROP, GameEvent.LOCK)


def test_line_clear_emits_its_own_event() -> None:
    """Eliminar una línea emite su evento de feedback independiente."""
    game = Game(kind_sequence=("O",))
    _fill_row(game.board, BOARD_ROWS - 1, BOARD_COLUMNS - 2)
    for _ in range(4):
        game.move_right()
    game.drain_events()

    game.hard_drop()

    assert game.drain_events() == (
        GameEvent.HARD_DROP,
        GameEvent.LOCK,
        GameEvent.LINE_CLEAR,
    )
