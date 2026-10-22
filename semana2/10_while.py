# Ciclo while: repetir mientras una condición siga siendo verdadera.
#
# El `while` comprueba su condición ANTES de cada vuelta. Si es verdadera,
# ejecuta el bloque indentado y vuelve a comprobarla; cuando se vuelve falsa,
# sale del ciclo. La condición se evalúa al menos una vez.
#
# Ejecución: python3 semana2/10_while.py

# El contador hace de condición de control: mientras sea menor que 5, seguimos.
contador = 0

while contador < 5:
    contador += 1

    # `continue` salta el resto de esta vuelta y vuelve a comprobar la condición.
    # Aquí tiene un efecto visible: el turno 3 nunca llega al print de abajo.
    if contador == 3:
        print(f"Turno {contador}: saltamos el resto de la vuelta")
        continue

    print(f"Turno {contador}: atendido")

# Fuera del while: el bloque indentado terminó y el contador quedó en 5.
print(f"El contador terminó en {contador}")


# `break` termina el ciclo por completo, sin volver a comprobar la condición.
# Es la forma de salir de un `while True` cuando ya se cumplió lo que buscábamos.
print("--- break ---")
intentos = 0

while True:
    intentos += 1
    print(f"Intento {intentos}")

    if intentos == 3:
        print("Se alcanzó el máximo de intentos")
        break  # Salimos del ciclo sin comprobar la condición otra vez.
