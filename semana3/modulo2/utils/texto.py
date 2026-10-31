# utils/texto.py
def limpiar_texto(texto):
    """Elimina espacios extra y convierte a minúsculas."""
    return " ".join(texto.lower().split())

def contar_palabras(texto):
    """Cuenta cuántas palabras tiene un texto."""
    return len(texto.split())