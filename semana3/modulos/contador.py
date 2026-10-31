# contador.py — Módulo con estado

contador_llamadas = 0  # <1> — variable del módulo

def registrar_accion(accion):
    """Registra una acción y cuenta cuántas se han hecho."""
    global contador_llamadas
    contador_llamadas += 1
    print(f"[{contador_llamadas}] {accion}")

def obtener_total():
    """Devuelve el total de acciones registradas."""
    return contador_llamadas