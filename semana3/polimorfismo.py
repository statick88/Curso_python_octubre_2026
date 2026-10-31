"""Ejemplo de polimorfismo con sonidos de distintos animales."""


class Animal:
    """Base didáctica para animales que pueden emitir un sonido."""

    def hablar(self):
        """Define el punto de extensión para el sonido de cada animal."""
        pass


class Perro(Animal):
    """Animal que emite un ladrido."""

    def hablar(self):
        """Muestra el sonido del perro."""
        print("Guau")


class Gato(Animal):
    """Animal que emite un maullido."""

    def hablar(self):
        """Muestra el sonido del gato."""
        print("Miau")


class Vaca(Animal):
    """Animal que emite un mugido."""

    def hablar(self):
        """Muestra el sonido de la vaca."""
        print("Muu")


animales = [Perro(), Gato(), Vaca()]

for animal in animales:
    animal.hablar()
