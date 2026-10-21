# Misiones Python: aprende practicando

Cada actividad es independiente: completa sus comentarios `TODO` o marcadores y ejecuta únicamente la prueba de ese módulo. No necesitas terminar archivos anteriores para importar la práctica siguiente. Disponer de una actividad no significa que sus temas ya se hayan impartido o dominado.

Usa Python 3 y su biblioteca estándar, sin instalar paquetes. Consulta también el [catálogo del ebook](https://statick88.github.io/Course_of_python/labs/practicas-abp-modulos.html): explica qué repasar, qué revisar y qué evidencia entregar.

## Catálogo M0–M10

Cada módulo tiene su carpeta `practicas/modulo-NN/`, con el archivo de trabajo, las pruebas y `guia.md`. La tabla muestra nombres breves; sus enlaces incluyen la carpeta completa. Ejecuta los comandos desde la **raíz del repositorio**, sin cambiar de directorio entre módulos.

| Módulo | Artefacto que editas | Prueba docente | Instrucciones |
| --- | --- | --- | --- |
| M0 · Misión excursión: planifica la aventura | [m00_planificador.md](modulo-00/m00_planificador.md) | [test_m00_planificador.py](modulo-00/test_m00_planificador.py) | [Guía M0](modulo-00/guia.md) |
| M1 · ¡Hola, equipo! Tu tarjeta de presentación | [m01_tarjeta_presentacion.py](modulo-01/m01_tarjeta_presentacion.py) | [test_m01_tarjeta_presentacion.py](modulo-01/test_m01_tarjeta_presentacion.py) | [Guía M1](modulo-01/guia.md) |
| M2 · Rumbo a la aventura: calcula tu presupuesto | [m02_presupuesto_viaje.py](modulo-02/m02_presupuesto_viaje.py) | [test_m02_presupuesto_viaje.py](modulo-02/test_m02_presupuesto_viaje.py) | [Guía M2](modulo-02/guia.md) |
| M3 · Detectives de números: pares e impares | [m03_reporte_paridad.py](modulo-03/m03_reporte_paridad.py) | [test_m03_reporte_paridad.py](modulo-03/test_m03_reporte_paridad.py) | [Guía M3](modulo-03/guia.md) |
| M4 · Entrega especial: crea tu recibo de envío | [m04_recibo_envio.py](modulo-04/m04_recibo_envio.py) | [test_m04_recibo_envio.py](modulo-04/test_m04_recibo_envio.py) | [Guía M4](modulo-04/guia.md) |
| M5 · La maleta inteligente: prepara tu aventura | [m05_maleta.py](modulo-05/m05_maleta.py) | [test_m05_maleta.py](modulo-05/test_m05_maleta.py) | [Guía M5](modulo-05/guia.md) |
| M6 · ¡Tu voto cuenta! Elige al representante | [m06_votacion_club.py](modulo-06/m06_votacion_club.py) | [test_m06_votacion_club.py](modulo-06/test_m06_votacion_club.py) | [Guía M6](modulo-06/guia.md) |
| M7 · Misión inventario: del CSV al JSON | [m07_exportar_inventario.py](modulo-07/m07_exportar_inventario.py) | [test_m07_exportar_inventario.py](modulo-07/test_m07_exportar_inventario.py) | [Guía M7](modulo-07/guia.md) |
| M8 · La fábrica de saludos: crea tu paquete | [m08_saludos/formato.py](modulo-08/m08_saludos/formato.py) | [test_m08_saludos.py](modulo-08/test_m08_saludos.py) | [Guía M8](modulo-08/guia.md) |
| M9 · Cazadores de errores: prueba los impuestos | [m09_pruebas_impuesto.py](modulo-09/m09_pruebas_impuesto.py) | [test_m09_pruebas_impuesto.py](modulo-09/test_m09_pruebas_impuesto.py) | [Guía M9](modulo-09/guia.md) |
| M10 · Pasaporte lector: organiza tu biblioteca | [m10_biblioteca.py](modulo-10/m10_biblioteca.py) | [test_m10_biblioteca.py](modulo-10/test_m10_biblioteca.py) | [Guía M10](modulo-10/guia.md) |

**Límites de la evaluación:** M0 revisa estructura y requiere defensa humana del razonamiento. En M8 no edites `__init__.py` ni `catalogo.py`. En M9 escribes al menos cuatro métodos de prueba para las funciones de [soporte docente](modulo-09/soporte_m09_impuestos.py); el evaluador externo ejecuta tu suite y comprueba que detecte errores. En M10 integras lectura, resumen y guardado dentro del mismo archivo, sin importar otros ejercicios incompletos.

## Elegir y ejecutar pruebas

Ejemplo para M5; cada guía contiene su comando exacto:

```bash
python3 -m unittest discover -s practicas/modulo-05 -p 'test_m05_maleta.py' -v
```

La plantilla inicial debe dar **FAIL por aserciones**, no errores de importación o sintaxis ni pruebas omitidas. Tras completar el artefacto, su suite debe dar `OK`. No cambies pruebas docentes para conseguirlo; en M9, el archivo estudiantil de pruebas sí es tu producto.

Para revisar todos los módulos nuevos:

```bash
python3 -m unittest discover -s practicas -p 'test_m*.py' -v
```

Este comando descubre 46 métodos docentes. El comando global incluye además las 12 pruebas de snacks, es decir, 58 métodos docentes; el evaluador M9 ejecuta internamente los métodos que escribas, sin duplicarlos en ese conteo:

```bash
python3 -m unittest discover -s practicas -p 'test_*.py' -v
```

No necesitas que el comando global pase para entregar un solo módulo: los demás artefactos pueden seguir incompletos. En M7 y M10 las pruebas usan directorios temporales y datos sintéticos; no uses archivos personales como fixtures.

## Organización del material docente

`test_modulos.py` agrupa las carpetas para conservar los comandos globales y el filtro de snacks; es infraestructura docente, no un archivo del estudiante. Las verificaciones de organización se ejecutan por separado y no requieren completar los TODO:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

<a id="práctica-abp-puesto-de-snacks-de-la-feria"></a>

## La feria del sabor: tu puesto de snacks

Construirás, por etapas, tres funciones de un puesto de snacks. Cada etapa tiene
su propio archivo: sigue los comentarios `TODO`, ejecuta su prueba docente y
mejora tu código hasta que pase. No hay una solución entregada: el resultado se
verifica por el comportamiento público.

**Duración estimada:** 90 minutos.

**Herramienta:** Python 3 y su biblioteca estándar; no instales paquetes ni uses `pip`.

### Objetivos

Al finalizar podrás:

- devolver resultados desde funciones con parámetros;
- construir cadenas y calcular un total redondeado;
- usar `for`, `range` e `if` para producir un reporte acumulado;
- interpretar fallos de `unittest` como retroalimentación.

### Antes de empezar

**Conocimientos usados:** funciones, parámetros y `return`; cadenas, números y
operadores; `if` y `for`/`range`. Son actividades de M1–M2 y de lo ya visto de
M3. La lectura de `input()` es anticipada, pero **no se usa** en esta práctica.

Lee, como máximo 20 minutos:

- [Módulo 1](https://statick88.github.io/Course_of_python/content/modulo-01/index.html): introducción y f-strings.
- [Módulo 2](https://statick88.github.io/Course_of_python/content/modulo-02/index.html): cadenas, números y `round`.
- [Módulo 3](https://statick88.github.io/Course_of_python/content/modulo-03/index.html): secciones `if` y `for`.

Desde la raíz del repositorio, comprueba Python:

```bash
python3 --version
```

Al comienzo las pruebas deben mostrar **FAIL** por aserciones: las funciones
tienen un `return` provisional sin valor (devuelve `None`) que debes completar.
El filtro de esta actividad selecciona 12 pruebas docentes, sin errores de
importación o sintaxis ni pruebas omitidas. Algunos tests tienen subcasos, por lo que el número de fallos
puede ser mayor que 12.

Todos los comandos siguientes parten de la raíz del repositorio; no cambies de
directorio entre etapas.

### Archivos y roles

| Etapa | Tu archivo de trabajo | Prueba docente | Comando desde la raíz |
| --- | --- | --- | --- |
| 1 — etiqueta | `etiqueta_pedido.py` | `test_etiqueta_pedido.py` | `python3 -m unittest discover -s practicas -p 'test_etiqueta_pedido.py' -v` |
| 2 — total | `calcular_total.py` | `test_calcular_total.py` | `python3 -m unittest discover -s practicas -p 'test_calcular_total.py' -v` |
| 3 — turnos | `reporte_turnos.py` | `test_reporte_turnos.py` | `python3 -m unittest discover -s practicas -p 'test_reporte_turnos.py' -v` |

Completa únicamente el cuerpo de la función de tu etapa. Las clases `TestCase`,
las importaciones de la biblioteca estándar y la captura de salida pertenecen a
la infraestructura docente; no requieren conocimientos de programación
orientada a objetos.

### En el laboratorio

#### Etapa 1 — guiada: etiqueta del pedido

Completa `etiqueta_pedido(evento, producto, cantidad)` en `etiqueta_pedido.py`.

| Entrada válida | Salida exacta |
| --- | --- |
| `('Feria', 'Jugo', 3)` | `'Feria | 3 x Jugo'` |
| `('Patio', 'Pan', 0)` | `'Patio | 0 x Pan'` |

Los textos son cadenas no vacías tal como llegan; `cantidad` es un entero mayor
o igual que cero. Devuelve la cadena: no imprimas ni solicites datos.

```bash
python3 -m unittest discover -s practicas -p 'test_etiqueta_pedido.py' -v
```

**Checkpoint:** las 3 pruebas de la etapa terminan en `OK`.

#### Etapa 2 — independiente: total del pedido

Completa `calcular_total(precio_unitario, cantidad)` en `calcular_total.py`. El
precio es un `int` o `float` finito no negativo y la cantidad es un entero no
negativo. Devuelve el total redondeado a dos decimales; los valores fuera de ese
contrato no forman parte de esta actividad.

| Entrada válida | Salida esperada |
| --- | --- |
| `(2.5, 3)` | `7.5` |
| `(1.235, 3)` | `3.71` |
| `(4, 0)` | `0.0` |
| `(0, 8)` | `0.0` |

```bash
python3 -m unittest discover -s practicas -p 'test_calcular_total.py' -v
```

**Checkpoint:** las 4 pruebas de la etapa terminan en `OK`.

#### Etapa 3 — reto obligatorio: reporte de turnos

Completa `reporte_turnos(turnos, stock)` en `reporte_turnos.py`. Ambos valores
son enteros mayores o iguales que cero. Genera una línea por cada turno de 1 a
`turnos`: primero se atienden como máximo `stock` turnos y los restantes quedan
sin stock. Cada línea termina en `\n`; con cero turnos devuelve `''`.

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
python3 -m unittest discover -s practicas -p 'test_reporte_turnos.py' -v
```

**Checkpoint final de snacks:** ejecuta desde la raíz el filtro que conserva las 12 pruebas originales:

```bash
python3 -m unittest discover -s practicas -p 'test_*.py' -k TestEtapa -v
```

Las 12 pruebas deben terminar en `OK`. Ejecuta las pruebas sin cambiarlas: son
la especificación pública para comprobar tu avance.

### Después del laboratorio

Entrega los tres archivos completados (`etiqueta_pedido.py`,
`calcular_total.py` y `reporte_turnos.py`) y un registro breve del proceso: qué
probaste, qué fallo de prueba viste y qué cambiaste. Durante la revisión oral,
demuestra una función y explica por qué devuelve el resultado en lugar de
imprimirlo. Escribe además un ejemplo propio válido para cada función y explica
qué caso límite verificaste. Estas tres evidencias muestran tu proceso, no solo
el resultado final.

Reflexiona:

1. ¿Qué diferencia encontraste entre `return` y `print()` al ejecutar las pruebas?
2. ¿Qué condición separa un turno atendido de uno sin stock?
3. ¿Qué ejemplo te ayudó a comprobar el redondeo y por qué?

### Rúbrica (100 puntos)

| Criterio | Puntos | Evidencia |
| --- | ---: | --- |
| Etapa 1 | 20 | 3 pruebas de etiqueta en `OK`. |
| Etapa 2 | 25 | 4 pruebas de total en `OK`. |
| Etapa 3 | 30 | 5 pruebas de turnos en `OK`. |
| Proceso y explicación oral | 15 | Registro breve y demostración razonada. |
| Ejemplos propios y reflexión | 10 | Tres ejemplos válidos y respuestas claras. |

### Comprobación original del material de snacks

El punto de partida se comprobó con Python 3.15.0: las 12 pruebas se descubren
sin errores de importación ni pruebas omitidas. Inicialmente fallan por las
aserciones de los ejercicios aún incompletos.

Las mismas pruebas pasaron con una implementación temporal no incluida en el
material. También detectaron siete variantes incorrectas: cantidad ignorada,
redondeo omitido, stock invertido, último turno omitido, impresión indebida,
stock exacto mal resuelto y eliminación indebida de espacios. Los 14 ejemplos
anteriores conservan su salida y código de salida.

En la validación original de snacks, el ebook se comprobó de forma acotada con 36 pruebas existentes y el render HTML
de siete páginas de M1–M2 y de `if`/`for` de M3, sin ejecutar sus bloques. Esto
no certifica cada ejemplo del libro ni sus versiones PDF/EPUB. La práctica usa
solo la biblioteca estándar y no necesita las dependencias de validación del
ebook.

### Más adelante en la actividad de snacks

La validación de entradas con `input()`, `while`, archivos y programación
orientada a objetos se trabajarán en actividades posteriores. Esta práctica no
pretende cerrar esos temas.
