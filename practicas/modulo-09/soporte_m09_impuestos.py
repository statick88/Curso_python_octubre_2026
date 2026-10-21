"""Funciones docentes que son el sujeto de prueba de la práctica M09."""

import math


def _validar_no_negativo(valor):
    if (
        not isinstance(valor, (int, float))
        or isinstance(valor, bool)
        or not math.isfinite(valor)
        or valor < 0
    ):
        raise ValueError("se espera un número finito no negativo")


def calcular_subtotal(precio, cantidad):
    """Devuelve precio por cantidad redondeado a dos decimales."""
    _validar_no_negativo(precio)
    if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad < 0:
        raise ValueError("cantidad debe ser un entero no negativo")
    return round(precio * cantidad, 2)


def aplicar_iva(monto, tasa=0.15):
    """Aplica una tasa no negativa y redondea el resultado a dos decimales."""
    _validar_no_negativo(monto)
    _validar_no_negativo(tasa)
    return round(monto * (1 + tasa), 2)
