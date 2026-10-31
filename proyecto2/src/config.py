"""Application-level configuration: window, fonts and asset locations."""

from __future__ import annotations

from pathlib import Path
from typing import Final

APP_TITLE: Final[str] = "TETRIS"
WINDOW_PADDING: Final[int] = 24

FONT_FAMILY_CANDIDATES: Final[tuple[str, ...]] = (
    "JetBrains Mono",
    "Consolas",
    "Courier New",
)
FONT_TITLE_SIZE: Final[int] = 26
FONT_LABEL_SIZE: Final[int] = 13
FONT_VALUE_SIZE: Final[int] = 20
FONT_OVERLAY_SIZE: Final[int] = 34

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent.parent
ASSETS_DIR: Final[Path] = PROJECT_ROOT / "assets"
SOUNDS_DIR: Final[Path] = ASSETS_DIR / "sounds"
FONTS_DIR: Final[Path] = ASSETS_DIR / "fonts"

BACKGROUND_MUSIC: Final[Path] = SOUNDS_DIR / "bg_music.ogg"
MOVE_SOUND: Final[Path] = SOUNDS_DIR / "move.wav"
ROTATE_SOUND: Final[Path] = SOUNDS_DIR / "rotate.wav"
LINE_CLEAR_SOUND: Final[Path] = SOUNDS_DIR / "line_clear.wav"
GAME_OVER_SOUND: Final[Path] = SOUNDS_DIR / "game_over.wav"

MUSIC_VOLUME: Final[float] = 0.35
SFX_VOLUME: Final[float] = 0.55
