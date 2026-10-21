"""Esqueleto del proyecto ABP: puesto de snacks de la feria.

Completa cada función siguiendo sus comentarios numerados y sus docstrings.
No agregues print(), input(), archivos ni clases: las pruebas llamarán las funciones.
"""


def etiqueta_pedido(evento, producto, cantidad):
    """Construye la etiqueta de un pedido válido.

    Recibe evento y producto como cadenas no vacías tal como se proporcionan,
    y cantidad como entero mayor o igual que cero. Devuelve una cadena con el
    formato exacto ``evento | cantidad x producto``.

    Ejemplos:
    - etiqueta_pedido('Feria', 'Jugo', 3) devuelve 'Feria | 3 x Jugo'.
    - etiqueta_pedido('Patio', 'Pan', 0) devuelve 'Patio | 0 x Pan'.
    """
    # TODO 1: Une los tres datos en una sola cadena con el formato indicado.
    # TODO 2: Puedes usar concatenación o una f-string; no imprimas el resultado.
    # TODO 3: Completa este return provisional con tu resultado.
    return


def calcular_total(precio_unitario, cantidad):
    """Calcula el costo de un pedido válido y lo redondea a dos decimales.

    Recibe precio_unitario como int o float finito mayor o igual que cero, y
    cantidad como entero mayor o igual que cero. Devuelve el total redondeado
    a dos decimales.

    Ejemplos:
    - calcular_total(2.5, 3) devuelve 7.5.
    - calcular_total(1.235, 3) devuelve 3.71.
    - calcular_total(4, 0) devuelve 0.0.
    - calcular_total(0, 8) devuelve 0.0.

    Pista sobre la herramienta: ``round(1.236, 2)`` produce ``1.24``.
    """
    # TODO 1: Decide qué operación representa el costo de varias unidades.
    # TODO 2: Aplica round al resultado para conservar dos decimales.
    # TODO 3: Completa este return provisional con tu valor; no lo imprimas.
    return


def reporte_turnos(turnos, stock):
    """Genera el reporte de atención de turnos válidos.

    Recibe turnos y stock como enteros mayores o iguales que cero. Devuelve
    una cadena con una línea por cada turno desde 1 hasta turnos: las primeras
    ``stock`` líneas dicen ``Turno N: atendido`` y las restantes dicen
    ``Turno N: sin stock``. Cada línea termina en ``\n``. Si turnos es 0,
    devuelve la cadena vacía.

    Ejemplo:
    - reporte_turnos(4, 2) devuelve
      'Turno 1: atendido\nTurno 2: atendido\nTurno 3: sin stock\n'
      'Turno 4: sin stock\n'.
    """
    # TODO 1: Crea una cadena acumuladora inicialmente vacía.
    # TODO 2: Recorre con for y range los turnos, incluyendo el último turno.
    # TODO 3: Con if decide si el turno actual todavía tiene stock.
    # TODO 4: Agrega una línea al acumulador en cada vuelta, con su salto de línea.
    # TODO 5: Completa este return provisional con el acumulador.
    # No uses print(), input() ni archivos.
    return
