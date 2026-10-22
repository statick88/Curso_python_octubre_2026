"""Esqueleto de la etapa 1: etiqueta de pedido de la feria.

Completa la función siguiendo sus comentarios numerados. No agregues print(),
input(), archivos ni clases: las pruebas llamarán la función.
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
    # 1. La f-string arma la cadena en un solo paso: entre llaves va la
    #    variable y fuera el texto fijo. cantidad llega como int, pero la
    #    f-string la convierte a texto sola, así que no hace falta str().
    # 2. Los separadores van CON espacios: " | " y " x ". Sin ellos la salida
    #    sería "Feria|3xJugo" y assertEqual fallaría.
    #    Con concatenación sería: evento + " | " + str(cantidad) + " x " + producto.
    # 3. Se devuelve, no se imprime: return entrega el valor a quien llama la
    #    función; con print() el valor saldría por pantalla y la función
    #    devolvería None, que es justo lo que el test comprueba.
    salida1 = f"{evento} | {cantidad} x {producto}"
    return salida1
