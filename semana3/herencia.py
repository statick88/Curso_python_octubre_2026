"""Ejemplo de herencia múltiple con un perro que también es mamífero."""


class Animal:
    """Define los datos comunes de un animal."""

    def __init__(self, nombre, edad):
        """Guarda el nombre y la edad del animal."""
        self.nombre = nombre
        self.edad = edad


class Mamifero:
    """Base didáctica que identifica a los animales mamíferos."""

    pass


class Perro(Animal, Mamifero):
    """Especializa Animal con el comportamiento de ladrar."""

    def __init__(self, nombre, edad):
        """Inicializa un perro usando los datos heredados de Animal."""
        super().__init__(nombre, edad)

    def ladrar(self):
        """Muestra el sonido característico del perro."""
        print(f"{self.nombre} ladra fuerte")


perro = Perro("Firulais", 7)
perro.ladrar()
print(perro.edad)
