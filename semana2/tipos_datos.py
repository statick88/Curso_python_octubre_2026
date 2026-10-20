#Booleanos

is_mayor_edad = False
is_avalible = True

# Numbers

edad = 35
peso = 95.8
#a = a +2j

#print(type(a))

# Comlejos

lista = ["a", "e", "i", "o", "u"]
print(lista)
print(type(lista))
lista.append("ae")
print(lista)
lista.remove("ae")
print(lista)
lista2 = ["Diego", 38, 95.6]
print(lista2)
print(lista2[1])

# Tuplas
tupla = ("Diego", "Loja", "0980192790")
#tupla.remove("Diego")
print(tupla)

# Diccionario
dic = {
    "nombre": "Diego",
    "telefono": "0980192790",
    "ciudad": "Loja"
}
print(dic)
#print(dic.clear())
dic.pop("ciudad")
print(dic)

#set
print(lista)
print(type(lista))
lista.append("a")
print(lista)
conjunto = set(lista)
print(conjunto)
print(type(conjunto))

print('esta \'palabra\' esta entre comillas')
print("esta \"palabra\" esta entre comillas")