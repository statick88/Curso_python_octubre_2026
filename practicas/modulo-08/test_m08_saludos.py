"""Comprobaciones docentes para la práctica M08."""

import unittest

from m08_saludos import construir_saludo


class TestM08Saludos(unittest.TestCase):
    def test_saluda_en_la_manana_con_exportacion_publica(self):
        """Verifica el saludo matutino desde la API pública."""
        self.assertEqual(construir_saludo("Ana", "manana"), "Buenos días, Ana.")

    def test_saluda_en_la_tarde(self):
        """Verifica el saludo correspondiente a la tarde."""
        self.assertEqual(construir_saludo("Luis", "tarde"), "Buenas tardes, Luis.")

    def test_saluda_en_la_noche(self):
        """Verifica el saludo correspondiente a la noche."""
        self.assertEqual(construir_saludo("Zoé", "noche"), "Buenas noches, Zoé.")


if __name__ == "__main__":
    unittest.main()
