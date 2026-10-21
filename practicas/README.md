# Práctica ABP: Puesto de snacks de la feria

Construirás, por etapas, las tres funciones de un puesto de snacks. El archivo
`feria_snacks.py` contiene el punto de partida: sigue los comentarios `TODO`,
ejecuta las pruebas y mejora tu código hasta que todas pasen. No hay una
solución entregada: el resultado se verifica por el comportamiento público.

**Duración estimada:** 90 minutos.

**Herramienta:** Python 3 y su biblioteca estándar; no instales paquetes ni uses `pip`.

## Objetivos

Al finalizar podrás:

- devolver resultados desde funciones con parámetros;
- construir cadenas y calcular un total redondeado;
- usar `for`, `range` e `if` para producir un reporte acumulado;
- interpretar fallos de `unittest` como retroalimentación.

## Antes de empezar

**Conocimientos usados:** funciones, parámetros y `return`; cadenas, números y
operadores; `if` y `for`/`range`. Son actividades de M1–M2 y de lo ya visto de
M3. La lectura de `input()` es anticipada, pero **no se usa** en esta práctica.

Lee, como máximo 20 minutos:

- [Módulo 1](https://statick88.github.io/Course_of_python/content/modulo-01/index.html): introducción y f-strings.
- [Módulo 2](https://statick88.github.io/Course_of_python/content/modulo-02/index.html): cadenas, números y `round`.
- [Módulo 3](https://statick88.github.io/Course_of_python/content/modulo-03/index.html): secciones `if` y `for`.

Desde la raíz del repositorio, comprueba Python y ejecuta el punto de partida:

```bash
python3 --version
python3 -m unittest discover -s practicas -p 'test_*.py' -v
```

Al comienzo las pruebas deben mostrar **FAIL** por aserciones: las funciones
tienen un `return` provisional sin valor (devuelve `None`) que debes completar. Se descubren 12 pruebas,
sin errores de importación o sintaxis ni pruebas omitidas. Algunos tests tienen
subcasos, por lo que el número de fallos puede ser mayor que 12.

Todos los comandos siguientes parten de la raíz del repositorio; no cambies de
directorio entre etapas.

## Archivos y roles

| Archivo | Rol |
| --- | --- |
| `feria_snacks.py` | Tu espacio de trabajo: completa únicamente los cuerpos de las funciones. |
| `test_feria_snacks.py` | Infraestructura docente: describe y verifica el comportamiento. No lo modifiques. |

Las clases `TestCase`, las importaciones de la biblioteca estándar y la captura
de salida pertenecen a la infraestructura docente; no requieren conocimientos
de programación orientada a objetos.

## En el laboratorio

### Etapa 1 — guiada: etiqueta del pedido

Completa `etiqueta_pedido(evento, producto, cantidad)`.

| Entrada válida | Salida exacta |
| --- | --- |
| `('Feria', 'Jugo', 3)` | `'Feria | 3 x Jugo'` |
| `('Patio', 'Pan', 0)` | `'Patio | 0 x Pan'` |

Los textos son cadenas no vacías tal como llegan; `cantidad` es un entero mayor
o igual que cero. Devuelve la cadena: no imprimas ni solicites datos.

```bash
python3 -m unittest discover -s practicas -p 'test_*.py' -k TestEtapa1Etiqueta -v
```

**Checkpoint:** las 3 pruebas de la etapa terminan en `OK`.

### Etapa 2 — independiente: total del pedido

Completa `calcular_total(precio_unitario, cantidad)`. El precio es un `int` o
`float` finito no negativo y la cantidad es un entero no negativo. Devuelve el
total redondeado a dos decimales; los valores fuera de ese contrato no forman
parte de esta actividad.

| Entrada válida | Salida esperada |
| --- | --- |
| `(2.5, 3)` | `7.5` |
| `(1.235, 3)` | `3.71` |
| `(4, 0)` | `0.0` |
| `(0, 8)` | `0.0` |

```bash
python3 -m unittest discover -s practicas -p 'test_*.py' -k TestEtapa2Total -v
```

**Checkpoint:** las 4 pruebas de la etapa terminan en `OK`.

### Etapa 3 — reto obligatorio: reporte de turnos

Completa `reporte_turnos(turnos, stock)`. Ambos valores son enteros mayores o
iguales que cero. Genera una línea por cada turno de 1 a `turnos`: primero se
atienden como máximo `stock` turnos y los restantes quedan sin stock. Cada línea
termina en `\n`; con cero turnos devuelve `''`.

Para `(4, 2)`, el resultado exacto es:

```text
Turno 1: atendido
Turno 2: atendido
Turno 3: sin stock
Turno 4: sin stock
```

Usa `for`, `range`, `if` y una cadena acumuladora. No uses `while`, listas por
comprensión, `print()`, `input()` ni archivos.

```bash
python3 -m unittest discover -s practicas -p 'test_*.py' -k TestEtapa3Turnos -v
```

**Checkpoint final:** ejecuta desde la raíz:

```bash
python3 -m unittest discover -s practicas -p 'test_*.py' -v
```

Las 12 pruebas deben terminar en `OK`. Ejecuta las pruebas sin cambiarlas: son
la especificación pública para comprobar tu avance.

## Después del laboratorio

Entrega `feria_snacks.py` completado y un registro breve del proceso: qué
probaste, qué fallo de prueba viste y qué cambiaste. Durante la revisión oral,
demuestra una función y explica por qué devuelve el resultado en lugar de
imprimirlo. Escribe además un ejemplo propio válido para cada función y explica
qué caso límite verificaste. Estas tres evidencias muestran tu proceso, no solo
el resultado final.

Reflexiona:

1. ¿Qué diferencia encontraste entre `return` y `print()` al ejecutar las pruebas?
2. ¿Qué condición separa un turno atendido de uno sin stock?
3. ¿Qué ejemplo te ayudó a comprobar el redondeo y por qué?

## Rúbrica (100 puntos)

| Criterio | Puntos | Evidencia |
| --- | ---: | --- |
| Etapa 1 | 20 | 3 pruebas de etiqueta en `OK`. |
| Etapa 2 | 25 | 4 pruebas de total en `OK`. |
| Etapa 3 | 30 | 5 pruebas de turnos en `OK`. |
| Proceso y explicación oral | 15 | Registro breve y demostración razonada. |
| Ejemplos propios y reflexión | 10 | Tres ejemplos válidos y respuestas claras. |

## Comprobación del material docente

El punto de partida se comprobó con Python 3.15.0: las 12 pruebas se descubren
sin errores de importación ni pruebas omitidas. Inicialmente fallan por las
aserciones de los ejercicios aún incompletos.

Las mismas pruebas pasaron con una implementación temporal no incluida en el
material. También detectaron siete variantes incorrectas: cantidad ignorada,
redondeo omitido, stock invertido, último turno omitido, impresión indebida,
stock exacto mal resuelto y eliminación indebida de espacios. Los 14 ejemplos
anteriores conservan su salida y código de salida.

El ebook se comprobó de forma acotada con 36 pruebas existentes y el render HTML
de siete páginas de M1–M2 y de `if`/`for` de M3, sin ejecutar sus bloques. Esto no
certifica cada ejemplo del libro ni sus versiones PDF/EPUB. La práctica usa solo
la biblioteca estándar y no necesita las dependencias de validación del ebook.

## Más adelante

La validación de entradas con `input()`, `while`, archivos y programación
orientada a objetos se trabajarán en actividades posteriores. Esta práctica no
pretende cerrar esos temas.
