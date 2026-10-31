"""Ejemplo resuelto de la práctica ABP M05: organización de una maleta."""


def peso_total(pesos):
    """Devuelve la suma de pesos sin modificar la colección recibida."""
    return sum(pesos)


def seleccionar_livianos(pesos, limite):
    """Devuelve una lista nueva con pesos menores o iguales al límite."""
    return [peso for peso in pesos if peso <= limite]


def invertir_itinerario(paradas):
    """Devuelve una lista nueva con las paradas en orden inverso."""
    return list(reversed(paradas))
