"""Ejemplo resuelto de la práctica ABP M06: votación de un club."""


def contar_votos(votos):
    """Devuelve el número de apariciones de cada candidato sin mutar los votos."""
    conteo = {}
    for candidato in votos:
        conteo[candidato] = conteo.get(candidato, 0) + 1
    return conteo


def candidatos_unicos(votos):
    """Devuelve un conjunto nuevo con los candidatos presentes en los votos."""
    return set(votos)


def ganador(conteo):
    """Devuelve el máximo único o ``None`` si no hay votos o existe empate."""
    if not conteo:
        return None
    mayor = max(conteo.values())
    candidatos = [nombre for nombre, votos in conteo.items() if votos == mayor]
    return candidatos[0] if len(candidatos) == 1 else None
