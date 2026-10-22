"""Verificación docente de la práctica M06: votación de un club."""

import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

from m06_votacion_club import candidatos_unicos, contar_votos, ganador


class TestM06VotacionClub(unittest.TestCase):
    def llamar(self, funcion, *args):
        salida, errores = io.StringIO(), io.StringIO()
        with redirect_stdout(salida), redirect_stderr(errores):
            resultado = funcion(*args)
        return resultado, salida.getvalue(), errores.getvalue()

    def test_contar_votos_cuenta_repetidos_y_no_modifica_lista(self):
        votos = ["Ana", "Luis", "Ana", "Mia"]
        original = votos[:]
        resultado, salida, errores = self.llamar(contar_votos, votos)
        self.assertIsNotNone(resultado, "contar_votos debe devolver un diccionario")
        self.assertEqual({"Ana": 2, "Luis": 1, "Mia": 1}, resultado)
        self.assertEqual(original, votos)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

    def test_contar_votos_acepta_lista_vacia(self):
        votos = []
        resultado, salida, errores = self.llamar(contar_votos, votos)
        self.assertIsNotNone(resultado, "contar_votos debe devolver un diccionario")
        self.assertEqual({}, resultado)
        self.assertEqual([], votos)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

    def test_candidatos_unicos_elimina_duplicados_y_no_modifica_lista(self):
        votos = ["Ana", "Luis", "Ana", "Mia"]
        original = votos[:]
        resultado, salida, errores = self.llamar(candidatos_unicos, votos)
        self.assertIsNotNone(resultado, "candidatos_unicos debe devolver un set")
        self.assertIsInstance(resultado, set)
        self.assertEqual({"Ana", "Luis", "Mia"}, resultado)
        self.assertEqual(original, votos)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

    def test_candidatos_unicos_acepta_lista_vacia(self):
        resultado, salida, errores = self.llamar(candidatos_unicos, [])
        self.assertIsNotNone(resultado, "candidatos_unicos debe devolver un set")
        self.assertIsInstance(resultado, set)
        self.assertEqual(set(), resultado)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

    def test_ganador_devuelve_maximo_unico_y_no_modifica_diccionario(self):
        conteo = {"Luis": 1, "Ana": 3, "Mia": 2}
        original = conteo.copy()
        resultado, salida, errores = self.llamar(ganador, conteo)
        self.assertIsNotNone(resultado, "ganador debe devolver el candidato único")
        self.assertEqual("Ana", resultado)
        self.assertEqual(original, conteo)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

        unico = {"Ana": 2}
        resultado, salida, errores = self.llamar(ganador, unico)
        self.assertIsNotNone(resultado, "ganador debe devolver un candidato único")
        self.assertEqual("Ana", resultado)
        self.assertEqual({"Ana": 2}, unico)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

    def test_ganador_devuelve_none_para_empate_y_conteo_vacio(self):
        unico, salida, errores = self.llamar(ganador, {"Ana": 2, "Luis": 1})
        self.assertIsNotNone(unico, "ganador debe resolver antes los máximos únicos")
        self.assertEqual("Ana", unico)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

        empate = {"Ana": 2, "Luis": 2, "Mia": 1}
        original = empate.copy()
        resultado, salida, errores = self.llamar(ganador, empate)
        self.assertIsNone(resultado)
        self.assertEqual(original, empate)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

        vacio = {}
        resultado, salida, errores = self.llamar(ganador, vacio)
        self.assertIsNone(resultado)
        self.assertEqual({}, vacio)
        self.assertEqual("", salida)
        self.assertEqual("", errores)


if __name__ == "__main__":
    unittest.main()
