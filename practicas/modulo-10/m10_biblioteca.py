"""Solución comentada: cargar, resumir y guardar lecturas sin otros ejercicios."""

import json
from pathlib import Path


def _es_lectura_valida(item):
    """Describe el esquema de un registro, sin realizar lectura ni escritura."""
    return (
        isinstance(item, dict)
        and isinstance(item.get("titulo"), str)
        and bool(item["titulo"].strip())
        and item.get("estado") in ("pendiente", "leido")
    )


def cargar_lecturas(path):
    """Lee JSON UTF-8; un esquema inválido es un ValueError de los datos."""
    with Path(path).open(encoding="utf-8") as archivo:
        items = json.load(archivo)
    if not (
        isinstance(items, list) and all(_es_lectura_valida(item) for item in items)
    ):
        raise ValueError("el JSON no corresponde al esquema de lecturas")
    return items


def resumir_por_estado(items):
    """Cuenta una lista validada y conserva ambas claves aunque esté vacía."""
    resumen = {"pendiente": 0, "leido": 0}
    for item in items:
        resumen[item["estado"]] += 1
    return resumen


def guardar_reporte(path, resumen):
    """Serializa sin mutar y crea un archivo nuevo; nunca lo sobrescribe."""
    destino = Path(path)
    if destino.exists():
        raise FileExistsError(destino)
    contenido = json.dumps(resumen, ensure_ascii=False, indent=2)
    with destino.open("x", encoding="utf-8") as archivo:
        archivo.write(contenido)
