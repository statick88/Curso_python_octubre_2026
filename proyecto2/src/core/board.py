"""The playfield grid: collisions, locking and line clearing.

The board stores the kind of the piece that locked each cell, or ``None`` for an
empty cell. It knows nothing about rendering; the UI reads ``cell`` and decides
how to paint it.
"""

from __future__ import annotations

from src.core.piece import Piece
from src.utils.constants import BOARD_COLUMNS, BOARD_ROWS

Grid = list[list[str | None]]


class Board:
    """A fixed-size grid of locked cells."""

    def __init__(self, rows: int = BOARD_ROWS, columns: int = BOARD_COLUMNS) -> None:
        """Crea una cuadrícula vacía con dimensiones positivas."""
        if rows <= 0 or columns <= 0:
            raise ValueError("a board needs positive rows and columns")
        self._rows = rows
        self._columns = columns
        self._grid: Grid = self._empty_grid()

    @property
    def rows(self) -> int:
        """Expone la cantidad fija de filas del tablero."""
        return self._rows

    @property
    def columns(self) -> int:
        """Expone la cantidad fija de columnas del tablero."""
        return self._columns

    def _empty_grid(self) -> Grid:
        """Crea una matriz vacía sin compartir filas mutables."""
        return [[None] * self._columns for _ in range(self._rows)]

    def _check_bounds(self, row: int, column: int) -> None:
        """Valida que una coordenada pertenezca al tablero."""
        if not 0 <= row < self._rows:
            raise IndexError(f"row {row} is outside 0..{self._rows - 1}")
        if not 0 <= column < self._columns:
            raise IndexError(f"column {column} is outside 0..{self._columns - 1}")

    def cell(self, row: int, column: int) -> str | None:
        """The locked piece kind at that position, or ``None`` when empty."""
        self._check_bounds(row, column)
        return self._grid[row][column]

    def set_cell(self, row: int, column: int, kind: str | None) -> None:
        """Escribe una celda; se usa para preparación controlada y pruebas."""
        self._check_bounds(row, column)
        self._grid[row][column] = kind

    def can_place(self, piece: Piece) -> bool:
        """True when every cell of ``piece`` is free and inside the board."""
        for row, column in piece.cells():
            if not (0 <= row < self._rows and 0 <= column < self._columns):
                return False
            if self._grid[row][column] is not None:
                return False
        return True

    def drop_distance(self, piece: Piece) -> int:
        """How many rows ``piece`` can still fall before it would collide."""
        distance = 0
        candidate = piece
        while self.can_place(candidate.moved(d_row=1)):
            candidate = candidate.moved(d_row=1)
            distance += 1
        return distance

    def lock(self, piece: Piece) -> tuple[int, ...]:
        """Write ``piece`` into the grid and return the cleared row indices."""
        if not self.can_place(piece):
            raise ValueError("cannot lock a piece outside the board or over a locked cell")
        for row, column in piece.cells():
            self._grid[row][column] = piece.kind
        return self.clear_full_rows()

    def clear_full_rows(self) -> tuple[int, ...]:
        """Remove every completed row and settle the rows above; return their indices."""
        cleared = tuple(
            index for index, row in enumerate(self._grid) if all(cell is not None for cell in row)
        )
        if not cleared:
            return ()
        remaining = [row for row in self._grid if any(cell is None for cell in row)]
        blank = [[None] * self._columns for _ in range(self._rows - len(remaining))]
        self._grid[:] = blank + remaining
        return cleared

    def reset(self) -> None:
        """Empty every cell, keeping the board size."""
        self._grid = self._empty_grid()
