"""Ejemplo resuelto de proyecto independiente de registro de lecturas JSON."""

import json
from pathlib import Path

_ESTADOS_VALIDOS = {"pendiente", "leido"}


def cargar_lecturas(path):
    """Carga una lista JSON válida de lecturas sin modificar el archivo origen."""
    with Path(path).open("r", encoding="utf-8") as archivo:
        try:
            registros = json.load(archivo)
        except json.JSONDecodeError as error:
            raise ValueError("el archivo debe contener JSON válido") from error

    if not isinstance(registros, list):
        raise ValueError("las lecturas deben ser una lista")
    for registro in registros:
        if (
            not isinstance(registro, dict)
            or set(registro) != {"titulo", "estado"}
            or not isinstance(registro["titulo"], str)
            or not registro["titulo"]
            or not isinstance(registro["estado"], str)
            or registro["estado"] not in _ESTADOS_VALIDOS
        ):
            raise ValueError("cada lectura debe tener título y estado válidos")
    return registros


def resumir_por_estado(items):
    """Cuenta lecturas pendientes y leídas sin modificar los registros recibidos."""
    resumen = {"pendiente": 0, "leido": 0}
    for item in items:
        resumen[item["estado"]] += 1
    return resumen


def guardar_reporte(path, resumen):
    """Crea un JSON de resumen nuevo y rechaza sobrescribir uno existente."""
    destino = Path(path)
    if destino.exists():
        raise FileExistsError(destino)
    with destino.open("x", encoding="utf-8") as archivo:
        json.dump(resumen, archivo, ensure_ascii=False)
