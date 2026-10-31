"""The seven tetrominoes and their four precomputed rotation states.

Cell coordinates are ``(row, column)`` pairs relative to the piece origin and
normalized so that the smallest row and column are always zero.
"""

from __future__ import annotations

from typing import Final

Cell = tuple[int, int]

TETROMINO_KINDS: Final[tuple[str, ...]] = ("I", "J", "L", "O", "S", "T", "Z")

BOX_SIZE: Final[dict[str, int]] = {
    "I": 4,
    "J": 3,
    "L": 3,
    "O": 2,
    "S": 3,
    "T": 3,
    "Z": 3,
}

BASE_CELLS: Final[dict[str, tuple[Cell, ...]]] = {
    "I": ((0, 0), (0, 1), (0, 2), (0, 3)),
    "J": ((0, 0), (1, 0), (1, 1), (1, 2)),
    "L": ((0, 2), (1, 0), (1, 1), (1, 2)),
    "O": ((0, 0), (0, 1), (1, 0), (1, 1)),
    "S": ((0, 1), (0, 2), (1, 0), (1, 1)),
    "T": ((0, 0), (0, 1), (0, 2), (1, 1)),
    "Z": ((0, 0), (0, 1), (1, 1), (1, 2)),
}


def rotate_cells(cells: tuple[Cell, ...], size: int) -> tuple[Cell, ...]:
    """Turn a normalized cell set one quarter turn clockwise.

    Each cell maps to ``(column, size - 1 - row)`` inside its square box and the
    result is re-normalized back to the origin. The input stays untouched.
    """
    rotated = tuple((column, size - 1 - row) for row, column in cells)
    min_row = min(row for row, _ in rotated)
    min_column = min(column for _, column in rotated)
    return tuple((row - min_row, column - min_column) for row, column in rotated)


def _build_rotations(kind: str) -> tuple[tuple[Cell, ...], ...]:
    """Precalcula los cuatro estados de rotación para un tetrominó."""
    size = BOX_SIZE[kind]
    states: list[tuple[Cell, ...]] = [BASE_CELLS[kind]]
    for _ in range(3):
        states.append(rotate_cells(states[-1], size))
    return tuple(states)


SHAPES: Final[dict[str, tuple[tuple[Cell, ...], ...]]] = {
    kind: _build_rotations(kind) for kind in TETROMINO_KINDS
}


def piece_width(kind: str) -> int:
    """Width, in columns, of the piece in its spawn rotation."""
    cells = SHAPES[kind][0]
    return max(column for _, column in cells) + 1


def spawn_origin(kind: str, columns: int) -> Cell:
    """Top row and horizontally centered column for a freshly spawned piece."""
    return 0, max(0, (columns - piece_width(kind)) // 2)
