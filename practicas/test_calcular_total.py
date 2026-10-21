"""Pruebas docentes de la etapa 2: total de pedido.

La clase TestCase es infraestructura entregada por el docente: no es un
requisito de programación orientada a objetos para realizar la práctica.
"""

import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO

from calcular_total import calcular_total


def _ejecutar_sin_salida(funcion, *argumentos):
    """Ejecuta una función y confirma que comunica su resultado con return."""
    salida_estandar = StringIO()
    salida_error = StringIO()
    with redirect_stdout(salida_estandar), redirect_stderr(salida_error):
        resultado = funcion(*argumentos)
    if salida_estandar.getvalue() or salida_error.getvalue():
        raise AssertionError("La función debe devolver el resultado sin imprimir.")
    return resultado


class TestEtapa2Total(unittest.TestCase):
    def test_total_del_ejemplo_principal(self):
        resultado = _ejecutar_sin_salida(calcular_total, 2.5, 3)
        self.assertIsNotNone(resultado)
        self.assertAlmostEqual(resultado, 7.5)

    def test_total_multiplica_por_la_cantidad(self):
        resultado = _ejecutar_sin_salida(calcular_total, 4, 3)
        self.assertIsNotNone(resultado)
        self.assertAlmostEqual(resultado, 12.0)

    def test_total_se_redondea_a_dos_decimales(self):
        for precio in (1.235, 1.237):
            with self.subTest(precio=precio):
                resultado = _ejecutar_sin_salida(calcular_total, precio, 3)
                self.assertIsNotNone(resultado)
                self.assertAlmostEqual(resultado, 3.71)

    def test_ceros_producen_total_cero(self):
        total_sin_unidades = _ejecutar_sin_salida(calcular_total, 4, 0)
        total_sin_precio = _ejecutar_sin_salida(calcular_total, 0, 8)
        self.assertIsNotNone(total_sin_unidades)
        self.assertIsNotNone(total_sin_precio)
        self.assertAlmostEqual(total_sin_unidades, 0.0)
        self.assertAlmostEqual(total_sin_precio, 0.0)
