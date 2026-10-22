"""Solución comentada: conversiones y formato de un presupuesto de viaje."""


def calcular_costo(distancia_texto, tarifa_texto):
    """Convierte textos finitos no negativos y devuelve el costo redondeado."""
    distancia = float(distancia_texto)
    tarifa = float(tarifa_texto)
    return round(distancia * tarifa, 2)


def normalizar_destino(destino):
    """Elimina espacios exteriores y aplica una mayúscula inicial."""
    return destino.strip().capitalize()


def formatear_presupuesto(destino, costo):
    """Reutiliza la normalización y muestra exactamente dos decimales."""
    nombre = normalizar_destino(destino)
    return f"Viaje a {nombre}: ${costo:.2f}"
