"""Solución comentada: reutilizar el catálogo de un paquete."""

from .catalogo import SALUDOS

_catalogo_disponible = SALUDOS


def construir_saludo(nombre, momento):
    """Consulta el momento válido sin duplicar ni cambiar el catálogo."""
    saludo = SALUDOS[momento]
    return f"{saludo}, {nombre}."
