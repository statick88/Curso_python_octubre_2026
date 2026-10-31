"""Renderizador del Canvas para tablero, piezas, estados y feedback de Tetris."""

from __future__ import annotations

import tkinter as tk
from collections.abc import Iterable

from src.core.board import Board
from src.core.game import Game, GameEvent, GameState
from src.core.piece import Piece
from src.ui.styles import piece_color
from src.utils.constants import (
    BOARD_COLUMNS,
    BOARD_ROWS,
    CELL_SIZE,
    COLOR_ALERT,
    COLOR_BACKGROUND,
    COLOR_GLOW,
    COLOR_GLOW_BRIGHT,
    COLOR_GRID,
    COLOR_TEXT,
)


class Renderer:
    """Dibuja el estado del modelo sin modificar reglas ni datos de partida."""

    def __init__(self, canvas: tk.Canvas) -> None:
        """Conserva el Canvas que recibirá todas las operaciones de dibujo."""
        self.canvas = canvas
        self._line_feedback_frames = 0
        self._level_feedback_frames = 0

    def notify_events(self, events: Iterable[GameEvent]) -> None:
        """Convierte eventos de reglas en feedback visible de duración limitada."""
        for event in events:
            if event is GameEvent.LINE_CLEAR:
                self._line_feedback_frames = 2
            elif event is GameEvent.LEVEL_UP:
                self._level_feedback_frames = 4

    def draw(self, game: Game) -> None:
        """Redibuja el tablero, la pieza, overlays y feedback del estado actual."""
        self.canvas.delete("all")
        self._draw_grid()
        self._draw_locked(game.board)
        if game.current is not None:
            self._draw_piece(game.current)
        self._draw_feedback(game.state)
        self._draw_overlay(game.state)

    def _draw_grid(self) -> None:
        """Traza las líneas que delimitan cada celda del tablero."""
        for row in range(BOARD_ROWS + 1):
            y = row * CELL_SIZE
            self.canvas.create_line(0, y, BOARD_COLUMNS * CELL_SIZE, y, fill=COLOR_GRID)
        for column in range(BOARD_COLUMNS + 1):
            x = column * CELL_SIZE
            self.canvas.create_line(x, 0, x, BOARD_ROWS * CELL_SIZE, fill=COLOR_GRID)

    def _draw_locked(self, board: Board) -> None:
        """Pinta las piezas que ya fueron fijadas en el tablero."""
        for row in range(board.rows):
            for column in range(board.columns):
                kind = board.cell(row, column)
                if kind is not None:
                    self._draw_cell(row, column, piece_color(kind))

    def _draw_piece(self, piece: Piece) -> None:
        """Pinta la pieza que el jugador aún puede mover."""
        for row, column in piece.cells():
            if 0 <= row < BOARD_ROWS and 0 <= column < BOARD_COLUMNS:
                self._draw_cell(row, column, piece_color(piece.kind))

    def _draw_cell(self, row: int, column: int, color: str) -> None:
        """Dibuja una celda coloreada con borde luminoso."""
        x1 = column * CELL_SIZE + 1
        y1 = row * CELL_SIZE + 1
        x2 = (column + 1) * CELL_SIZE - 1
        y2 = (row + 1) * CELL_SIZE - 1
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=COLOR_GLOW)

    def _draw_feedback(self, state: GameState) -> None:
        """Muestra brevemente confirmaciones de líneas y niveles durante el juego."""
        if state is not GameState.PLAYING:
            return
        center_x = BOARD_COLUMNS * CELL_SIZE // 2
        if self._line_feedback_frames:
            self.canvas.create_rectangle(
                0,
                BOARD_ROWS * CELL_SIZE - CELL_SIZE,
                BOARD_COLUMNS * CELL_SIZE,
                BOARD_ROWS * CELL_SIZE,
                outline=COLOR_GLOW_BRIGHT,
                width=3,
            )
            self.canvas.create_text(
                center_x,
                BOARD_ROWS * CELL_SIZE - CELL_SIZE // 2,
                text="LÍNEA COMPLETA",
                fill=COLOR_GLOW_BRIGHT,
                font=("Consolas", 12, "bold"),
            )
            self._line_feedback_frames -= 1
        if self._level_feedback_frames:
            self.canvas.create_text(
                center_x,
                CELL_SIZE,
                text="NIVEL SUPERIOR",
                fill=COLOR_GLOW_BRIGHT,
                font=("Consolas", 16, "bold"),
            )
            self._level_feedback_frames -= 1

    def _draw_overlay(self, state: GameState) -> None:
        """Cubre el tablero con los mensajes de pausa o final de partida."""
        if state is GameState.PAUSED:
            self._overlay_text("PAUSA", COLOR_GLOW_BRIGHT)
        elif state is GameState.GAME_OVER:
            self._overlay_text("GAME OVER", COLOR_ALERT)
            self.canvas.create_text(
                BOARD_COLUMNS * CELL_SIZE // 2,
                BOARD_ROWS * CELL_SIZE // 2 + 30,
                text="R PARA REINICIAR",
                fill=COLOR_TEXT,
                font=("Consolas", 12, "bold"),
            )

    def _overlay_text(self, text: str, color: str) -> None:
        """Dibuja una banda translúcida con un mensaje central destacado."""
        self.canvas.create_rectangle(
            0,
            BOARD_ROWS * CELL_SIZE // 2 - 30,
            BOARD_COLUMNS * CELL_SIZE,
            BOARD_ROWS * CELL_SIZE // 2 + 30,
            fill=COLOR_BACKGROUND,
            stipple="gray50",
        )
        self.canvas.create_text(
            BOARD_COLUMNS * CELL_SIZE // 2,
            BOARD_ROWS * CELL_SIZE // 2,
            text=text,
            fill=color,
            font=("Consolas", 24, "bold"),
        )
