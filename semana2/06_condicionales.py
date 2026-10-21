# if, elif y else permiten elegir una acción según una condición.
edad = 50
if edad >= 18 and edad < 50:
    print("Es mayor de edad")
elif edad >= 50:
    print("Es adulto")
else:
    print("Es menor de edad")

print("=" * 96)

numero = 5
# Esta expresión condicional imprime uno de dos mensajes en una sola línea.
print("Mayor que 2") if numero > 2 else print("Menor o igual a 2")

# La misma decisión se escribe aquí con una estructura if/else convencional.
if numero > 2:
    print("Mayor que 2")
else:
    print("Menor o igual a 2")
