"""Centralized gameplay and visual constants.

Every value that shapes a game rule or a visual token lives here so the core
logic and the UI share a single source of truth.
"""

from __future__ import annotations

from typing import Final

BOARD_COLUMNS: Final[int] = 10
BOARD_ROWS: Final[int] = 20

CELL_SIZE: Final[int] = 30
CANVAS_WIDTH: Final[int] = BOARD_COLUMNS * CELL_SIZE
CANVAS_HEIGHT: Final[int] = BOARD_ROWS * CELL_SIZE

TOTAL_LEVELS: Final[int] = 3
STARTING_LEVEL: Final[int] = 1
LINES_PER_LEVEL: Final[int] = 10

STARTING_LIVES: Final[int] = 3

LEVEL_SPEEDS_MS: Final[dict[int, int]] = {1: 600, 2: 420, 3: 260}

LINE_SCORES: Final[dict[int, int]] = {1: 100, 2: 300, 3: 500, 4: 800}
SOFT_DROP_POINTS_PER_CELL: Final[int] = 1
HARD_DROP_POINTS_PER_CELL: Final[int] = 2

COLOR_BACKGROUND: Final[str] = "#000814"
COLOR_GRID: Final[str] = "#001D3D"
COLOR_GLOW: Final[str] = "#00E0FF"
COLOR_GLOW_BRIGHT: Final[str] = "#00FFFF"
COLOR_TEXT: Final[str] = "#E6FFFF"
COLOR_ALERT: Final[str] = "#FF3366"

PIECE_COLORS: Final[dict[str, str]] = {
    "I": "#00FFFF",
    "J": "#0099FF",
    "L": "#33FFFF",
    "O": "#00BFFF",
    "S": "#00E0FF",
    "T": "#66FFFF",
    "Z": "#0077CC",
}

LINE_CLEAR_FLASH_MS: Final[int] = 140
LEVEL_UP_FLASH_MS: Final[int] = 260
