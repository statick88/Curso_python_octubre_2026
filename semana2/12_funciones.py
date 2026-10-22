# Funciones: bloques con nombre que reciben datos y devuelven un resultado.
#
# Una función se define con `def`, recibe parámetros entre paréntesis y
# entrega su resultado con `return`. Este archivo contrasta las dos formas
# de comunicar un resultado, que es justo lo que evalúa la práctica ABP.
#
# Ejecución: python3 semana2/12_funciones.py


# 1. Función que SOLO imprime: ejecuta su cuerpo y no devuelve nada.
#    Quien la llama recibe None. Sirve para mostrar mensajes en pantalla.
def saludo(nombre):
    """Muestra un saludo en la consola."""
    print("Hola", nombre)


saludo("Juan")
saludo("Margarita")


# 2. Función que RETORNA: calcula un valor y lo entrega a quien la llamó.
#    Aquí no hay print: el resultado viaja de vuelta al punto de la llamada.
def suma(num1, num2):
    """Devuelve la suma de dos números."""
    return num1 + num2


resultado = suma(1, 2)
print("La suma es:", resultado)

# La diferencia se nota cuando necesitas el dato para seguir trabajando:
# con `print` solo tendrías texto en pantalla; con `return` tienes el número
# y puedes operar con él.
print("El doble de la suma es:", suma(1, 2) * 2)


# 3. `return` también sirve para salir antes de tiempo: en cuanto se ejecuta,
#    la función termina y entrega ese valor.
def es_par(numero):
    """Devuelve True si el número es par y False si no."""
    if numero % 2 != 0:
        return False
    return True


print("¿4 es par?", es_par(4))
print("¿5 es par?", es_par(5))
