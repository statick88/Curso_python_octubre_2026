# If, elif, else
# es mayor de edad
edad = 50
if edad >= 18 and edad <50:
    print("Es mayor de edad")
elif edad >= 50:
    print("Es adulto")
else:
    print("Es menor de edad")

print("="*96)

n = 5
print("Mayor que 2") if n > 2 else print("Menor o igual a 2")

if n > 2:
    print("Mayor que 2")
else:
    print("Menor o igual a 2")