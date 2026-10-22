"""Esqueleto de la etapa 3: reporte de turnos de la feria.

Completa la función siguiendo sus comentarios numerados. No agregues print(),
input(), archivos ni clases: las pruebas llamarán la función.
"""


def reporte_turnos(turnos, stock):
    """Genera el reporte de atención de turnos válidos.

    Recibe turnos y stock como enteros mayores o iguales que cero. Devuelve
    una cadena con una línea por cada turno desde 1 hasta turnos: las primeras
    ``stock`` líneas dicen ``Turno N: atendido`` y las restantes dicen
    ``Turno N: sin stock``. Cada línea termina en ``\\n``. Si turnos es 0,
    devuelve la cadena vacía.

    Ejemplo:
    - reporte_turnos(4, 2) devuelve
      'Turno 1: atendido\\nTurno 2: atendido\\nTurno 3: sin stock\\n'
      'Turno 4: sin stock\\n'.
    """
    # 1. El acumulador arranca vacío: si turnos es 0 el for no da ninguna
    #    vuelta y se devuelve "" tal como pide el enunciado.
    reporte = ""

    # 2. range(1, turnos + 1) recorre 1, 2, ... turnos. El +1 es necesario
    #    porque range() excluye el límite, y así el último turno también entra.
    for numero in range(1, turnos + 1):

        # 3. Los primeros stock turnos se atienden; a partir de ahí no hay
        #    stock, así que el resto de la cola queda sin atender.
        if numero <= stock:

            # 4. Cada vuelta añade su línea al acumulador, con el salto de
            #    línea "\n" al final para separar los turnos entre sí.
            reporte += f"Turno {numero}: atendido\n"
        else:
            reporte += f"Turno {numero}: sin stock\n"

    # 5. Se devuelve el acumulador completo, ya con todas las líneas.
    # No uses print(), input() ni archivos.
    return reporte
