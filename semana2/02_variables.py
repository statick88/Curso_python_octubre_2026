# Las variables guardan valores que pueden reutilizarse o cambiarse.
# Un guion bajo inicial también es válido en el nombre de una variable.
nombre = "Diego"
apellido = "Saavedra"
edad = 38
peso = 95.8
correo_electronico = "dsaavedra@gmail.com"
valor_decimal = 2.56
_otro_decimal = 3.4
variable_de_ejemplo = "algo"

# Estos bloques de texto entre comillas triples NO ejecutan nada: son literales
# guardados en una variable descartable. Sirven para dejar escritas las
# pruebas de una idea antes de programarla.
"""print(nombre + " " + apellido)
print(edad)
print(peso)"""

"""
print(type(edad))
print(type(nombre))
print(type(peso))
"""

# Reasignar reemplaza el valor anterior de una variable.
valor_decimal = 9
resultado = valor_decimal + 5
print(resultado)


# --- Alcance: la misma variable vista desde dentro y desde fuera de una función
#
# Una función crea su propio espacio de nombres. Si dentro de ella se escribe
# un nombre que ya existe afuera, Python NO modifica el de afuera: crea una
# variable local nueva que desaparece al terminar la función.
print("-------------------------")

variable = 60


def funcion():
    # Aquí `variable` es una variable LOCAL: nace con 30 y existe solo
    # mientras dura esta función. La `variable` de afuera no se toca.
    variable = 30
    if variable < 100:
        print(variable)


print(variable)  # 60: todavía la de afuera, sin cambios.
funcion()       # Dentro se imprimió 30 (la local).
print(variable)  # 60 otra vez: la de afuera nunca cambió.

# Para modificar de verdad la variable de afuera desde dentro, se usa
# `global variable` al inicio de la función. No hace falta aquí: es la
# diferencia entre alcance local y global.
