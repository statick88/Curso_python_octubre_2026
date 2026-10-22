"""Verificación docente de la práctica M04: recibo de envío."""

import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

from m04_recibo_envio import calcular_envio, crear_recibo


class TestM04ReciboEnvio(unittest.TestCase):
    def llamar(self, funcion, *args, **kwargs):
        salida, errores = io.StringIO(), io.StringIO()
        with redirect_stdout(salida), redirect_stderr(errores):
            resultado = funcion(*args, **kwargs)
        return resultado, salida.getvalue(), errores.getvalue()

    def test_calcular_envio_usa_tarifa_predeterminada_y_redondea(self):
        resultado, salida, errores = self.llamar(calcular_envio, 2.5)
        self.assertIsNotNone(resultado, "calcular_envio debe devolver un costo")
        self.assertEqual(7.5, resultado)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

        redondeado, salida, errores = self.llamar(calcular_envio, 1.234, 2)
        self.assertIsNotNone(redondeado, "calcular_envio debe devolver un costo")
        self.assertEqual(2.47, redondeado)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

    def test_calcular_envio_admite_argumentos_posicionales_y_por_nombre(self):
        posicional, salida, errores = self.llamar(calcular_envio, 2.5, 4)
        self.assertIsNotNone(posicional, "calcular_envio debe devolver un costo")
        self.assertEqual(10.0, posicional)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

        por_nombre, salida, errores = self.llamar(calcular_envio, peso=2.5, tarifa=4)
        self.assertIsNotNone(por_nombre, "calcular_envio debe devolver un costo")
        self.assertEqual(10.0, por_nombre)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

        tarifa_cero, salida, errores = self.llamar(calcular_envio, 2.5, tarifa=0)
        self.assertIsNotNone(
            tarifa_cero, "calcular_envio debe respetar una tarifa explícita de cero"
        )
        self.assertEqual(0.0, tarifa_cero)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

    def test_calcular_envio_acepta_peso_cero(self):
        resultado, salida, errores = self.llamar(calcular_envio, 0)
        self.assertIsNotNone(resultado, "calcular_envio debe devolver un costo")
        self.assertEqual(0.0, resultado)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

    def test_crear_recibo_compone_costo_y_formato_exacto(self):
        recibo, salida, errores = self.llamar(crear_recibo, "Loja", 2.5)
        self.assertIsNotNone(recibo, "crear_recibo debe devolver un recibo")
        self.assertEqual("Envío a Loja: $7.50", recibo)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

        recibo, salida, errores = self.llamar(crear_recibo, "Quito", 1.234, tarifa=2)
        self.assertIsNotNone(recibo, "crear_recibo debe devolver un recibo")
        self.assertEqual("Envío a Quito: $2.47", recibo)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

        recibo_cero, salida, errores = self.llamar(
            crear_recibo, "Cuenca", 2.5, tarifa=0
        )
        self.assertIsNotNone(recibo_cero, "crear_recibo debe devolver un recibo")
        self.assertEqual("Envío a Cuenca: $0.00", recibo_cero)
        self.assertEqual("", salida)
        self.assertEqual("", errores)


if __name__ == "__main__":
    unittest.main()
