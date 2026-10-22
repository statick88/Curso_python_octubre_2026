# Ciclo for: recorrer una secuencia, un elemento por vuelta.
#
# El `for` pide un iterable (una lista, una tupla, un texto, o el resultado de
# `range(...)`) y coloca uno de sus elementos en la variable de la vuelta.
# No necesita un contador: el elemento ES el estado de cada vuelta.
#
# Ejecución: python3 semana2/11_for.py

# 1. Recorrer una lista: en cada vuelta la variable recibe un elemento.
frutas = ["kiwi", "manzana", "pera"]

for fruta in frutas:
    print(fruta)

# 2. Recorrer un texto: cada vuelta recibe un carácter.
print("--- caracteres ---")

for letra in "hola":
    print(letra)

# 3. Recorrer range(): el patrón clásico cuando lo que cuenta son los números.
#    range(1, 6) produce 1, 2, 3, 4, 5 porque el final queda excluido.
print("--- range ---")

for numero in range(1, 6):
    print(f"Número {numero}")

# 4. range() con paso: range(inicio, fin, paso) avanza de N en N.
#    Aquí 0, 2, 4, 6, 8 porque el 10 no se incluye.
print("--- range con paso ---")

for numero in range(0, 10, 2):
    print(numero)
