# M0 · Misión excursión: planifica la aventura

Planifica una salida escolar antes de programar. El resultado es un documento razonado, no código Python.

## Objetivo y requisitos previos

Organizar un problema en entradas, salidas y subproblemas, y comparar alternativas. Consulta las lecciones oficiales [descomposición](https://statick88.github.io/Course_of_python/content/modulo-00/02-descomposicion.html) y [pseudocódigo](https://statick88.github.io/Course_of_python/content/modulo-00/04-pseudocodigo.html). Solo necesitas un editor de texto.

## Antes del laboratorio

1. ¿Qué dato cambiaría más la viabilidad de una salida escolar?
2. ¿Por qué dividir una salida en subproblemas puede evitar olvidos?
3. Escribe dos alternativas posibles para el transporte o la organización.

## Durante el laboratorio

Edita **solo** `practicas/modulo-00/m00_planificador.md`: reemplaza todos los marcadores visibles y conserva los encabezados. Escribe al menos cuatro subproblemas no vacíos y dos alternativas no vacías usando las listas visibles de la plantilla. No hay una respuesta única ni la prueba evalúa tu razonamiento.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s practicas/modulo-00 -p 'test_m00_planificador.py' -v
```

**Checkpoint:** inicialmente varias pruebas fallan porque el material contiene marcadores y listas sin completar. Tras completar tu plan, las cuatro pruebas estructurales quedan en `OK`. Comprueban estructura y contenido visible, no una respuesta única; la revisión docente oral decide si la propuesta es factible.

## Después del laboratorio

Entrega el plan y un registro del proceso: decisiones, cambios y dudas. En la defensa oral explica la factibilidad, tus subproblemas y por qué elegiste una alternativa. Añade dos ejemplos propios de decisiones que cambiarías si cambia el presupuesto o el grupo.

## Rúbrica (100 puntos)

| Criterio | Puntos |
| --- | ---: |
| Secciones y marcadores completados | 20 |
| Descomposición en subproblemas | 25 |
| Alternativas comparadas | 20 |
| Factibilidad y justificación oral | 25 |
| Registro y ejemplos propios | 10 |

Las pruebas son docentes; no las edites. Esta práctica disponible no demuestra por sí misma que el contenido ya fue enseñado.
