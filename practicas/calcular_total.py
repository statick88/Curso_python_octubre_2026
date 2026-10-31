"""Ejemplo resuelto de la etapa 2: total de pedido de la feria."""


def calcular_total(precio_unitario, cantidad):
    """Calcula el total de un pedido válido y lo redondea a dos decimales.

    ``precio_unitario`` es un número finito no negativo y ``cantidad`` un
    entero no negativo. Devuelve ``0.0`` si cualquiera de los dos es cero y
    no imprime ni modifica los argumentos.
    """
    return round(precio_unitario * cantidad, 2)
