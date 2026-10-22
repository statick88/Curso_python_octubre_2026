"""Solución M09: pruebas públicas de cantidades, tasas, redondeo y errores."""

import unittest

from soporte_m09_impuestos import aplicar_iva, calcular_subtotal

__all__ = ["TestM09ImpuestosDelEstudiante", "aplicar_iva", "calcular_subtotal"]


class TestM09ImpuestosDelEstudiante(unittest.TestCase):
    """Cada método cubre una regla sin reemplazar las funciones docentes."""

    def test_subtotal_cantidad_y_redondeo(self):
        self.assertEqual(calcular_subtotal(2.5, 3), 7.5)
        self.assertEqual(calcular_subtotal(1.237, 3), 3.71)

    def test_subtotal_cero_y_errores(self):
        self.assertEqual(calcular_subtotal(0, 3), 0)
        self.assertEqual(calcular_subtotal(2, 0), 0)
        # Cada argumento negativo se comprueba por separado.
        with self.assertRaises(ValueError):
            calcular_subtotal(-1, 2)
        with self.assertRaises(ValueError):
            calcular_subtotal(1, -2)

    def test_iva_tasas_y_redondeo(self):
        self.assertEqual(aplicar_iva(10), 11.5)
        self.assertEqual(aplicar_iva(10, 0.2), 12)
        self.assertEqual(aplicar_iva(10, 0), 10)
        self.assertEqual(aplicar_iva(1.237, 0.15), 1.42)

    def test_iva_cero_y_errores(self):
        self.assertEqual(aplicar_iva(0), 0)
        with self.assertRaises(ValueError):
            aplicar_iva(-1)
        with self.assertRaises(ValueError):
            aplicar_iva(1, -0.1)
