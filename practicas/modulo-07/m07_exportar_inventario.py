"""Ejemplo resuelto de exportación segura de inventario CSV a JSON."""

import csv
import json
from pathlib import Path


def exportar_inventario(origen_csv, destino_json):
    """Valida un CSV y crea un JSON nuevo, devolviendo el número de filas.

    No crea ni modifica el destino cuando el origen o alguna fila es inválida,
    y rechaza explícitamente sobrescribir un reporte existente.
    """
    origen = Path(origen_csv)
    destino = Path(destino_json)
    inventario = []

    with origen.open("r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        if lector.fieldnames != ["nombre", "cantidad"]:
            raise ValueError("el CSV debe tener encabezado nombre,cantidad")
        for fila in lector:
            nombre = fila.get("nombre")
            cantidad_texto = fila.get("cantidad")
            if set(fila) != {"nombre", "cantidad"} or not nombre or cantidad_texto is None:
                raise ValueError("cada fila debe incluir nombre y cantidad")
            try:
                cantidad = int(cantidad_texto)
            except ValueError as error:
                raise ValueError("cantidad debe ser un entero no negativo") from error
            if cantidad < 0:
                raise ValueError("cantidad debe ser un entero no negativo")
            inventario.append({"nombre": nombre, "cantidad": cantidad})

    if destino.exists():
        raise FileExistsError(destino)
    with destino.open("x", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, ensure_ascii=False)
    return len(inventario)
