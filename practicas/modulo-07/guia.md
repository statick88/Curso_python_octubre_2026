# M7 · Misión inventario: del CSV al JSON

Convierte un CSV sintético de inventario en un JSON nuevo y protegido contra sobrescrituras.

## Objetivo y requisito

- Aplicar lectura, validación y escritura UTF-8 con `csv` y `json`.
- Revisa antes [manejo CSV](https://statick88.github.io/Course_of_python/content/modulo-07/04-manejo-csv.html), [JSON](https://statick88.github.io/Course_of_python/content/modulo-07/05-manejo-json.html) y [pathlib](https://statick88.github.io/Course_of_python/content/modulo-07/06-pathlib.html).
- Los errores de archivos son un requisito de lectura de esta práctica; no prueban que un módulo posterior ya se haya impartido.

## Ruta rápida

1. Edita solo `practicas/modulo-07/m07_exportar_inventario.py`; `test_m07_exportar_inventario.py` es del docente.
2. Implementa `exportar_inventario(origen_csv, destino_json)`.
3. Desde la raíz del repositorio ejecuta `python3 -m unittest discover -s practicas/modulo-07 -p 'test_m07_exportar_inventario.py' -v`.

El CSV tiene exactamente `nombre,cantidad`: nombre no vacío y cantidad entera mayor o igual que cero. Devuelve el número de filas y conserva el orden; un archivo con solo encabezado genera `[]` y devuelve `0`. Un origen ausente genera `FileNotFoundError`, una fila o encabezado inválido `ValueError` y un destino existente `FileExistsError`. No crees salida al rechazar datos ni modifiques origen o destino existente.

## Pre-lab

Explica en tu bitácora la diferencia entre abrir para leer y crear un archivo nuevo. Crea únicamente fixtures sintéticos en un directorio temporal.

## En laboratorio

Prueba primero `nombre,cantidad\ncuaderno,2\nlapiz,0\n`; el JSON esperado contiene cantidades enteras. **Checkpoint:** muestra al docente el comando verde y un caso inválido que no deja reporte.

## Post-lab

Registra intento, error observado y corrección. En defensa oral explica por qué comprobarías el destino antes de escribir. Añade un ejemplo propio sintético con tres artículos y guarda la evidencia de su resultado.

## Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| CSV, orden y JSON correctos | 35 |
| Validación y errores exactos | 25 |
| Protección de archivos y no mutación | 20 |
| Bitácora, checkpoint y defensa oral | 10 |
| Ejemplo propio sintético | 10 |
