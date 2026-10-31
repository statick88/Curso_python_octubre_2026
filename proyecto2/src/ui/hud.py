"""HUD panel: score, level, lives, lines and next piece."""

from __future__ import annotations

import tkinter as tk

from src.core.game import Game
from src.core.piece import Piece
from src.core.tetrominos import SHAPES
from src.ui.renderer import Renderer
from src.ui.styles import piece_color


class HUD:
    """Muestra métricas de partida y vista previa sin alterar el modelo."""

    def __init__(self, parent: tk.Widget) -> None:
        """Construye los controles del panel lateral dentro del padre indicado."""
        self.next_frame = tk.Frame(parent, bg="#000814")
        self.next_label = tk.Label(
            self.next_frame,
            text="SIGUIENTE",
            fg="#00E0FF",
            bg="#000814",
            font=("Consolas", 12, "bold"),
        )
        self.next_label.pack()
        self.next_canvas = tk.Canvas(
            self.next_frame,
            width=4 * 24,
            height=4 * 24,
            bg="#000814",
            highlightthickness=0,
        )
        self.next_canvas.pack(pady=4)
        self.frame = tk.Frame(parent, bg="#000814")
        self.score_var = tk.StringVar(value="PUNTOS: 0")
        self.level_var = tk.StringVar(value="NIVEL: 1")
        self.lives_var = tk.StringVar(value="VIDAS: 3")
        self.lines_var = tk.StringVar(value="LÍNEAS: 0")
        for var in (self.score_var, self.level_var, self.lives_var, self.lines_var):
            tk.Label(self.frame, textvariable=var, fg="#E6FFFF", bg="#000814",
                     font=("Consolas", 13)).pack(anchor="w", padx=8, pady=2)

    def update(self, game: Game) -> None:
        """Sincroniza textos y vista previa con el estado actual de la partida."""
        self.score_var.set(f"PUNTOS: {game.score}")
        self.level_var.set(f"NIVEL: {game.level}")
        self.lives_var.set(f"VIDAS: {game.lives}")
        self.lines_var.set(f"LÍNEAS: {game.lines}")
        self._draw_next(game.next_kind)

    def _draw_next(self, kind: str) -> None:
        """Dibuja la pieza reservada en su rotación inicial."""
        self.next_canvas.delete("all")
        for row, column in SHAPES[kind][0]:
            x1 = column * 24 + 1
            y1 = row * 24 + 1
            x2 = (column + 1) * 24 - 1
            y2 = (row + 1) * 24 - 1
            self.next_canvas.create_rectangle(x1, y1, x2, y2, fill=piece_color(kind),
                                             outline="#00E0FF")
