"""Ejemplo resuelto de la etapa 3: reporte de turnos de la feria."""


def reporte_turnos(turnos, stock):
    """Genera el reporte de atención para turnos y stock no negativos.

    Devuelve una línea terminada en ``\\n`` para cada turno de 1 a
    ``turnos``: atiende los primeros ``stock`` y marca el resto sin stock.
    Cuando ``turnos`` es cero devuelve la cadena vacía; no imprime resultados.
    """
    reporte = ""
    for turno in range(1, turnos + 1):
        estado = "atendido" if turno <= stock else "sin stock"
        reporte += f"Turno {turno}: {estado}\n"
    return reporte
