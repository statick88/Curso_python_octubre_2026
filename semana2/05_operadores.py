# Operadores matemáticos.
import math

print(2 + 2)  # Suma.
print(2 - 2)  # Resta.
print(2 * 2)  # Multiplicación.
print(2 / 2)  # División.
print(5 // 2)  # División de piso (redondea hacia abajo).
print(5 % 2)  # Módulo o residuo.
print(5**2)  # Potenciación.
print(math.sqrt(16))  # Raíz cuadrada.

# Operadores lógicos que combinan comparaciones.
primer_valor = 9
segundo_valor = 8
tercer_valor = 10
cuarto_valor = 5
print(primer_valor > segundo_valor and tercer_valor > cuarto_valor)  # True.

primer_valor = 10
segundo_valor = 9
tercer_valor = 20
cuarto_valor = 100
print(primer_valor > segundo_valor and tercer_valor > cuarto_valor)  # False.

primer_valor = 9
segundo_valor = 2
tercer_valor = 100
cuarto_valor = 1000
print(primer_valor > segundo_valor or tercer_valor > cuarto_valor)  # True.

primer_valor = 20
segundo_valor = 18
print(math.sqrt(4) > 1 or primer_valor < segundo_valor)  # True.
print(20 / 5 > 6 or 50 / 25 > 10)  # False.

es_mayor_de_edad = True
print(es_mayor_de_edad)
print(not es_mayor_de_edad)

# print(("a") == ("e"))  # False.
