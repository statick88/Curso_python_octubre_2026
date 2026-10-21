"""Comprobaciones docentes para la práctica M08."""

import unittest

from m08_saludos import construir_saludo


class TestM08Saludos(unittest.TestCase):
    def test_saluda_en_la_manana_con_exportacion_publica(self):
        self.assertEqual(construir_saludo("Ana", "manana"), "Buenos días, Ana.")

    def test_saluda_en_la_tarde(self):
        self.assertEqual(construir_saludo("Luis", "tarde"), "Buenas tardes, Luis.")

    def test_saluda_en_la_noche(self):
        self.assertEqual(construir_saludo("Zoé", "noche"), "Buenas noches, Zoé.")


if __name__ == "__main__":
    unittest.main()
