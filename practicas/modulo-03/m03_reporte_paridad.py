"""Solución comentada: intervalos inclusivos con for y while."""


def reporte_paridad(inicio, fin):
    """Acumula una línea por entero, incluidos ambos extremos."""
    reporte = ""
    # range excluye su segundo argumento: fin + 1 incluye el último entero.
    for numero in range(inicio, fin + 1):
        if numero % 2 == 0:
            paridad = "par"
        else:
            paridad = "impar"
        reporte += f"{numero}: {paridad}\n"
    return reporte


def contar_pares(inicio, fin):
    """Recorre el mismo intervalo mediante while y cuenta sus pares."""
    cantidad = 0
    numero = inicio
    while numero <= fin:
        if numero % 2 == 0:
            cantidad += 1
        # Avanzar siempre evita que el ciclo quede detenido en un impar.
        numero += 1
    return cantidad
