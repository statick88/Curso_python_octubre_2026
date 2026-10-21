"""Comprobaciones docentes para la práctica M07."""

import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

from m07_exportar_inventario import exportar_inventario


class TestM07ExportarInventario(unittest.TestCase):
    def escribir(self, ruta, contenido):
        ruta.write_text(contenido, encoding="utf-8", newline="")

    def llamar_sin_salida(self, funcion, *args):
        salida, errores = io.StringIO(), io.StringIO()
        with redirect_stdout(salida), redirect_stderr(errores):
            resultado = funcion(*args)
        self.assertEqual(salida.getvalue(), "")
        self.assertEqual(errores.getvalue(), "")
        return resultado

    def test_exporta_filas_validas_en_orden_y_con_enteros(self):
        with tempfile.TemporaryDirectory() as temporal:
            base = Path(temporal)
            origen, destino = base / "inventario.csv", base / "reporte.json"
            contenido = "nombre,cantidad\ncuaderno,2\nñame,0\n"
            self.escribir(origen, contenido)
            original = origen.read_bytes()
            cantidad = self.llamar_sin_salida(exportar_inventario, origen, destino)
            self.assertEqual(cantidad, 2)
            self.assertEqual(
                json.loads(destino.read_text(encoding="utf-8")),
                [
                    {"nombre": "cuaderno", "cantidad": 2},
                    {"nombre": "ñame", "cantidad": 0},
                ],
            )
            self.assertEqual(origen.read_bytes(), original)

    def test_encabezado_sin_filas_crea_lista_vacia(self):
        with tempfile.TemporaryDirectory() as temporal:
            base = Path(temporal)
            origen, destino = base / "vacio.csv", base / "vacio.json"
            self.escribir(origen, "nombre,cantidad\n")
            original = origen.read_bytes()
            self.assertEqual(
                self.llamar_sin_salida(exportar_inventario, origen, destino), 0
            )
            self.assertEqual(json.loads(destino.read_text(encoding="utf-8")), [])
            self.assertEqual(origen.read_bytes(), original)

    def test_origen_ausente_no_crea_salida_ni_emite_salida(self):
        with tempfile.TemporaryDirectory() as temporal:
            base = Path(temporal)
            destino = base / "no_debe_existir.json"
            salida, errores = io.StringIO(), io.StringIO()
            with (
                redirect_stdout(salida),
                redirect_stderr(errores),
                self.assertRaises(FileNotFoundError),
            ):
                exportar_inventario(base / "ausente.csv", destino)
            self.assertEqual(salida.getvalue(), "")
            self.assertEqual(errores.getvalue(), "")
            self.assertFalse(destino.exists())

    def test_csv_malformado_eleva_valueerror_y_no_crea_salida(self):
        casos = (
            "producto,cantidad\na,1\n",
            "nombre,cantidad\n,2\n",
            "nombre,cantidad\na,-1\n",
            "nombre,cantidad\na,uno\n",
        )
        for contenido in casos:
            with (
                self.subTest(contenido=contenido),
                tempfile.TemporaryDirectory() as temporal,
            ):
                base = Path(temporal)
                origen, destino = base / "malo.csv", base / "malo.json"
                self.escribir(origen, contenido)
                original = origen.read_bytes()
                salida, errores = io.StringIO(), io.StringIO()
                with (
                    redirect_stdout(salida),
                    redirect_stderr(errores),
                    self.assertRaises(ValueError),
                ):
                    exportar_inventario(origen, destino)
                self.assertEqual(salida.getvalue(), "")
                self.assertEqual(errores.getvalue(), "")
                self.assertFalse(destino.exists())
                self.assertEqual(origen.read_bytes(), original)

    def test_destino_existente_permanece_identico_y_no_muta_origen(self):
        with tempfile.TemporaryDirectory() as temporal:
            base = Path(temporal)
            origen, destino = base / "inventario.csv", base / "reporte.json"
            contenido, previo = "nombre,cantidad\na,1\n", b'{"anterior": true}\n'
            self.escribir(origen, contenido)
            original = origen.read_bytes()
            destino.write_bytes(previo)
            salida, errores = io.StringIO(), io.StringIO()
            with (
                redirect_stdout(salida),
                redirect_stderr(errores),
                self.assertRaises(FileExistsError),
            ):
                exportar_inventario(origen, destino)
            self.assertEqual(salida.getvalue(), "")
            self.assertEqual(errores.getvalue(), "")
            self.assertEqual(destino.read_bytes(), previo)
            self.assertEqual(origen.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
