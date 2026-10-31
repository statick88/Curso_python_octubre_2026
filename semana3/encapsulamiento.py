"""Ejemplo de encapsulamiento mediante un atributo privado."""


class Computer:
    """Representa un equipo cuyo precio se modifica mediante un método público."""

    def __init__(self):
        """Inicializa el precio de venta protegido del equipo."""
        self.__maxprice = 900

    def sell(self):
        """Muestra el precio de venta configurado actualmente."""
        print(f"El precio de venta es: {self.__maxprice}")

    def set_maxprice(self, price):
        """Actualiza el precio de venta mediante la interfaz pública."""
        self.__maxprice = price


c = Computer()
c.sell()  # El precio de venta es: 900.
# El nombre con doble guion bajo no modifica el atributo encapsulado.
c.__maxprice = 1000
c.sell()

# El método público sí modifica el valor protegido.
c.set_maxprice(1000)
c.sell()  # El precio de venta es: 1000.
