"""Solución comentada: CSV validado a un reporte JSON nuevo."""

import csv
import json
from pathlib import Path


def exportar_inventario(origen_csv, destino_json):
    """Valida todo el inventario antes de crear una salida UTF-8 exclusiva."""
    destino = Path(destino_json)
    if destino.exists():
        raise FileExistsError(destino)

    registros = []
    with Path(origen_csv).open(encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo, strict=True)
        try:
            if lector.fieldnames != ["nombre", "cantidad"]:
                raise ValueError("el encabezado debe ser nombre,cantidad")
            for fila in lector:
                if set(fila) != {"nombre", "cantidad"}:
                    raise ValueError("cada fila debe contener dos columnas")
                nombre = fila["nombre"]
                if not isinstance(nombre, str) or not nombre.strip():
                    raise ValueError("nombre debe ser un texto no vacío")
                texto = fila["cantidad"]
                if texto is None:
                    raise ValueError("falta la cantidad")
                cantidad = int(texto)
                if cantidad < 0:
                    raise ValueError("cantidad debe ser un entero no negativo")
                registros.append({"nombre": nombre, "cantidad": cantidad})
        except csv.Error as error:
            raise ValueError("el CSV está malformado") from error

    # Serializar antes de abrir evita crear una salida al rechazar datos.
    contenido = json.dumps(registros, ensure_ascii=False, indent=2)
    # El modo x también protege si otro proceso creó el destino entretanto.
    with destino.open("x", encoding="utf-8") as archivo:
        archivo.write(contenido)
    return len(registros)
