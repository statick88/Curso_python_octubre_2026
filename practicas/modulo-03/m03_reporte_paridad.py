"""Ejemplo resuelto de reportes de paridad para intervalos inclusivos."""


def reporte_paridad(inicio, fin):
    """Devuelve una línea por entero del intervalo válido, incluidos sus límites."""
    reporte = ""
    for numero in range(inicio, fin + 1):
        tipo = "par" if numero % 2 == 0 else "impar"
        reporte += f"{numero}: {tipo}\n"
    return reporte


def contar_pares(inicio, fin):
    """Cuenta con ``while`` los enteros pares de un intervalo inclusivo válido."""
    cantidad = 0
    numero = inicio
    while numero <= fin:
        if numero % 2 == 0:
            cantidad += 1
        numero += 1
    return cantidad
