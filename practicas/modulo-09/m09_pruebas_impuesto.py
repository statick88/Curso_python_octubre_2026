"""Suite resuelta de la práctica M09 para las funciones docentes de impuestos."""

import unittest

from soporte_m09_impuestos import aplicar_iva, calcular_subtotal

__all__ = ["TestM09ImpuestosDelEstudiante", "aplicar_iva", "calcular_subtotal"]


class TestM09ImpuestosDelEstudiante(unittest.TestCase):
    """Comprueba resultados y contratos de error de las APIs públicas docentes."""

    def test_subtotal_cantidad_y_redondeo(self):
        """Comprueba que la cantidad participa en el subtotal y este se redondea."""
        self.assertEqual(calcular_subtotal(2.5, 3), 7.5)
        self.assertEqual(calcular_subtotal(1.235, 3), 3.71)

    def test_subtotal_cero_y_errores(self):
        """Comprueba cero y rechazos independientes para precio y cantidad negativos."""
        self.assertEqual(calcular_subtotal(4, 0), 0)
        with self.assertRaises(ValueError):
            calcular_subtotal(-1, 1)
        with self.assertRaises(ValueError):
            calcular_subtotal(1, -1)

    def test_iva_tasas_y_redondeo(self):
        """Comprueba la tasa predeterminada, una explícita y el redondeo."""
        self.assertEqual(aplicar_iva(100), 115.0)
        self.assertEqual(aplicar_iva(100, 0.12), 112.0)
        self.assertEqual(aplicar_iva(1.235), 1.42)

    def test_iva_cero_y_errores(self):
        """Comprueba monto cero y rechazos independientes para monto y tasa negativos."""
        self.assertEqual(aplicar_iva(0), 0.0)
        with self.assertRaises(ValueError):
            aplicar_iva(-1)
        with self.assertRaises(ValueError):
            aplicar_iva(1, -0.01)
