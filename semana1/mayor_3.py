def encontrar_mayor(a, b, c):
    if a >= b and a >= c:
        mayor = a
    elif b >= a and b >= c:
        mayor = b
    else:
        mayor = c
    return mayor

mayor = encontrar_mayor(4,100,7)
print(mayor)