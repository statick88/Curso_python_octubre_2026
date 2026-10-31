"""POO: Programación orientada a objetos mediante un monstruo."""


class Monster:
    """Representa un monstruo con nombre y categoría."""

    def __init__(self, nombre, categoria):
        """Guarda los datos descriptivos del monstruo."""
        self.nombre = nombre
        self.categoria = categoria

    def myFunc(self):
        """Muestra el nombre del monstruo mediante un método de instancia."""
        print("Hey, yo soy " + self.nombre)


# Instancia de clase.
mounstrito = Monster("Sullivan", "asustador")
mounstrito.myFunc()
