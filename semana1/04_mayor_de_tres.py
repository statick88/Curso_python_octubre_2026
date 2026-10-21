def encontrar_mayor(primer_numero, segundo_numero, tercer_numero):
    """Devuelve el número mayor entre tres valores."""
    if primer_numero >= segundo_numero and primer_numero >= tercer_numero:
        mayor = primer_numero
    elif segundo_numero >= primer_numero and segundo_numero >= tercer_numero:
        mayor = segundo_numero
    else:
        mayor = tercer_numero

    return mayor


numero_mayor = encontrar_mayor(4, 100, 7)
print(numero_mayor)
