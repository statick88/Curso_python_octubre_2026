# calculadora.py — Versión mejorada

def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta dos números."""
    return a - b

# Este bloque solo se ejecuta si corres el archivo directamente
if __name__ == "__main__":
    print("=== Calculadora ===")
    print("10 + 5 =", sumar(10, 5))
    print("10 - 5 =", restar(10, 5))
    print("Ejecutado directamente")