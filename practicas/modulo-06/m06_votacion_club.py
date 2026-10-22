"""Solución comentada: conteo de votos, conjuntos y máximo único."""


def contar_votos(votos):
    """Acumula un voto por cada aparición de un nombre válido."""
    conteo = {}
    for nombre in votos:
        conteo[nombre] = conteo.get(nombre, 0) + 1
    return conteo


def candidatos_unicos(votos):
    """Un set elimina duplicados sin modificar la lista original."""
    return set(votos)


def ganador(conteo):
    """Devuelve el máximo único; vacío o empate producen None."""
    if not conteo:
        return None
    maximo = max(conteo.values())
    ganadores = []
    for nombre, cantidad in conteo.items():
        if cantidad == maximo:
            ganadores.append(nombre)
    if len(ganadores) == 1:
        return ganadores[0]
    return None
