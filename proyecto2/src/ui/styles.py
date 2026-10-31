"""Visual style tokens and font helpers for the Tetris UI."""

from __future__ import annotations

from src.utils.constants import (
    COLOR_ALERT,
    COLOR_BACKGROUND,
    COLOR_GLOW,
    COLOR_GLOW_BRIGHT,
    COLOR_GRID,
    COLOR_TEXT,
    PIECE_COLORS,
)


def piece_color(kind: str) -> str:
    """Devuelve el color asociado a un tetrominó o el glow de respaldo."""
    return PIECE_COLORS.get(kind, COLOR_GLOW_BRIGHT)


FONT_TITLE = ("Consolas", 24, "bold")
FONT_SUBTITLE = ("Consolas", 14, "bold")
FONT_HUD = ("Consolas", 14)
FONT_SMALL = ("Consolas", 11)
