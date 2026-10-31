# Curso de Python

Ejemplos semanales, prácticas resueltas y miniproyectos del curso, reunidos en **un solo repositorio**. Los scripts semanales se ejecutan desde la raíz con `python3 ruta/al/archivo.py`; cada miniproyecto conserva sus dependencias e instrucciones propias.

## Organización

| Carpeta | Contenido | Guía |
| --- | --- | --- |
| `semana1/` | Primeros programas, comparaciones y FizzBuzz | Índice inferior |
| `semana2/` | Tipos, colecciones, control, funciones y excepciones | Índice inferior |
| `semana3/` | POO, herencia, encapsulamiento, polimorfismo, módulos y paquetes | [Semana 3](semana3/README.md) |
| `practicas/` | Once prácticas M0–M10 y las tres etapas de la feria | [Prácticas](practicas/README.md) |
| `proyecto/` | Tetris inicial: ejemplo de una aplicación con interfaz | [Tetris inicial](proyecto/README.md) |
| `proyecto2/` | Tetris modular: núcleo separado de interfaz y audio | [Tetris modular](proyecto2/README.md) |
| `tests/` | Comprobaciones del curso y de descubrimiento de prácticas | Comandos de verificación inferiores |

Los dos Tetris son ejemplos independientes, **no** paquetes que deban importarse juntos: ambos usan un paquete llamado `src`. Ejecuta cada uno según su README y usa entornos virtuales separados. No se versionan entornos, cachés, credenciales locales ni el respaldo local del historial Git anterior de `proyecto2/`.

## Prácticas guiadas por módulo

