"""Solución comentada: sumar, seleccionar y copiar colecciones."""


def peso_total(pesos):
    """Suma los pesos sin cambiar la colección recibida."""
    return sum(pesos)


def seleccionar_livianos(pesos, limite):
    """Crea una lista nueva y conserva el orden de los pesos admitidos."""
    seleccionados = []
    for peso in pesos:
        if peso <= limite:
            seleccionados.append(peso)
    # Incluso si todos caben, el resultado no comparte la lista de entrada.
    return seleccionados


def invertir_itinerario(paradas):
    """Invierte la tupla mediante slicing y devuelve una lista nueva."""
    return list(paradas[::-1])
