# M8 · La fábrica de saludos: crea tu paquete

> **Rama `solucion`:** el artefacto está resuelto y sus pruebas deben pasar sin modificar al evaluador docente. El enunciado original de `main` se conserva debajo para comparar el problema con la respuesta.

Reutiliza un catálogo docente desde un paquete y completa una función de formato.

## Objetivo y requisito

- Importar un valor desde un módulo del mismo paquete y exponer una API pública.
- Revisa [importar módulos](https://statick88.github.io/Course_of_python/content/modulo-08/01-importar-modulos.html), [crear módulos](https://statick88.github.io/Course_of_python/content/modulo-08/03-crear-modulos.html) y [paquetes](https://statick88.github.io/Course_of_python/content/modulo-08/04-paquetes.html).

## Ruta rápida

1. Edita solo `practicas/modulo-08/m08_saludos/formato.py`.
2. No cambies `__init__.py`, `catalogo.py` ni `test_m08_saludos.py`: son archivos docentes.
3. Ejecuta desde la raíz: `python3 -m unittest discover -s practicas/modulo-08 -p 'test_m08_saludos.py' -v`.

`construir_saludo('Ana', 'manana')` debe devolver `Buenos días, Ana.`. Los otros momentos válidos son `tarde` (`Buenas tardes`) y `noche` (`Buenas noches`). Mantén acentos, coma y punto final.

## Pre-lab

Dibuja qué archivo importa a cuál y anota por qué el usuario importa desde `m08_saludos`, no desde un archivo interno.

## En laboratorio

Consulta `SALUDOS` y construye el texto sin copiar el catálogo. **Checkpoint:** demuestra las tres llamadas mediante el export público del paquete.

## Post-lab

Registra el error de importación o formato que encontraste y cómo lo corregiste. En defensa oral explica la diferencia entre `catalogo.py` y `formato.py`. Añade a tu bitácora un nombre propio distinto y su saludo nocturno.

## Rúbrica (100 puntos)

| Criterio | Puntos |
|---|---:|
| Uso correcto del catálogo | 30 |
| Textos exactos en los tres momentos | 30 |
| API pública y límites de edición respetados | 15 |
| Bitácora, checkpoint y defensa oral | 15 |
| Ejemplo propio | 10 |
