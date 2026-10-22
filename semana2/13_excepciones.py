# Manejo de errores: try, except y finally.
#
# Cuando una instrucción puede fallar (por ejemplo, `float("abc")`), Python
# lanza una excepción y detiene el programa. Con `try`/`except` se captura
# esa excepción y se sigue adelante. `finally` se ejecuta siempre, haya error
# o no, así que sirve para la limpieza que no puede quedar a medias.
#
# Ejecución: python3 semana2/13_excepciones.py

# El bucle se repite hasta conseguir un número válido: `break` sale de él
# en cuanto `input` entrega algo convertible a float.
while True:
    try:
        x = float(input("Por favor ingrese un numero: "))
        break  # Salimos del while porque ya tenemos el dato.
    except ValueError:
        # Solo se ejecuta si lo de arriba lanzó ValueError, es decir, si
        # `float` no pudo convertir lo que escribió el usuario.
        print("Ups, no era válido, intenta de nuevo")
    finally:
        # Se ejecuta en cada vuelta, tanto si hubo error como si no.
        print("Todo listo, ok")

# Al salir del bucle, `x` ya contiene el número convertido a float.
print("El numero ingresado es:", x)
