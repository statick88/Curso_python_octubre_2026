"""Formato resuelto de saludos para la práctica M08."""

from .catalogo import SALUDOS

# Conserva el catálogo visible para consultar la dependencia interna del paquete.
_catalogo_disponible = SALUDOS


def construir_saludo(nombre, momento):
    """Devuelve el saludo del catálogo para un nombre y momento válidos."""
    return f"{SALUDOS[momento]}, {nombre}."
