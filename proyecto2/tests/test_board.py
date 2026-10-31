"""Tests for the playfield: collisions, locking and line clearing."""

from __future__ import annotations

from pathlib import Path

from src.core.board import Board
from src.core.piece import Piece


def test_new_board_is_empty_and_matches_the_spec_size() -> None:
    """El tablero nuevo tiene 10x20 celdas vacías."""
    board = Board()
    assert board.columns == 10
    assert board.rows == 20
    assert all(board.cell(row, column) is None for row in range(20) for column in range(10))


def test_rows_are_stored_independently() -> None:
    """Escribir una fila no altera las demás filas ni columnas."""
    board = Board()
    board.set_cell(0, 0, "T")
    assert board.cell(0, 0) == "T"
    assert board.cell(1, 0) is None
    assert board.cell(0, 1) is None


def test_piece_inside_an_empty_board_is_placeable() -> None:
    """Una pieza recién generada cabe en un tablero vacío."""
    board = Board()
    assert board.can_place(Piece.spawn("T", columns=10))


def test_piece_crossing_the_left_border_is_rejected() -> None:
    """Una pieza fuera del borde izquierdo no es válida."""
    board = Board()
    piece = Piece(kind="O", row=0, column=-1)
    assert board.can_place(piece) is False


def test_piece_crossing_the_right_border_is_rejected() -> None:
    """Una pieza fuera del borde derecho no es válida."""
    board = Board()
    piece = Piece(kind="I", row=0, column=7)
    assert board.can_place(piece) is False


def test_piece_past_the_floor_is_rejected() -> None:
    """Una pieza que cruza el suelo no es válida."""
    board = Board()
    piece = Piece(kind="O", row=19, column=0)
    assert board.can_place(piece) is False


def test_piece_resting_on_the_floor_is_placeable() -> None:
    """Una pieza apoyada justo sobre el suelo conserva una posición válida."""
    board = Board()
    piece = Piece(kind="O", row=18, column=0)
    assert board.can_place(piece) is True


def test_locked_cells_block_the_piece() -> None:
    """Las celdas fijadas impiden superponer una pieza activa."""
    board = Board()
    board.set_cell(1, 4, "I")
    assert board.can_place(Piece(kind="O", row=0, column=4)) is False


def test_lock_writes_the_piece_kind_and_reports_no_cleared_rows() -> None:
    """Fijar una pieza escribe su tipo sin informar líneas inexistentes."""
    board = Board()
    cleared = board.lock(Piece(kind="O", row=18, column=0))
    assert cleared == ()
    assert board.cell(18, 0) == "O"
    assert board.cell(19, 1) == "O"
    assert board.cell(18, 2) is None


def test_completed_row_disappears_and_the_rows_above_fall() -> None:
    """Una fila completa desaparece y el contenido superior desciende."""
    board = Board()
    for column in range(8):
        board.set_cell(19, column, "J")
    board.set_cell(18, 0, "L")

    cleared = board.lock(Piece(kind="O", row=18, column=8))

    assert cleared == (19,)
    assert board.cell(19, 0) == "L"
    assert board.cell(19, 8) == "O"
    assert board.cell(19, 9) == "O"
    assert board.cell(18, 0) is None


def test_several_completed_rows_clear_together() -> None:
    """Varias filas completas se eliminan en una única operación."""
    board = Board()
    for row in (18, 19):
        for column in range(10):
            board.set_cell(row, column, "S")

    cleared = board.clear_full_rows()

    assert cleared == (18, 19)
    assert all(board.cell(row, column) is None for row in range(20) for column in range(10))


def test_clear_full_rows_ignores_incomplete_rows() -> None:
    """Una fila incompleta permanece intacta tras la limpieza."""
    board = Board()
    for column in range(9):
        board.set_cell(19, column, "Z")
    assert board.clear_full_rows() == ()
    assert board.cell(19, 0) == "Z"


def test_drop_distance_counts_the_free_rows_below() -> None:
    """La distancia de caída cuenta todas las filas libres disponibles."""
    board = Board()
    piece = Piece(kind="O", row=0, column=0)
    assert board.drop_distance(piece) == 18


def test_drop_distance_stops_on_top_of_the_stack() -> None:
    """La distancia de caída termina sobre la pila de piezas fijadas."""
    board = Board()
    for column in range(10):
        board.set_cell(15, column, "T")
    piece = Piece(kind="O", row=0, column=0)
    assert board.drop_distance(piece) == 13


def test_drop_distance_is_zero_when_already_resting() -> None:
    """Una pieza ya apoyada no puede descender más."""
    board = Board()
    piece = Piece(kind="O", row=18, column=0)
    assert board.drop_distance(piece) == 0


def test_reset_empties_the_board() -> None:
    """Restablecer el tablero elimina celdas previamente ocupadas."""
    board = Board()
    board.set_cell(5, 5, "I")
    board.reset()
    assert board.cell(5, 5) is None


def test_core_package_has_no_ui_imports() -> None:
    """El núcleo conserva su independencia respecto de la interfaz."""
    core_dir = Path(__file__).resolve().parent.parent / "src" / "core"
    for source in core_dir.glob("*.py"):
        text = source.read_text(encoding="utf-8")
        assert "tkinter" not in text
        assert "customtkinter" not in text
        assert "from src.ui" not in text
