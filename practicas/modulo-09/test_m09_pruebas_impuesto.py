"""Evaluador docente observable de la suite que escribe el estudiante en M09."""

import importlib
import unittest
from unittest import mock

MODULO_ESTUDIANTE = "m09_pruebas_impuesto"


def ejecutar_suite(modulo):
    suite = unittest.defaultTestLoader.loadTestsFromModule(modulo)
    resultado = unittest.TestResult()
    suite.run(resultado)
    return suite.countTestCases(), resultado


class TestM09PruebasImpuesto(unittest.TestCase):
    def setUp(self):
        self.estudiante = importlib.reload(importlib.import_module(MODULO_ESTUDIANTE))

    def exigir_suite_correcta(self):
        cantidad, resultado = ejecutar_suite(self.estudiante)
        self.assertGreaterEqual(cantidad, 4, "entrega al menos cuatro pruebas")
        self.assertEqual(resultado.skipped, [], "no se permiten pruebas omitidas")
        self.assertEqual(
            resultado.expectedFailures, [], "no se permiten expected failures"
        )
        self.assertTrue(
            resultado.wasSuccessful(), "las pruebas deben pasar con las APIs correctas"
        )

    def assert_mutante_es_detectado(self, nombre, reemplazo):
        with mock.patch.object(self.estudiante, nombre, reemplazo):
            _, resultado = ejecutar_suite(self.estudiante)
        self.assertFalse(
            resultado.wasSuccessful(), f"la suite no detecta el mutante {nombre}"
        )

    def test_suite_estudiante_valida_con_api_correcta_y_cubre_mutantes(self):
        self.exigir_suite_correcta()
        subtotal_correcto = self.estudiante.calcular_subtotal
        iva_correcto = self.estudiante.aplicar_iva

        def subtotal_sin_cantidad(precio, cantidad):
            subtotal_correcto(precio, cantidad)
            return round(precio, 2)

        def subtotal_sin_cero(precio, cantidad):
            subtotal_correcto(precio, cantidad)
            if cantidad == 0:
                return round(precio, 2)
            return round(precio * cantidad, 2)

        def subtotal_sin_redondeo(precio, cantidad):
            subtotal_correcto(precio, cantidad)
            return precio * cantidad

        def subtotal_acepta_precio_negativo(precio, cantidad):
            subtotal_correcto(abs(precio), cantidad)
            return round(precio * cantidad, 2)

        def subtotal_acepta_cantidad_negativa(precio, cantidad):
            subtotal_correcto(precio, abs(cantidad))
            return round(precio * cantidad, 2)

        def iva_defecto_incorrecto(monto, tasa=0):
            return iva_correcto(monto, tasa)

        def iva_ignora_tasa_explicita(monto, tasa=0.15):
            iva_correcto(monto, tasa)
            return iva_correcto(monto)

        def iva_sin_redondeo(monto, tasa=0.15):
            iva_correcto(monto, tasa)
            return monto * (1 + tasa)

        def iva_acepta_monto_negativo(monto, tasa=0.15):
            iva_correcto(abs(monto), tasa)
            return round(monto * (1 + tasa), 2)

        def iva_acepta_tasa_negativa(monto, tasa=0.15):
            iva_correcto(monto, abs(tasa))
            return round(monto * (1 + tasa), 2)

        for nombre, reemplazo in (
            ("calcular_subtotal", subtotal_sin_cantidad),
            ("calcular_subtotal", subtotal_sin_cero),
            ("calcular_subtotal", subtotal_sin_redondeo),
            ("calcular_subtotal", subtotal_acepta_precio_negativo),
            ("calcular_subtotal", subtotal_acepta_cantidad_negativa),
            ("aplicar_iva", iva_defecto_incorrecto),
            ("aplicar_iva", iva_ignora_tasa_explicita),
            ("aplicar_iva", iva_sin_redondeo),
            ("aplicar_iva", iva_acepta_monto_negativo),
            ("aplicar_iva", iva_acepta_tasa_negativa),
        ):
            with self.subTest(mutante=reemplazo.__name__):
                self.assert_mutante_es_detectado(nombre, reemplazo)


if __name__ == "__main__":
    unittest.main()
