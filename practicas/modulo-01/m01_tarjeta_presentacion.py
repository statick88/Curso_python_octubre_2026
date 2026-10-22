"""Solución comentada: tarjeta de presentación interactiva del módulo 1."""


def presentarse():
    """Lee una vez cada texto válido, lo conserva y muestra la tarjeta."""
    # 1. input elimina el salto de línea, pero no los espacios del texto válido.
    nombre = input("Nombre: ")
    ciudad = input("Ciudad: ")
    # 2. print muestra la tarjeta y añade su único salto de línea final.
    print(f"Hola, soy {nombre} y vivo en {ciudad}.")
    # 3. Sin return explícito, la función termina devolviendo None.
