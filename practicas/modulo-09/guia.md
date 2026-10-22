# M9 · Cazadores de errores: prueba los impuestos

Aquí tu producto es una suite `unittest`: las funciones de impuestos son soporte docente, no una solución que debas reescribir.

## Objetivo y requisito

- Formular aserciones observables para resultados normales, cero, redondeo y errores.
- Revisa [testing básico](https://statick88.github.io/Course_of_python/content/modulo-09/06-testing-basico.html), [funciones puras](https://statick88.github.io/Course_of_python/content/modulo-09/03-funciones-puras.html) y [manejo de errores](https://statick88.github.io/Course_of_python/content/modulo-09/04-manejo-errores.html).
- El ebook presenta pytest; esta práctica introduce la alternativa estándar `unittest` sin reemplazar esa lección.

## Ruta rápida

1. Edita solo `practicas/modulo-09/m09_pruebas_impuesto.py`.
2. No edites `soporte_m09_impuestos.py` ni `test_m09_pruebas_impuesto.py`: son docentes.
3. Ejecuta desde la raíz: `python3 -m unittest discover -s practicas/modulo-09 -p 'test_m09_pruebas_impuesto.py' -v`.

Sustituye los cuatro `TODO` por pruebas significativas para `calcular_subtotal` y `aplicar_iva`. Importa sus APIs públicas directamente. Cubre ambas APIs: cantidad (incluido cero), redondeo y negativos separados para subtotal; tasa por defecto y explícita, redondeo y negativos separados para IVA. Puedes usar `subTest` y varias aserciones por método; no omitas ni declares fallos esperados.

## Pre-lab

Predice qué debe comprobar una prueba de redondeo que no comprobaría una prueba de importe entero. Escribe esa predicción en tu bitácora.

## En laboratorio

Completa una prueba y ejecútala antes de continuar con la siguiente. **Checkpoint:** muestra cuatro pruebas verdes y explica qué mutante detectaría cada una.

## Post-lab

Registra al menos un fallo inicial y su corrección. En defensa oral explica por qué una suite que siempre pasa no protege el cálculo. Propón un importe propio con tasa y resultado esperado, sin modificar el soporte docente.

## Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| Casos normal y cero | 25 |
| Redondeo observable | 25 |
| Excepciones negativas | 20 |
| Pruebas independientes y sin omisiones | 15 |
| Bitácora, checkpoint, defensa y ejemplo | 15 |
