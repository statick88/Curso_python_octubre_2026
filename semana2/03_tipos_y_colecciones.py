# Booleanos: valores que representan verdadero o falso.
es_mayor_de_edad = False
esta_disponible = True

# Números enteros y decimales.
edad = 35
peso = 95.8
# numero_complejo = 2j

# print(type(numero_complejo))

# Listas: colecciones ordenadas que pueden modificarse.
vocales = ["a", "e", "i", "o", "u"]
print(vocales)
print(type(vocales))
vocales.append("ae")
print(vocales)
vocales.remove("ae")
print(vocales)

datos_personales = ["Diego", 38, 95.6]
print(datos_personales)
print(datos_personales[1])

# Tuplas: colecciones ordenadas que no se modifican.
datos_contacto = ("Diego", "Loja", "0980192790")
# datos_contacto.remove("Diego")  # Fallaría: las tuplas no tienen remove.
print(datos_contacto)

# Diccionarios: relacionan una clave con un valor.
datos_usuario = {
    "nombre": "Diego",
    "telefono": "0980192790",
    "ciudad": "Loja",
}
print(datos_usuario)
# print(datos_usuario.clear())
datos_usuario.pop("ciudad")
print(datos_usuario)

# Los conjuntos eliminan valores repetidos.
print(vocales)
print(type(vocales))
vocales.append("a")
print(vocales)
conjunto_vocales = set(vocales)
print(conjunto_vocales)
print(type(conjunto_vocales))

# Elegimos comillas externas distintas para incluir comillas dentro de una cadena.
print("esta 'palabra' esta entre comillas")
print('esta "palabra" esta entre comillas')
