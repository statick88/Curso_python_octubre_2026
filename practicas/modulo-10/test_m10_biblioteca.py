"""Comprobaciones docentes para la práctica M10."""

import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

from m10_biblioteca import cargar_lecturas, guardar_reporte, resumir_por_estado


class TestM10Biblioteca(unittest.TestCase):
    def escribir_json(self, ruta, valor):
        ruta.write_text(json.dumps(valor, ensure_ascii=False), encoding="utf-8")

    def llamar_sin_salida(self, funcion, *args):
        salida, errores = io.StringIO(), io.StringIO()
        with redirect_stdout(salida), redirect_stderr(errores):
            resultado = funcion(*args)
        self.assertEqual(salida.getvalue(), "")
        self.assertEqual(errores.getvalue(), "")
        return resultado

    def test_carga_registros_validos_preserva_orden_y_bytes(self):
        with tempfile.TemporaryDirectory() as temporal:
            ruta = Path(temporal) / "lecturas.json"
            esperado = [
                {"titulo": "Python", "estado": "pendiente"},
                {"titulo": "Cien años", "estado": "leido"},
            ]
            self.escribir_json(ruta, esperado)
            original = ruta.read_bytes()
            self.assertEqual(self.llamar_sin_salida(cargar_lecturas, ruta), esperado)
            self.assertEqual(ruta.read_bytes(), original)

    def test_lectura_ausente_y_json_o_esquema_invalido_no_emiten_salida(self):
        with tempfile.TemporaryDirectory() as temporal:
            base = Path(temporal)
            salida, errores = io.StringIO(), io.StringIO()
            with (
                redirect_stdout(salida),
                redirect_stderr(errores),
                self.assertRaises(FileNotFoundError),
            ):
                cargar_lecturas(base / "ausente.json")
            self.assertEqual(salida.getvalue(), "")
            self.assertEqual(errores.getvalue(), "")
            for valor in (
                "{no json",
                {"estado": "leido"},
                [{"titulo": "", "estado": "leido"}],
                [{"titulo": 7, "estado": "leido"}],
                [{"titulo": "Python"}],
                [{"titulo": "Python", "estado": 7}],
                [{"titulo": "Python", "estado": "nuevo"}],
            ):
                ruta = base / "invalido.json"
                if isinstance(valor, str):
                    ruta.write_text(valor, encoding="utf-8")
                else:
                    self.escribir_json(ruta, valor)
                original = ruta.read_bytes()
                salida, errores = io.StringIO(), io.StringIO()
                with (
                    self.subTest(valor=valor),
                    redirect_stdout(salida),
                    redirect_stderr(errores),
                    self.assertRaises(ValueError),
                ):
                    cargar_lecturas(ruta)
                self.assertEqual(salida.getvalue(), "")
                self.assertEqual(errores.getvalue(), "")
                self.assertEqual(ruta.read_bytes(), original)

    def test_resume_ambos_estados_sin_mutar_entrada_ni_emitir_salida(self):
        items = [
            {"titulo": "A", "estado": "pendiente"},
            {"titulo": "B", "estado": "leido"},
            {"titulo": "C", "estado": "leido"},
        ]
        copia = [item.copy() for item in items]
        self.assertEqual(
            self.llamar_sin_salida(resumir_por_estado, items),
            {"pendiente": 1, "leido": 2},
        )
        self.assertEqual(items, copia)
        self.assertEqual(
            self.llamar_sin_salida(resumir_por_estado, []),
            {"pendiente": 0, "leido": 0},
        )

    def test_guarda_reporte_nuevo_no_muta_resumen_y_rechaza_sobrescritura(self):
        with tempfile.TemporaryDirectory() as temporal:
            ruta = Path(temporal) / "reporte.json"
            resumen = {"pendiente": 1, "leido": 2}
            copia = resumen.copy()
            self.assertIsNone(self.llamar_sin_salida(guardar_reporte, ruta, resumen))
            self.assertTrue(
                ruta.exists(), "guardar_reporte debe crear un archivo nuevo"
            )
            self.assertEqual(json.loads(ruta.read_text(encoding="utf-8")), resumen)
            self.assertEqual(resumen, copia)
            previo = ruta.read_bytes()
            salida, errores = io.StringIO(), io.StringIO()
            with (
                redirect_stdout(salida),
                redirect_stderr(errores),
                self.assertRaises(FileExistsError),
            ):
                guardar_reporte(ruta, resumen)
            self.assertEqual(salida.getvalue(), "")
            self.assertEqual(errores.getvalue(), "")
            self.assertEqual(ruta.read_bytes(), previo)
            self.assertEqual(resumen, copia)

    def test_pipeline_independiente_usa_archivos_temporales_sin_salida(self):
        with tempfile.TemporaryDirectory() as temporal:
            base = Path(temporal)
            origen, reporte = base / "lecturas.json", base / "reporte.json"
            registros = [
                {"titulo": "Árbol", "estado": "pendiente"},
                {"titulo": "B", "estado": "leido"},
            ]
            self.escribir_json(origen, registros)
            original = origen.read_bytes()
            cargados = self.llamar_sin_salida(cargar_lecturas, origen)
            resumen = self.llamar_sin_salida(resumir_por_estado, cargados)
            self.assertIsNotNone(resumen, "resumir_por_estado debe devolver un resumen")
            copia_resumen = resumen.copy()
            self.assertIsNone(self.llamar_sin_salida(guardar_reporte, reporte, resumen))
            self.assertTrue(reporte.exists(), "el pipeline debe crear el reporte")
            self.assertEqual(
                json.loads(reporte.read_text(encoding="utf-8")),
                {"pendiente": 1, "leido": 1},
            )
            self.assertEqual(origen.read_bytes(), original)
            self.assertEqual(resumen, copia_resumen)


if __name__ == "__main__":
    unittest.main()