Consulta el [catálogo de prácticas, archivos y pruebas](practicas/README.md) y la [guía del ebook](https://statick88.github.io/Course_of_python/labs/practicas-abp-modulos.html). Cada módulo tiene un artefacto, una guía y pruebas docentes de la biblioteca estándar. Esta entrega completa los artefactos como ejemplos de solución; las guías conservan el contrato para estudiar y reproducir el ejercicio.

- **M0:** completa un plan en Markdown; las pruebas revisan su estructura, no la calidad del razonamiento.
- **M1–M8:** completa el archivo indicado por la guía del módulo.
- **M9:** escribe pruebas para las funciones docentes proporcionadas.
- **M10:** integra conceptos en un proyecto independiente, sin importar prácticas anteriores incompletas.

Elige un módulo y ejecuta su comando desde la raíz. Por ejemplo, M1:

```bash
python3 -m unittest discover -s practicas/modulo-01 -p 'test_m01_tarjeta_presentacion.py' -v
```

Las prácticas se publicaron originalmente como andamios **RED**; esta entrega incorpora las soluciones y sus comprobaciones. Para practicarlas, trabaja en una copia y contrasta tu implementación con las pruebas, sin modificarlas para obtener un resultado favorable. Las prácticas no requieren paquetes externos. La práctica complementaria [La feria del sabor: tu puesto de snacks](practicas/README.md#práctica-abp-puesto-de-snacks-de-la-feria) conserva sus tres archivos y sus 12 pruebas; el catálogo explica cómo seleccionarlas sin incluir otros módulos.

Las prácticas disponibles no cambian las casillas curriculares: una casilla marcada registra contenido previamente visto, no demuestra que se haya completado una actividad nueva.

La [rama histórica `solucion`](https://github.com/statick88/Curso_python_octubre_2026/tree/solucion/practicas) conserva la entrega anterior de snacks. Ya no es necesario cambiar de rama para estudiar las soluciones de esta entrega.

## Índice de ejemplos

### Semana 1: primeros programas, funciones y lógica

| Orden | Tema | Archivo | Ejecución |
| --- | --- | --- | --- |
| 01 | Saludo inicial | [`01_saludo_personal.py`](semana1/01_saludo_personal.py) | `python3 semana1/01_saludo_personal.py` |
| 02 | Hello, World! | [`02_hola_mundo.py`](semana1/02_hola_mundo.py) | `python3 semana1/02_hola_mundo.py` |
| 03 | Zen de Python e importación | [`03_zen_python.py`](semana1/03_zen_python.py) | `python3 semana1/03_zen_python.py` |
| 04 | Comparar tres números | [`04_mayor_de_tres.py`](semana1/04_mayor_de_tres.py) | `python3 semana1/04_mayor_de_tres.py` |
| 05 | Ciclo `for` y FizzBuzz | [`05_fizzbuzz.py`](semana1/05_fizzbuzz.py) | `python3 semana1/05_fizzbuzz.py` |

### Semana 2: fundamentos del lenguaje

| Orden | Tema | Archivo | Ejecución |
| --- | --- | --- | --- |
| 01 | Comentarios y docstrings | [`01_comentarios.py`](semana2/01_comentarios.py) | `python3 semana2/01_comentarios.py` |
| 02 | Variables y reasignación | [`02_variables.py`](semana2/02_variables.py) | `python3 semana2/02_variables.py` |
| 03 | Tipos de datos y colecciones | [`03_tipos_y_colecciones.py`](semana2/03_tipos_y_colecciones.py) | `python3 semana2/03_tipos_y_colecciones.py` |
| 04 | Cadenas y conversiones | [`04_cadenas_y_conversiones.py`](semana2/04_cadenas_y_conversiones.py) | `python3 semana2/04_cadenas_y_conversiones.py` |
| 05 | Operadores matemáticos y lógicos | [`05_operadores.py`](semana2/05_operadores.py) | `python3 semana2/05_operadores.py` |
| 06 | Condicionales | [`06_condicionales.py`](semana2/06_condicionales.py) | `python3 semana2/06_condicionales.py` |
| 07 | Indentación y funciones | [`07_indentacion.py`](semana2/07_indentacion.py) | `python3 semana2/07_indentacion.py` |
| 08 | Palabras reservadas | [`08_palabras_reservadas.py`](semana2/08_palabras_reservadas.py) | `python3 semana2/08_palabras_reservadas.py` |
| 09 | Nombres descriptivos | [`09_nombres_descriptivos.py`](semana2/09_nombres_descriptivos.py) | `python3 semana2/09_nombres_descriptivos.py` |
| 10 | Ciclo `while`, `break` y `continue` | [`10_while.py`](semana2/10_while.py) | `python3 semana2/10_while.py` |
| 11 | Ciclo `for` y `range` | [`11_for.py`](semana2/11_for.py) | `python3 semana2/11_for.py` |
| 12 | Funciones, `return` y alcance | [`12_funciones.py`](semana2/12_funciones.py) | `python3 semana2/12_funciones.py` |
| 13 | Errores con `try`, `except` y `finally` | [`13_excepciones.py`](semana2/13_excepciones.py) | `python3 semana2/13_excepciones.py` |

## Mapa de rutas

| Ruta anterior | Ruta actual |
| --- | --- |
| `semana1/hola.py` | `semana1/01_saludo_personal.py` |
| `semana1/helloWorld.py` | `semana1/02_hola_mundo.py` |
| `semana1/zen.py` | `semana1/03_zen_python.py` |
| `semana1/mayor_3.py` | `semana1/04_mayor_de_tres.py` |
| `semana1/fizzbuzz.py` | `semana1/05_fizzbuzz.py` |
| `semana2/comentarios.py` | `semana2/01_comentarios.py` |
| `semana2/variables.py` | `semana2/02_variables.py` |
| `semana2/tipos_datos.py` | `semana2/03_tipos_y_colecciones.py` |
| `semana2/string.py` | `semana2/04_cadenas_y_conversiones.py` |
| `semana2/operadores.py` | `semana2/05_operadores.py` |
| `semana2/condicionales.py` | `semana2/06_condicionales.py` |
| `semana2/identacion.py` | `semana2/07_indentacion.py` |
| `semana2/palabras_reservadas.py` | `semana2/08_palabras_reservadas.py` |
| `semana2/helloWorld.py` | `semana2/09_nombres_descriptivos.py` |

## Correspondencia con el ebook

La referencia es [Programación en Python + AI](https://github.com/statick88/course_of_python), específicamente su [índice fuente](https://github.com/statick88/course_of_python/blob/HEAD/_quarto.yml) y las guías de [prácticas M0–M10](https://github.com/statick88/course_of_python/blob/HEAD/labs/practicas-abp-modulos.qmd) y [feria de snacks](https://github.com/statick88/course_of_python/blob/HEAD/labs/practica-abp-feria-snacks.qmd). El ebook es una fuente de consulta: esta revisión no modifica su repositorio.

| Módulos del ebook | Evidencia en este repositorio |
| --- | --- |
| M0: pensamiento computacional | FizzBuzz y `practicas/modulo-00/` |
| M1–M3: introducción, tipos y control | `semana1/`, `semana2/`, prácticas M1–M3 y feria |
| M4–M6: funciones y colecciones | Ejemplos de semana 2 y prácticas M4–M6 |
| M7: archivos, CSV, JSON y `pathlib` | Práctica M7 y biblioteca M10 |
| M8: módulos y paquetes | `semana3/modulos/`, `semana3/modulo2/` y práctica M8 |
| M9: buenas prácticas y pruebas | Docstrings, manejo de errores, práctica M9 y suites de pruebas |
| M10: integración | Biblioteca M10 y los miniproyectos Tetris como ejemplos adicionales |
| POO complementaria | `semana3/` y los dos Tetris |

La correspondencia registra material disponible, no certifica dominio del estudiante ni cobertura total de todos los desafíos del ebook. Tetris es complementario: no se presenta como sustituto de los proyectos específicos del M10. Generadores y decoradores no se añaden artificialmente para marcar casillas.

## Verificación local

Desde la raíz, las comprobaciones de biblioteca estándar son:

```bash
python3 -m unittest discover -s practicas -p 'test_*.py' -v
python3 practicas/modulo-07/regression_m07.py -v
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 -m compileall -q semana1 semana2 semana3 practicas proyecto/src proyecto2/src
```

La suite de Tetris modular usa `pytest`; sigue [su preparación y comandos](proyecto2/README.md). Sus pruebas del núcleo no requieren abrir ventanas. Las pruebas automáticas no sustituyen la comprobación visual de las interfaces ni la escucha de audio en un equipo con las dependencias y recursos correspondientes.

## Checklist curricular histórico

Esta sección conserva el registro de ejemplos impartidos **antes de esta revisión**; las casillas no son el estado de implementación actual ni una evaluación del alumnado. Para el material incorporado consulta la correspondencia anterior. Los ejemplos solo comentados no cuentan como contenido impartido.

### M0. Pensamiento computacional — Inicial

- [x] Resolver un problema concreto con FizzBuzz.
- [x] Escribir pseudocódigo.
- [x] Descomponer explícitamente un problema en pasos.

### M1. Introducción — Parcial

- [x] Ejecutar scripts y usar `print`.
- [x] Conocer palabras reservadas con `keyword`.
- [x] Obtener datos con `input`.

### M2. Tipos, operadores, casting y strings — Parcial

- [x] Usar variables con `bool`, `int`, `float` y `str`.
- [x] Usar operaciones matemáticas y comparaciones `>`, `<`, `>=` y `==`.
- [x] Convertir activamente con `int` y `str`.
- [x] Usar escapes y cadenas crudas.
- [x] Convertir con `float` y `bool`.
- [ ] Usar métodos, f-strings y slicing de cadenas.
- [ ] Usar `None`, identidad y pertenencia.
- [ ] Usar números complejos en código activo.
- [x] Usar comparaciones `!=` en código activo.

### M3. Control de flujo — Parcial

- [x] Usar `if`, `elif`, `else` y una expresión condicional.
- [x] Usar `for` y `range`.
- [x] Usar `while`, `break` y `continue`.
- [ ] Usar condicionales anidados y comprehensions.

### M4. Funciones — Parcial

- [x] Definir funciones, recibir parámetros, retornar y llamar funciones.
- [ ] Usar parámetros por defecto, con nombre, `*args` y `**kwargs`.
- [x] Entender alcance: variables locales y globales.
- [ ] Usar `lambda` y recursión.

### M5. Listas y tuplas — Parcial

- [x] Crear listas, acceder por índice y usar `append` y `remove`.
- [x] Crear tuplas.
- [ ] Usar slicing, métodos de colecciones, iteración y anidamiento.

### M6. Diccionarios y sets — Parcial

- [x] Crear diccionarios, usar claves y eliminar con `pop`.
- [x] Crear sets para eliminar duplicados.
- [x] Acceder, actualizar e iterar diccionarios.
- [x] Usar diccionarios anidados y operaciones de sets.

### M7. Archivos, CSV, JSON y `pathlib` — Pendiente

- [ ] Abrir, leer y escribir archivos.
- [ ] Trabajar con CSV y JSON.
- [ ] Usar `pathlib`.

No hay ejemplos impartidos registrados para esta sección; las prácticas disponibles no modifican ese historial.

### M8. Módulos, paquetes, `pip` y entornos virtuales — Parcial

- [x] Importar módulos estándar, incluidos `math`, `this` y `keyword`.
- [ ] Crear módulos personalizados y paquetes.
- [ ] Usar `pip` y entornos virtuales.

### M9. Buenas prácticas, errores, docstrings y testing — Parcial

- [x] Usar nombres, comentarios, docstrings y sangría de cuatro espacios en ejemplos existentes.
- [x] Aplicar PEP 8 de forma formal.
- [x] Manejar errores y excepciones.
- [ ] Escribir pruebas.

### M10. Proyecto integrador — Pendiente

- [ ] Planificar el proyecto.
- [ ] Definir su estructura.
- [ ] Construirlo y presentarlo.

No hay ejemplos impartidos registrados para esta sección; las prácticas disponibles no modifican ese historial.

### Temas complementarios pendientes de Majo

- [ ] Programación orientada a objetos.
- [ ] Generadores.
- [ ] Decoradores.

Estos temas son complementarios pendientes y no se presentan como módulos numerados actuales. Cuando haya material nuevo, puede complementarse con [Los apuntes de Majo](https://losapuntesdemajo.vercel.app).

## Recursos

- Repositorio principal del curso: [statick88/course_of_python](https://github.com/statick88/course_of_python)
- Material complementario: [Los apuntes de Majo](https://losapuntesdemajo.vercel.app)

Los enlaces de los ejemplos de este README describen los archivos presentes en este repositorio; no se afirma que cada fuente esté publicada por separado.
