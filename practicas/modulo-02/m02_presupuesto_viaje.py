"""Ejemplo resuelto de funciones para un presupuesto de viaje."""


def calcular_costo(distancia_texto, tarifa_texto):
    """Convierte textos numéricos válidos y devuelve su producto redondeado."""
    return round(float(distancia_texto) * float(tarifa_texto), 2)


def normalizar_destino(destino):
    """Quita espacios exteriores y capitaliza un destino válido."""
    return destino.strip().capitalize()


def formatear_presupuesto(destino, costo):
    """Devuelve el mensaje de presupuesto con destino normalizado y dos decimales."""
    return f"Viaje a {normalizar_destino(destino)}: ${costo:.2f}"
