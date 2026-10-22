"""Regresiones docentes de organización; no califican soluciones estudiantiles."""

import os
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COUNTS = (4, 3, 5, 5, 4, 5, 6, 5, 3, 1, 5)


class TestPracticeDiscovery(unittest.TestCase):
    def comprobar_comando(self, cantidad, *argumentos):
        resultado = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", *argumentos, "-v"],
            cwd=ROOT,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )
        self.assertEqual(resultado.stdout, "")
        self.assertRegex(resultado.stderr, rf"Ran {cantidad} tests? in ")
        self.assertNotRegex(
            resultado.stderr, re.compile(r"^ERROR:|skipped=", re.MULTILINE)
        )
        self.assertRegex(resultado.stderr, r"\n(?:OK|FAILED \(failures=\d+\))\s*$")
        esperado = 1 if "FAILED (" in resultado.stderr else 0
        self.assertEqual(resultado.returncode, esperado)

    def test_descubrimiento_global_y_modulos(self):
        for patron, cantidad in (("test_*.py", 58), ("test_m*.py", 46)):
            with self.subTest(patron=patron):
                self.comprobar_comando(cantidad, "-s", "practicas", "-p", patron)

    def test_selector_heredado_conserva_doce_pruebas(self):
        self.comprobar_comando(
            12, "-s", "practicas", "-p", "test_*.py", "-k", "TestEtapa"
        )

    def test_cada_modulo_tiene_un_comando_independiente(self):
        for modulo, cantidad in enumerate(COUNTS):
            with self.subTest(modulo=modulo):
                self.comprobar_comando(
                    cantidad,
                    "-s",
                    f"practicas/modulo-{modulo:02d}",
                    "-p",
                    f"test_m{modulo:02d}_*.py",
                )


if __name__ == "__main__":
    unittest.main()
