"""Ejemplo de una clase Perro con representación y comportamiento."""


class Perro:
    """Representa un perro mediante su nombre y edad."""

    def __init__(self, name, age):
        """Guarda el nombre y la edad del perro."""
        self.name = name
        self.age = age

    def __str__(self):
        """Devuelve una representación legible del perro."""
        return f"{self.name} de {self.age} años"

    def ladrar(self):
        """Muestra el sonido del perro en la consola."""
        print(f"{self.name} ladra fuerte")


# Instancia de clase: crear el objeto.
perro_1 = Perro("Wolf", 7)
print(perro_1)
perro_1.ladrar()
