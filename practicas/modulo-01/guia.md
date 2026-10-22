# M1 · ¡Hola, equipo! Tu tarjeta de presentación

> **Rama `solucion`:** el artefacto está resuelto y sus pruebas deben pasar sin modificar al evaluador docente. El enunciado original de `main` se conserva debajo para comparar el problema con la respuesta.

Construye una interacción breve que solicita dos datos y muestra una oración exacta.

## Objetivo y requisitos previos

Usar `input()`, variables y `print()` con f-strings. Revisa las lecciones oficiales de [variables](https://statick88.github.io/Course_of_python/content/modulo-01/04-variables.html) e [entrada y salida](https://statick88.github.io/Course_of_python/content/modulo-01/06-input-output.html). Necesitas Python 3 y un terminal.

## Antes del laboratorio

1. ¿Qué valor entrega `input()`?
2. ¿Qué diferencia hay entre mostrar un texto y devolverlo?
3. Predice el resultado para nombre `Ana` y ciudad `Quito`.

## Durante el laboratorio

Edita **solo** `practicas/modulo-01/m01_tarjeta_presentacion.py`. Completa `presentarse()` con una lectura para cada dato, en este orden y con estos mensajes exactos: `Nombre: ` y `Ciudad: `. Para Ana/Quito debe aparecer:

```text
Hola, soy Ana y vivo en Quito.
```

No agregues ciclos, reintentos ni validación todavía. Conserva el texto válido tal como lo escribe la persona, incluidos sus espacios exteriores. Las pruebas pertenecen al docente.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s practicas/modulo-01 -p 'test_m01_tarjeta_presentacion.py' -v
```

**Checkpoint:** al inicio el test queda en RED por una aserción de comportamiento. Cuando completes la función queda en GREEN: verifica orden de llamadas, mensajes, salida estándar, salida de error y retorno `None`.

## Después del laboratorio

Registra qué falló y qué cambiaste. En la defensa oral ejecuta la función y explica el orden de las dos llamadas a `input()`. Añade dos ejemplos propios válidos y explica por qué no se valida texto vacío en esta etapa.

## Rúbrica (100 puntos)

| Criterio | Puntos |
| --- | ---: |
| Lecturas y mensajes exactos | 30 |
| Tarjeta con formato exacto | 25 |
| Sin salida de error ni retorno inventado | 15 |
| Registro y ejemplos propios | 10 |
| Defensa oral del proceso | 20 |

La disponibilidad de esta práctica no prueba que el tema se haya enseñado; la comprobación docente y la explicación oral son obligatorias.
