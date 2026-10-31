# utils/numeros.py
def formatear_moneda(cantidad, simbolo="$"):
    """Formatea un número como moneda."""
    return f"{simbolo}{cantidad:,.2f}"

def calcular_promedio(numeros):
    """Calcula el promedio de una lista de números."""
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)