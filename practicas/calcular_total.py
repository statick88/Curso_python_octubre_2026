"""
Esqueleto de la etapa 2: total de pedido de la feria.

Completa la función siguiendo sus comentarios numerados. No agregues print(),
input(), archivos ni clases: las pruebas llamarán la función.
"""


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
    # 1. El costo de varias unidades es el precio de una unidad multiplicado
    #    por cuantas unidades se compran.
    total = precio_unitario * cantidad

    # 2. round(total, 2) deja el total con dos decimales.
    #    El float() no sobra: si el precio y la cantidad son int, el producto
    #    también lo es y round(4 * 0, 2) devolvería 0 (int), no 0.0 como
    #    documenta el enunciado.
    total = round(float(total), 2)

    # 3. Se devuelve el total con return; con print() el resultado saldría
    #    fuera de la función y el test lo detectaría como fallo.
    return total
