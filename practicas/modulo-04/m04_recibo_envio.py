"""Solución comentada: costo y recibo de un envío."""


def calcular_envio(peso, tarifa=3):
    """Usa la tarifa explícita o, si se omite, la tarifa por defecto."""
    return round(peso * tarifa, 2)


def crear_recibo(destino, peso, tarifa=3):
    """Reutiliza el cálculo y devuelve el texto, sin imprimirlo."""
    costo = calcular_envio(peso, tarifa)
    return f"Envío a {destino}: ${costo:.2f}"
