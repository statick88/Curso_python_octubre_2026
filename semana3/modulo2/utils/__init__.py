# utils/__init__.py
# Este archivo se ejecuta cuando alguien hace: import utils

from .texto import limpiar_texto, contar_palabras
from .numeros import formatear_moneda, calcular_promedio
#from .archivos import leer_archivo, guardar_archivo

__all__ = [
    "limpiar_texto",
    "contar_palabras",
    "formatear_moneda",
    "calcular_promedio",
    #"leer_archivo",
    #"guardar_archivo",
]