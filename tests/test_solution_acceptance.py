"""Aceptación exclusiva de la rama solucion, sobre las funciones reales."""

import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestSolutionAcceptance(unittest.TestCase):
    def test_todos_los_contratos_docentes_pasan_sin_sustituciones(self):
        resultado = subprocess.run(
            [
                sys.executable,
                "-m",
                "unittest",
                "discover",
                "-s",
                "practicas",
                "-p",
                "test_*.py",
                "-v",
            ],
            cwd=ROOT,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            capture_output=True,
            text=True,
            timeout=15,
            check=False,
        )
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertEqual(resultado.stdout, "")
        self.assertRegex(resultado.stderr, r"Ran 58 tests in ")
        self.assertNotRegex(
            resultado.stderr, re.compile(r"^ERROR:|^FAIL:|skipped=", re.MULTILINE)
        )
        self.assertRegex(resultado.stderr, r"\nOK\s*$")
