"""Tests for the moving piece instance."""

from __future__ import annotations

import pytest

from src.core import tetrominos
from src.core.piece import Piece


def test_new_piece_starts_at_rotation_zero() -> None:
    """Una pieza nueva comienza en su rotación base."""
    piece = Piece(kind="T", row=0, column=4)
    assert piece.rotation == 0
    assert piece.shape() == tetrominos.SHAPES["T"][0]


def test_cells_are_translated_to_board_coordinates() -> None:
    """Las celdas relativas se trasladan a coordenadas del tablero."""
    piece = Piece(kind="O", row=3, column=5)
    assert piece.cells() == ((3, 5), (3, 6), (4, 5), (4, 6))


def test_spawn_places_the_piece_at_the_top_centered() -> None:
    """La aparición centra una pieza ancha en la fila superior."""
    piece = Piece.spawn("I", columns=10)
    assert piece.row == 0
    assert piece.column == 3
    assert piece.rotation == 0
    assert piece.kind == "I"


def test_moved_returns_a_new_piece() -> None:
    """Mover crea una instancia nueva y preserva la original."""
    piece = Piece(kind="L", row=0, column=3)
    moved = piece.moved(d_row=1, d_column=-1)
    assert moved.row == 1
    assert moved.column == 2
    assert piece.row == 0
    assert piece.column == 3


def test_rotated_advances_the_rotation_index() -> None:
    """Rotar avanza el índice sin mutar la pieza de origen."""
    piece = Piece(kind="S", row=0, column=3)
    rotated = piece.rotated()
    assert rotated.rotation == 1
    assert piece.rotation == 0


def test_rotation_wraps_around_after_four_turns() -> None:
    """Cuatro giros devuelven la pieza a su rotación inicial."""
    piece = Piece(kind="Z", row=0, column=3)
    for _ in range(4):
        piece = piece.rotated()
    assert piece.rotation == 0


def test_counter_rotation_moves_backwards() -> None:
    """La rotación antihoraria retrocede el índice de orientación."""
    piece = Piece(kind="J", row=0, column=3)
    assert piece.rotated(clockwise=False).rotation == 3


def test_rotation_changes_the_occupied_cells_of_an_i_piece() -> None:
    """La pieza I alterna entre orientación horizontal y vertical."""
    piece = Piece(kind="I", row=0, column=3)
    horizontal = piece.cells()
    vertical = piece.rotated().cells()
    assert len({row for row, _ in horizontal}) == 1
    assert len({row for row, _ in vertical}) == 4


def test_piece_is_immutable() -> None:
    """La pieza inmutable rechaza asignaciones directas a sus campos."""
    piece = Piece(kind="T", row=0, column=4)
    with pytest.raises(AttributeError):
        piece.row = 5  # type: ignore[misc]


def test_unknown_kind_is_rejected() -> None:
    """Consultar una pieza desconocida informa el error correspondiente."""
    with pytest.raises(KeyError):
        Piece(kind="X", row=0, column=0).cells()


def test_moving_keeps_kind_and_rotation() -> None:
    """El desplazamiento no cambia tipo ni orientación de la pieza."""
    piece = Piece.spawn("S", columns=10).rotated()
    moved = piece.moved(d_row=2, d_column=1)
    assert moved.kind == "S"
    assert moved.rotation == piece.rotation
