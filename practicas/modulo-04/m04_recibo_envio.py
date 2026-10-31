"""Ejemplo resuelto de la práctica ABP M04: recibo de envío."""


def calcular_envio(peso, tarifa=3):
    """Devuelve el costo de envío válido, redondeado a dos decimales."""
    return round(peso * tarifa, 2)


def crear_recibo(destino, peso, tarifa=3):
    """Devuelve el recibo con el costo calculado y formato monetario exacto."""
    costo = calcular_envio(peso, tarifa)
    return f"Envío a {destino}: ${costo:.2f}"
