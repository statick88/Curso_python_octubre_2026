"""Tests for the seven tetromino definitions and their rotations."""

from __future__ import annotations

import pytest

from src.core import tetrominos

ALL_KINDS = ("I", "J", "L", "O", "S", "T", "Z")


def test_all_seven_kinds_are_defined() -> None:
    """Las siete piezas clásicas están presentes en el catálogo."""
    assert tuple(tetrominos.TETROMINO_KINDS) == ALL_KINDS
    assert set(tetrominos.SHAPES) == set(ALL_KINDS)


@pytest.mark.parametrize("kind", ALL_KINDS)
def test_every_rotation_has_four_cells(kind: str) -> None:
    """Cada orientación conserva cuatro celdas únicas."""
    rotations = tetrominos.SHAPES[kind]
    assert len(rotations) == 4
    for cells in rotations:
        assert len(cells) == 4
        assert len(set(cells)) == 4


@pytest.mark.parametrize("kind", ALL_KINDS)
def test_cells_use_non_negative_integer_coordinates(kind: str) -> None:
    """Las formas usan coordenadas enteras relativas no negativas."""
    for cells in tetrominos.SHAPES[kind]:
        for row, column in cells:
            assert isinstance(row, int)
            assert isinstance(column, int)
            assert row >= 0
            assert column >= 0


@pytest.mark.parametrize("kind", ALL_KINDS)
def test_each_rotation_state_is_reached_by_one_turn(kind: str) -> None:
    """Cada estado precomputado coincide con un giro de su predecesor."""
    rotations = tetrominos.SHAPES[kind]
    size = tetrominos.BOX_SIZE[kind]
    for index, cells in enumerate(rotations):
        assert tetrominos.rotate_cells(cells, size) == rotations[(index + 1) % 4]


def test_i_piece_turns_vertical() -> None:
    """La pieza I alterna entre cuatro columnas y cuatro filas."""
    start = tetrominos.SHAPES["I"][0]
    assert len({row for row, _ in start}) == 1
    assert len({column for _, column in start}) == 4

    rotated = tetrominos.SHAPES["I"][1]
    assert len({row for row, _ in rotated}) == 4
    assert len({column for _, column in rotated}) == 1


def test_o_piece_keeps_the_same_cells_in_every_rotation() -> None:
    """La pieza O conserva sus mismas celdas al girar."""
    rotations = tetrominos.SHAPES["O"]
    assert len({tuple(sorted(cells)) for cells in rotations}) == 1


@pytest.mark.parametrize("kind", ALL_KINDS)
def test_piece_dimensions_stay_within_its_box(kind: str) -> None:
    """Cada rotación permanece contenida en su caja de referencia."""
    size = tetrominos.BOX_SIZE[kind]
    for cells in tetrominos.SHAPES[kind]:
        width = max(column for _, column in cells) + 1
        height = max(row for row, _ in cells) + 1
        assert 1 <= width <= size
        assert 1 <= height <= size


def test_spawn_origin_centers_the_piece() -> None:
    """El origen de aparición centra una pieza T en diez columnas."""
    row, column = tetrominos.spawn_origin("T", columns=10)
    assert row == 0
    assert column == 3


def test_spawn_origin_keeps_wide_pieces_inside_the_board() -> None:
    """El origen de una pieza I ancha no cruza el tablero."""
    _, column = tetrominos.spawn_origin("I", columns=10)
    assert column >= 0
    assert column + tetrominos.piece_width("I") <= 10


def test_piece_width_reads_the_first_rotation() -> None:
    """El ancho de aparición procede de la primera rotación."""
    assert tetrominos.piece_width("I") == 4
    assert tetrominos.piece_width("O") == 2
    assert tetrominos.piece_width("T") == 3


def test_rotation_helper_returns_new_cells_without_mutating() -> None:
    """El ayudante de giro produce otra forma sin mutar la base."""
    cells = tetrominos.SHAPES["T"][0]
    original = tuple(cells)
    rotated = tetrominos.rotate_cells(cells, size=3)
    assert tuple(cells) == original
    assert rotated != original
