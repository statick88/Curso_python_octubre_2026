"""Pruebas docentes de la tarjeta interactiva del módulo 1."""

import builtins
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO

from m01_tarjeta_presentacion import presentarse


class TestM01TarjetaPresentacion(unittest.TestCase):
    def _probar_tarjeta(self, respuestas, esperado):
        llamadas = []
        originales = builtins.input

        def entrada_falsa(mensaje):
            llamadas.append(mensaje)
            return respuestas.pop(0)

        salida = StringIO()
        errores = StringIO()
        try:
            builtins.input = entrada_falsa
            with redirect_stdout(salida), redirect_stderr(errores):
                resultado = presentarse()
        finally:
            builtins.input = originales
        self.assertEqual(llamadas, ["Nombre: ", "Ciudad: "])
        self.assertEqual(salida.getvalue(), esperado)
        self.assertEqual(errores.getvalue(), "")
        self.assertIsNone(resultado)

    def test_tarjeta_del_ejemplo(self):
        self._probar_tarjeta(["Ana", "Quito"], "Hola, soy Ana y vivo en Quito.\n")

    def test_conserva_textos_validos_sin_reintentos(self):
        self._probar_tarjeta(
            ["Luis M.", "Loja Norte"], "Hola, soy Luis M. y vivo en Loja Norte.\n"
        )

    def test_conserva_espacios_validos_en_los_textos(self):
        self._probar_tarjeta(
            [" Ana ", " Quito "], "Hola, soy  Ana  y vivo en  Quito .\n"
        )
