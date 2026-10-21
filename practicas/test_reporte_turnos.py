"""Pruebas docentes de la etapa 3: reporte de turnos.

La clase TestCase es infraestructura entregada por el docente: no es un
requisito de programación orientada a objetos para realizar la práctica.
"""

import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO

from reporte_turnos import reporte_turnos


def _ejecutar_sin_salida(funcion, *argumentos):
    """Ejecuta una función y confirma que comunica su resultado con return."""
    salida_estandar = StringIO()
    salida_error = StringIO()
    with redirect_stdout(salida_estandar), redirect_stderr(salida_error):
        resultado = funcion(*argumentos)
    if salida_estandar.getvalue() or salida_error.getvalue():
        raise AssertionError("La función debe devolver el resultado sin imprimir.")
    return resultado


class TestEtapa3Turnos(unittest.TestCase):
    def test_reporte_combina_turnos_atendidos_y_sin_stock(self):
        resultado = _ejecutar_sin_salida(reporte_turnos, 4, 2)
        esperado = (
            "Turno 1: atendido\n"
            "Turno 2: atendido\n"
            "Turno 3: sin stock\n"
            "Turno 4: sin stock\n"
        )
        self.assertEqual(resultado, esperado)

    def test_cero_turnos_devuelve_cadena_vacia(self):
        resultado = _ejecutar_sin_salida(reporte_turnos, 0, 5)
        self.assertEqual(resultado, "")

    def test_stock_cero_deja_todos_los_turnos_sin_stock(self):
        resultado = _ejecutar_sin_salida(reporte_turnos, 3, 0)
        esperado = "Turno 1: sin stock\nTurno 2: sin stock\nTurno 3: sin stock\n"
        self.assertEqual(resultado, esperado)

    def test_stock_exacto_atiende_el_unico_turno(self):
        resultado = _ejecutar_sin_salida(reporte_turnos, 1, 1)
        self.assertEqual(resultado, "Turno 1: atendido\n")

    def test_stock_mayor_que_turnos_los_atiende_todos(self):
        resultado = _ejecutar_sin_salida(reporte_turnos, 2, 5)
        self.assertEqual(resultado, "Turno 1: atendido\nTurno 2: atendido\n")
