"""Pruebas de interfaz para los ejemplos de las semanas uno a tres."""

from __future__ import annotations

import ast
import os
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEMANA_1 = ROOT / "semana1"
SEMANA_2 = ROOT / "semana2"
SEMANA_3 = ROOT / "semana3"


def funciones_sin_docstring(ruta: Path) -> list[str]:
    """Devuelve las funciones y métodos sin docstring de un ejemplo."""
    arbol = ast.parse(ruta.read_text(encoding="utf-8"), filename=str(ruta))
    faltantes: list[str] = []
    for nodo in ast.walk(arbol):
        if isinstance(nodo, (ast.FunctionDef, ast.AsyncFunctionDef)) and not ast.get_docstring(nodo):
            faltantes.append(f"{ruta.relative_to(ROOT)}:{nodo.name}")
    return faltantes


def ejecutar_ejemplo(ruta: Path, entrada: str | None = None) -> subprocess.CompletedProcess[str]:
    """Ejecuta un ejemplo aislado y conserva su salida para las aserciones."""
    return subprocess.run(
        [sys.executable, str(ruta)],
        cwd=ROOT,
        input=entrada,
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )


class TestDocumentacionDeEjemplos(unittest.TestCase):
    """Comprueba que los ejemplos declaran sus funciones para el alumnado."""

    def test_todas_las_funciones_tienen_docstrings(self) -> None:
        """Exige docstrings en funciones y métodos de las tres semanas."""
        rutas = [*SEMANA_1.glob("*.py"), *SEMANA_2.glob("*.py"), *SEMANA_3.rglob("*.py")]
        faltantes = [faltante for ruta in rutas for faltante in funciones_sin_docstring(ruta)]
        self.assertEqual(faltantes, [])


class TestEjecucionDeEjemplos(unittest.TestCase):
    """Comprueba salidas observables de ejemplos ejecutables sin GUI."""

    def test_mayor_de_tres_muestra_el_mayor_valor(self) -> None:
        """Ejecuta el ejemplo de comparación con sus datos demostrativos."""
        resultado = ejecutar_ejemplo(SEMANA_1 / "04_mayor_de_tres.py")
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertEqual(resultado.stdout, "100\n")

    def test_fizzbuzz_conserva_las_reglas_en_su_salida(self) -> None:
        """Verifica las posiciones representativas de FizzBuzz del ejemplo."""
        resultado = ejecutar_ejemplo(SEMANA_1 / "05_fizzbuzz.py")
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        salida = resultado.stdout.splitlines()
        self.assertEqual(salida[2], "Fizz")
        self.assertEqual(salida[4], "Buzz")
        self.assertEqual(salida[14], "FizzBuzz")
        self.assertEqual(len(salida), 50)

    def test_ejemplo_de_excepciones_acepta_un_numero(self) -> None:
        """Confirma el recorrido válido del ejemplo interactivo."""
        resultado = ejecutar_ejemplo(SEMANA_2 / "13_excepciones.py", "3.5\n")
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn("El numero ingresado es: 3.5", resultado.stdout)

    def test_uso_contador_informa_el_total_real_de_acciones(self) -> None:
        """Comprueba que el ejemplo informa las tres acciones registradas."""
        resultado = ejecutar_ejemplo(SEMANA_3 / "modulos" / "uso_contador.py")
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertEqual(resultado.stdout.splitlines()[-1], "Total: 3")

    def test_paquete_utils_se_ejecuta_desde_su_miniproyecto(self) -> None:
        """Comprueba los imports públicos del paquete utils de modulo2."""
        resultado = ejecutar_ejemplo(SEMANA_3 / "modulo2" / "main.py")
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertEqual(
            resultado.stdout.splitlines(),
            ["hola mundo", "$1,234.50", "Promedio: 86.25", "python"],
        )


if __name__ == "__main__":
    unittest.main()
