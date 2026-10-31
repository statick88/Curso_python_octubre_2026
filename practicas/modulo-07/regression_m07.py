"""Regresión adicional de M07 para filas CSV con columnas no declaradas.

No usa el prefijo ``test_`` para conservar el conteo de pruebas docentes.
Ejecútala explícitamente desde la raíz con:
``python3 practicas/modulo-07/regression_m07.py -v``.
"""

import io
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

from m07_exportar_inventario import exportar_inventario


class TestRegresionM07ColumnasExtra(unittest.TestCase):
    """Verifica que una fila con columnas extra se rechaza sin efectos laterales."""

    def _ejecutar_rechazo(self, destino_existente):
        """Ejecuta el caso inválido y devuelve los bytes originales relevantes."""
        with tempfile.TemporaryDirectory() as temporal:
            base = Path(temporal)
            origen = base / "inventario.csv"
            destino = base / "reporte.json"
            origen.write_text(
                "nombre,cantidad\ncuaderno,2,detalle-extra\n",
                encoding="utf-8",
                newline="",
            )
            origen_original = origen.read_bytes()
            destino_original = b'{"existente": true}\n'
            if destino_existente:
                destino.write_bytes(destino_original)

            salida, errores = io.StringIO(), io.StringIO()
            with (
                redirect_stdout(salida),
                redirect_stderr(errores),
                self.assertRaises(ValueError),
            ):
                exportar_inventario(origen, destino)

            self.assertEqual(salida.getvalue(), "")
            self.assertEqual(errores.getvalue(), "")
            self.assertEqual(origen.read_bytes(), origen_original)
            if destino_existente:
                self.assertEqual(destino.read_bytes(), destino_original)
            else:
                self.assertFalse(destino.exists())

    def test_columna_extra_no_crea_destino_ausente(self):
        """Verifica destino ausente y origen byte a byte intactos."""
        self._ejecutar_rechazo(destino_existente=False)

    def test_columna_extra_no_altera_destino_existente(self):
        """Verifica destino existente y origen byte a byte intactos."""
        self._ejecutar_rechazo(destino_existente=True)


if __name__ == "__main__":
    unittest.main()
