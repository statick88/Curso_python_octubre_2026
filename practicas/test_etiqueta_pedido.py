"""Pruebas docentes de la etapa 1: etiqueta de pedido.

La clase TestCase es infraestructura entregada por el docente: no es un
requisito de programación orientada a objetos para realizar la práctica.
"""

import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO

from etiqueta_pedido import etiqueta_pedido


def _ejecutar_sin_salida(funcion, *argumentos):
    """Ejecuta una función y confirma que comunica su resultado con return."""
    salida_estandar = StringIO()
    salida_error = StringIO()
    with redirect_stdout(salida_estandar), redirect_stderr(salida_error):
        resultado = funcion(*argumentos)
    if salida_estandar.getvalue() or salida_error.getvalue():
        raise AssertionError("La función debe devolver el resultado sin imprimir.")
    return resultado


class TestEtapa1Etiqueta(unittest.TestCase):
    def test_formato_del_ejemplo_principal(self):
        resultado = _ejecutar_sin_salida(etiqueta_pedido, "Feria", "Jugo", 3)
        self.assertEqual(resultado, "Feria | 3 x Jugo")

    def test_cantidad_cero_se_conserva_en_la_etiqueta(self):
        resultado = _ejecutar_sin_salida(etiqueta_pedido, "Patio", "Pan", 0)
        self.assertEqual(resultado, "Patio | 0 x Pan")

    def test_datos_se_muestran_tal_como_se_reciben(self):
        for evento, producto in (
            ("Feria escolar", "Jugo natural"),
            (" Feria ", " Pan "),
        ):
            with self.subTest(evento=evento, producto=producto):
                resultado = _ejecutar_sin_salida(etiqueta_pedido, evento, producto, 12)
                self.assertEqual(resultado, evento + " | 12 x " + producto)
