"""Tests for the centralized gameplay constants."""

from __future__ import annotations

import pytest

from src.utils import constants


def test_board_geometry_matches_spec() -> None:
    """La geometría centralizada coincide con el tablero documentado."""
    assert constants.BOARD_COLUMNS == 10
    assert constants.BOARD_ROWS == 20
    assert constants.CANVAS_WIDTH == constants.BOARD_COLUMNS * constants.CELL_SIZE
    assert constants.CANVAS_HEIGHT == constants.BOARD_ROWS * constants.CELL_SIZE


def test_level_and_life_rules_match_spec() -> None:
    """Los límites de niveles, vidas y líneas siguen la especificación."""
    assert constants.TOTAL_LEVELS == 3
    assert constants.STARTING_LEVEL == 1
    assert constants.STARTING_LIVES == 3
    assert constants.LINES_PER_LEVEL == 10


def test_speed_increases_with_every_level() -> None:
    """Cada nivel reduce la demora de caída respecto del anterior."""
    delays = [constants.LEVEL_SPEEDS_MS[level] for level in range(1, constants.TOTAL_LEVELS + 1)]
    assert delays == sorted(delays, reverse=True)
    assert len(set(delays)) == constants.TOTAL_LEVELS


def test_speed_table_covers_exactly_the_three_levels() -> None:
    """La tabla de velocidad cubre solo los tres niveles permitidos."""
    assert set(constants.LEVEL_SPEEDS_MS) == {1, 2, 3}


@pytest.mark.parametrize(
    ("lines", "expected"),
    [(1, 100), (2, 300), (3, 500), (4, 800)],
)
def test_line_score_table(lines: int, expected: int) -> None:
    """La tabla conserva la puntuación cerrada por cantidad de líneas."""
    assert constants.LINE_SCORES[lines] == expected


def test_drop_bonus_values_match_spec() -> None:
    """Las bonificaciones de caída suave y rápida son las acordadas."""
    assert constants.SOFT_DROP_POINTS_PER_CELL == 1
    assert constants.HARD_DROP_POINTS_PER_CELL == 2


def test_palette_matches_spec() -> None:
    """Los colores centrales coinciden con la paleta hacker requerida."""
    assert constants.COLOR_BACKGROUND == "#000814"
    assert constants.COLOR_GRID == "#001D3D"
    assert constants.COLOR_GLOW == "#00E0FF"
    assert constants.COLOR_GLOW_BRIGHT == "#00FFFF"
    assert constants.COLOR_TEXT == "#E6FFFF"
    assert constants.COLOR_ALERT == "#FF3366"


def test_every_tetromino_kind_has_a_palette_color() -> None:
    """Cada tetrominó posee un color hexadecimal renderizable."""
    for kind in ("I", "J", "L", "O", "S", "T", "Z"):
        color = constants.PIECE_COLORS[kind]
        assert color.startswith("#")
        assert len(color) == 7
