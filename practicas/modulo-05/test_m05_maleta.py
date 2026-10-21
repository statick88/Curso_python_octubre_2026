"""Verificación docente de la práctica M05: organización de una maleta."""

import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

from m05_maleta import invertir_itinerario, peso_total, seleccionar_livianos


class TestM05Maleta(unittest.TestCase):
    def llamar(self, funcion, *args):
        salida, errores = io.StringIO(), io.StringIO()
        with redirect_stdout(salida), redirect_stderr(errores):
            resultado = funcion(*args)
        return resultado, salida.getvalue(), errores.getvalue()

    def test_peso_total_suma_y_acepta_coleccion_vacia(self):
        pesos = [1.2, 2.3, 0.5]
        resultado, salida, errores = self.llamar(peso_total, pesos)
        self.assertIsNotNone(resultado, "peso_total debe devolver un total")
        self.assertEqual(4.0, resultado)
        self.assertEqual([1.2, 2.3, 0.5], pesos)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

        unico = [3]
        resultado, salida, errores = self.llamar(peso_total, unico)
        self.assertIsNotNone(resultado, "peso_total debe devolver un total")
        self.assertEqual(3, resultado)
        self.assertEqual([3], unico)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

        entrada_vacia = []
        vacio, salida, errores = self.llamar(peso_total, entrada_vacia)
        self.assertIsNotNone(vacio, "peso_total debe devolver un total")
        self.assertEqual(0, vacio)
        self.assertEqual([], entrada_vacia)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

    def test_seleccionar_livianos_incluye_igualdad_y_conserva_orden(self):
        pesos = [5, 2, 5, 1]
        original = pesos[:]
        resultado, salida, errores = self.llamar(seleccionar_livianos, pesos, 5)
        self.assertIsNotNone(resultado, "seleccionar_livianos debe devolver una lista")
        self.assertEqual([5, 2, 5, 1], resultado)
        self.assertEqual(original, pesos)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

    def test_seleccionar_livianos_devuelve_lista_nueva_y_maneja_vacio(self):
        pesos = [1, 4, 7]
        resultado, salida, errores = self.llamar(seleccionar_livianos, pesos, 4)
        self.assertIsNotNone(resultado, "seleccionar_livianos debe devolver una lista")
        self.assertEqual([1, 4], resultado)
        self.assertIsNot(resultado, pesos)
        resultado.append(99)
        self.assertEqual([1, 4, 7], pesos)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

        todos_livianos = [1, 4]
        resultado, salida, errores = self.llamar(
            seleccionar_livianos, todos_livianos, 4
        )
        self.assertIsNotNone(resultado, "seleccionar_livianos debe devolver una lista")
        self.assertEqual([1, 4], resultado)
        self.assertIsNot(resultado, todos_livianos)
        resultado.append(99)
        self.assertEqual([1, 4], todos_livianos)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

        entrada_vacia = []
        vacio, salida, errores = self.llamar(seleccionar_livianos, entrada_vacia, 4)
        self.assertIsNotNone(vacio, "seleccionar_livianos debe devolver una lista")
        self.assertEqual([], vacio)
        self.assertIsNot(vacio, entrada_vacia)
        vacio.append(99)
        self.assertEqual([], entrada_vacia)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

    def test_invertir_itinerario_devuelve_lista_invertida_sin_modificar_tupla(self):
        paradas = ("Quito", "Ambato", "Loja")
        resultado, salida, errores = self.llamar(invertir_itinerario, paradas)
        self.assertIsNotNone(resultado, "invertir_itinerario debe devolver una lista")
        self.assertEqual(["Loja", "Ambato", "Quito"], resultado)
        self.assertIsInstance(resultado, list)
        self.assertEqual(("Quito", "Ambato", "Loja"), paradas)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

    def test_invertir_itinerario_acepta_tupla_vacia_y_un_elemento(self):
        vacio, salida, errores = self.llamar(invertir_itinerario, ())
        self.assertIsNotNone(vacio, "invertir_itinerario debe devolver una lista")
        self.assertEqual([], vacio)
        self.assertEqual("", salida)
        self.assertEqual("", errores)

        unico, salida, errores = self.llamar(invertir_itinerario, ("Cuenca",))
        self.assertIsNotNone(unico, "invertir_itinerario debe devolver una lista")
        self.assertEqual(["Cuenca"], unico)
        self.assertEqual("", salida)
        self.assertEqual("", errores)


if __name__ == "__main__":
    unittest.main()
