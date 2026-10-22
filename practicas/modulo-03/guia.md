# M3 · Detectives de números: pares e impares

Genera un reporte y un conteo sobre intervalos enteros inclusivos.

## Objetivo y requisitos previos

Aplicar `if`, resto `%`, `for`, `range` y `while`. Consulta las lecciones oficiales de [if/else](https://statick88.github.io/Course_of_python/content/modulo-03/01-if-else.html), [for](https://statick88.github.io/Course_of_python/content/modulo-03/03-for-loop.html) y [while](https://statick88.github.io/Course_of_python/content/modulo-03/04-while-loop.html). Necesitas Python 3.

## Antes del laboratorio

1. ¿Cómo reconoces un número par con `%`?
2. ¿Qué significa que un intervalo incluya los dos límites?
3. Predice cuántos pares hay de -2 a 2.

## Durante el laboratorio

Edita **solo** `practicas/modulo-03/m03_reporte_paridad.py`. Los argumentos son enteros y cumplen `inicio <= fin`; pueden ser negativos o cero. `reporte_paridad(2, 3)` debe devolver exactamente:

```text
2: par
3: impar
```

Cada línea termina en salto de línea. `contar_pares(inicio, fin)` usa `while` y cuenta el mismo intervalo sin imprimir.

| Llamada | Resultado |
| --- | --- |
| `reporte_paridad(-1, 1)` | `'-1: impar\n0: par\n1: impar\n'` |
| `contar_pares(-2, 2)` | `3` |
| `contar_pares(0, 0)` | `1` |
| `reporte_paridad(-3, -3)` | `'-3: impar\n'` |
| `contar_pares(-3, -3)` | `0` |

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s practicas/modulo-03 -p 'test_m03_reporte_paridad.py' -v
```

**Checkpoint:** en RED inicial los retornos provisionales causan aserciones, no errores de importación. En GREEN se validan ejemplos, límites negativos, cero, intervalo de un elemento, último límite y ausencia de salida.

## Después del laboratorio

Entrega el archivo y un registro de pruebas. En la defensa oral explica por qué el límite final se incluye y muestra el `while` de `contar_pares`. Añade dos intervalos propios, uno negativo y uno de un solo número.

## Rúbrica (100 puntos)

| Criterio | Puntos |
| --- | ---: |
| Reporte y formato exacto | 30 |
| Inclusión de límites | 25 |
| Conteo con `while` | 20 |
| Registro y ejemplos propios | 10 |
| Defensa oral | 15 |

No modifiques las pruebas docentes. Esta práctica es focalizada y no cubre todas las características de control de flujo.
