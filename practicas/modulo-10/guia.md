# M10 · Pasaporte lector: organiza tu biblioteca

> **Rama `solucion`:** el artefacto está resuelto y sus pruebas deben pasar sin modificar al evaluador docente. El enunciado original de `main` se conserva debajo para comparar el problema con la respuesta.

Construye un proyecto independiente que carga, resume y guarda un registro JSON sintético.

## Objetivo y requisito

- Integrar funciones pequeñas de lectura, resumen y escritura sin depender de prácticas anteriores.
- Revisa [planificar proyecto](https://statick88.github.io/Course_of_python/content/modulo-10/01-planificar-proyecto.html), [estructura](https://statick88.github.io/Course_of_python/content/modulo-10/02-estructura-proyecto.html) y [gestor de tareas](https://statick88.github.io/Course_of_python/content/modulo-10/03-proyecto-gestor-tareas.html).

## Ruta rápida

1. Edita `practicas/modulo-10/m10_biblioteca.py`; `test_m10_biblioteca.py` es docente.
2. Ejecuta desde la raíz: `python3 -m unittest discover -s practicas/modulo-10 -p 'test_m10_biblioteca.py' -v`.
3. Trabaja solo con archivos sintéticos temporales.

`cargar_lecturas(path)` acepta una lista JSON ordenada de registros con `titulo` no vacío y estado `pendiente` o `leido`; JSON o esquema inválido generan `ValueError` y ruta ausente `FileNotFoundError`. `resumir_por_estado(items)` devuelve siempre ambas claves desde cero sin mutar entradas. `guardar_reporte(path, resumen)` crea un JSON nuevo, devuelve `None` y rechaza sobrescritura con `FileExistsError` sin cambiar el archivo existente.

## Pre-lab

Esboza el flujo `cargar → resumir → guardar` y define qué datos deben permanecer intactos entre pasos.

## En laboratorio

Empieza con dos libros: uno pendiente y uno leído. **Checkpoint:** presenta un pipeline verde que produce `{"pendiente": 1, "leido": 1}` y un intento de sobrescritura rechazado.

## Post-lab

Registra una decisión de validación y un error corregido. En defensa oral explica por qué separar las tres funciones simplifica las pruebas. Añade un conjunto propio de tres títulos sintéticos y conserva su evidencia.

## Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| Carga y validación JSON | 30 |
| Resumen completo y no mutación | 25 |
| Reporte nuevo y protección de sobrescritura | 20 |
| Pipeline independiente | 10 |
| Bitácora, checkpoint, defensa y ejemplo | 15 |
