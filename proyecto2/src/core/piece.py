"""The moving piece instance.

``Piece`` is an immutable value object: every movement or rotation returns a new
instance so the caller can validate the result before committing to it.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

from src.core import tetrominos


@dataclass(frozen=True, slots=True)
class Piece:
    kind: str
    row: int
    column: int
    rotation: int = 0

    @classmethod
    def spawn(cls, kind: str, columns: int) -> "Piece":
        """Create a piece in its spawn rotation at the top of the board."""
        row, column = tetrominos.spawn_origin(kind, columns)
        return cls(kind=kind, row=row, column=column)

    def shape(self) -> tuple[tetrominos.Cell, ...]:
        """Devuelve las celdas relativas de la rotación actual."""
        return tetrominos.SHAPES[self.kind][self.rotation]

    def cells(self) -> tuple[tetrominos.Cell, ...]:
        """Occupied cells translated to absolute board coordinates."""
        return tuple(
            (self.row + row, self.column + column) for row, column in self.shape()
        )

    def moved(self, d_row: int = 0, d_column: int = 0) -> "Piece":
        """Crea otra pieza desplazada sin mutar la instancia actual."""
        return replace(self, row=self.row + d_row, column=self.column + d_column)

    def rotated(self, clockwise: bool = True) -> "Piece":
        """Crea otra pieza con una rotación en el sentido solicitado."""
        step = 1 if clockwise else -1
        return replace(self, rotation=(self.rotation + step) % 4)
