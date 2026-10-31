"""Ejemplo resuelto de la etapa 1: etiqueta de pedido de la feria."""


def etiqueta_pedido(evento, producto, cantidad):
    """Construye la etiqueta de un pedido válido sin imprimirla.

    Recibe ``evento`` y ``producto`` como textos no vacíos sin alterarlos, y
    ``cantidad`` como entero no negativo. Devuelve exactamente
    ``evento | cantidad x producto``, incluso cuando la cantidad es cero.
    """
    return f"{evento} | {cantidad} x {producto}"
