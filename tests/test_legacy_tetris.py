"""Pruebas de interfaz para la lógica pura del Tetris legado."""

from __future__ import annotations

import ast
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROYECTO = ROOT / "proyecto"
FUENTE = PROYECTO / "src"


def funciones_sin_docstring(ruta: Path) -> list[str]:
    """Devuelve los métodos sin docstring dentro del código legado."""
    arbol = ast.parse(ruta.read_text(encoding="utf-8"), filename=str(ruta))
    faltantes: list[str] = []
    for nodo in ast.walk(arbol):
        if isinstance(nodo, (ast.FunctionDef, ast.AsyncFunctionDef)) and not ast.get_docstring(nodo):
            faltantes.append(f"{ruta.relative_to(ROOT)}:{nodo.name}")
    return faltantes


def ejecutar_logica(codigo: str) -> dict[str, object]:
    """Ejecuta la lógica legado en un proceso sin compartir paquetes src."""
    resultado = subprocess.run(
        [sys.executable, "-c", codigo],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    if resultado.returncode != 0:
        raise AssertionError(resultado.stderr)
    return json.loads(resultado.stdout)


class TestDocumentacionDelTetrisLegado(unittest.TestCase):
    """Comprueba que la API del miniproyecto conserva documentación útil."""

    def test_todas_las_funciones_tienen_docstrings(self) -> None:
        """Exige docstrings en funciones y métodos del Tetris legado."""
        faltantes = [
            faltante
            for ruta in FUENTE.rglob("*.py")
            for faltante in funciones_sin_docstring(ruta)
        ]
        self.assertEqual(faltantes, [])


class TestLogicaPuraDelTetrisLegado(unittest.TestCase):
    """Comprueba tablero y tetrominos sin iniciar la interfaz gráfica."""

    def test_tetromino_rota_y_recupera_su_forma_inicial(self) -> None:
        """Verifica el ciclo público de rotación de la pieza T."""
        datos = ejecutar_logica(
            "import json, sys; sys.path.insert(0, 'proyecto'); "
            "from src.core.tetrominos import Tetromino; pieza = Tetromino('T'); "
            "inicial = pieza.get_shape(); [pieza.rotate() for _ in range(4)]; "
            "print(json.dumps({'inicial': inicial, 'final': pieza.get_shape(), "
            "'ancho': pieza.get_width(), 'alto': pieza.get_height()}))"
        )
        self.assertEqual(datos["inicial"], datos["final"])
        self.assertEqual((datos["ancho"], datos["alto"]), (3, 2))

    def test_tablero_rechaza_colisiones_y_limpia_una_fila(self) -> None:
        """Verifica colisiones de borde, fijación y limpieza de líneas."""
        datos = ejecutar_logica(
            "import json, sys; sys.path.insert(0, 'proyecto'); "
            "from src.core.board import Board; tablero = Board(); forma = [[1]]; "
            "valida = tablero.is_valid_position(forma, (0, 0)); "
            "tablero.add_piece(forma, (0, 0), '#00FFFF'); "
            "ocupada = tablero.is_valid_position(forma, (0, 0)); "
            "borde = tablero.is_valid_position(forma, (-1, 0)); "
            "tablero.grid[-1] = ['#00FFFF'] * tablero.width; "
            "lineas = tablero.clear_lines(); "
            "print(json.dumps({'valida': valida, 'ocupada': ocupada, 'borde': borde, "
            "'lineas': lineas, 'fila_superior_vacia': tablero.grid[0] == [0] * tablero.width}))"
        )
        self.assertTrue(datos["valida"])
        self.assertFalse(datos["ocupada"])
        self.assertFalse(datos["borde"])
        self.assertEqual(datos["lineas"], 1)
        self.assertTrue(datos["fila_superior_vacia"])


if __name__ == "__main__":
    unittest.main()
