"""Pruebas docentes del presupuesto de viaje del módulo 2."""

import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO

from m02_presupuesto_viaje import (
    calcular_costo,
    formatear_presupuesto,
    normalizar_destino,
)


def _sin_salida(funcion, *argumentos):
    """Ejecuta una función y confirma que su respuesta llega por return."""
    salida = StringIO()
    errores = StringIO()
    with redirect_stdout(salida), redirect_stderr(errores):
        resultado = funcion(*argumentos)
    if salida.getvalue() or errores.getvalue():
        raise AssertionError("La función no debe imprimir ni escribir errores.")
    return resultado


class TestM02PresupuestoViaje(unittest.TestCase):
    def test_calcular_costo_ejemplos_y_cero(self):
        for distancia, tarifa, esperado in (
            ("12", "0.35", 4.2),
            ("0", "2.5", 0.0),
            ("12", "0", 0.0),
        ):
            with self.subTest(distancia=distancia, tarifa=tarifa):
                resultado = _sin_salida(calcular_costo, distancia, tarifa)
                self.assertIsNotNone(resultado)
                self.assertIsInstance(resultado, (int, float))
                self.assertAlmostEqual(resultado, esperado)

    def test_calcular_costo_redondea_a_dos_decimales_y_preserva_textos(self):
        distancia = "2.675"
        tarifa = "1"
        resultado = _sin_salida(calcular_costo, distancia, tarifa)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado, 2.67)
        self.assertEqual((distancia, tarifa), ("2.675", "1"))

    def test_normalizar_destino_ejemplos_y_espacios(self):
        for destino, esperado in ((" loja ", "Loja"), ("  quITO  ", "Quito")):
            with self.subTest(destino=destino):
                original = destino
                resultado = _sin_salida(normalizar_destino, destino)
                self.assertIsNotNone(resultado)
                self.assertEqual(resultado, esperado)
                self.assertEqual(destino, original)

    def test_formatear_presupuesto_compone_el_ejemplo_sin_mutar(self):
        destino = " loja "
        costo = 4.2
        resultado = _sin_salida(formatear_presupuesto, destino, costo)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado, "Viaje a Loja: $4.20")
        self.assertEqual((destino, costo), (" loja ", 4.2))

    def test_formatear_presupuesto_respeta_dos_decimales_y_cero(self):
        self.assertEqual(
            _sin_salida(formatear_presupuesto, "quito", 0), "Viaje a Quito: $0.00"
        )
        self.assertEqual(
            _sin_salida(formatear_presupuesto, "cuenca", 7.5), "Viaje a Cuenca: $7.50"
        )
