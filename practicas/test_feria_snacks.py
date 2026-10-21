"""Pruebas docentes del proyecto Puesto de snacks de la feria.

Las clases TestCase son infraestructura entregada por el docente: no son un
requisito de programación orientada a objetos para realizar la práctica.
"""

import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO

from feria_snacks import calcular_total, etiqueta_pedido, reporte_turnos


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
