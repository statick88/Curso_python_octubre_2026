"""Práctica M09: escribe pruebas para las funciones de impuestos docentes."""

import unittest

from soporte_m09_impuestos import aplicar_iva, calcular_subtotal

__all__ = ["TestM09ImpuestosDelEstudiante", "aplicar_iva", "calcular_subtotal"]


class TestM09ImpuestosDelEstudiante(unittest.TestCase):
    """Sustituye cada TODO por aserciones de comportamiento público."""

    def test_subtotal_cantidad_y_redondeo(self):
        self.fail("TODO: cubre cantidad y redondeo del subtotal")

    def test_subtotal_cero_y_errores(self):
        self.fail("TODO: cubre cantidad cero y negativos separados")

    def test_iva_tasas_y_redondeo(self):
        self.fail("TODO: cubre tasa por defecto, explícita y redondeo")

    def test_iva_cero_y_errores(self):
        self.fail("TODO: cubre monto cero y negativos separados")
