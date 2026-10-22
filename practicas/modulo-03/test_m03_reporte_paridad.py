"""Pruebas docentes del reporte de paridad del módulo 3."""

import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO

from m03_reporte_paridad import contar_pares, reporte_paridad


def _sin_salida(funcion, *argumentos):
    """Comprueba que una función comunica su resultado mediante return."""
    salida = StringIO()
    errores = StringIO()
    with redirect_stdout(salida), redirect_stderr(errores):
        resultado = funcion(*argumentos)
    if salida.getvalue() or errores.getvalue():
        raise AssertionError("La función no debe imprimir ni escribir errores.")
    return resultado


class TestM03ReporteParidad(unittest.TestCase):
    def test_reporte_del_ejemplo_inclusivo(self):
        resultado = _sin_salida(reporte_paridad, 2, 3)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado, "2: par\n3: impar\n")

    def test_reporte_acepta_limites_negativos_y_cero(self):
        resultado = _sin_salida(reporte_paridad, -1, 1)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado, "-1: impar\n0: par\n1: impar\n")

    def test_reporte_de_un_solo_limite_par_e_impar(self):
        for numero, esperado in ((0, "0: par\n"), (-3, "-3: impar\n")):
            with self.subTest(numero=numero):
                resultado = _sin_salida(reporte_paridad, numero, numero)
                self.assertIsNotNone(resultado)
                self.assertEqual(resultado, esperado)

    def test_contar_pares_en_ejemplo_y_limites(self):
        for inicio, fin, esperado in ((2, 3, 1), (-2, 2, 3), (0, 0, 1), (-3, -3, 0)):
            with self.subTest(inicio=inicio, fin=fin):
                resultado = _sin_salida(contar_pares, inicio, fin)
                self.assertIsNotNone(resultado)
                self.assertEqual(resultado, esperado)

    def test_contar_pares_no_omite_el_limite_final(self):
        resultado = _sin_salida(contar_pares, 1, 2)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado, 1)
