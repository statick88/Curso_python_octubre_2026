# M4 · Entrega especial: crea tu recibo de envío

> **Rama `solucion`:** el artefacto está resuelto y sus pruebas deben pasar sin modificar al evaluador docente. El enunciado original de `main` se conserva debajo para comparar el problema con la respuesta.

Construirás dos funciones que calculan un envío y presentan su recibo. El archivo que editas es `practicas/modulo-04/m04_recibo_envio.py`; no escribas un programa que pida datos ni imprimas resultados.

## Objetivo

Aplicar parámetros predeterminados, argumentos posicionales y por nombre, `return`, redondeo y composición de funciones para producir un texto exacto.

## Antes del laboratorio

1. Repasa [definir funciones](https://statick88.github.io/Course_of_python/content/modulo-04/01-definir-funciones.html), [parámetros y argumentos](https://statick88.github.io/Course_of_python/content/modulo-04/02-parametros-argumentos.html) y [return](https://statick88.github.io/Course_of_python/content/modulo-04/03-return.html).
2. Abre únicamente `practicas/modulo-04/m04_recibo_envio.py` y lee los TODO numerados.
3. Ejecuta la prueba inicial:

```bash
python3 -m unittest discover -s practicas/modulo-04 -p 'test_m04_recibo_envio.py' -v
```

Al principio es normal que falle: el archivo contiene plantillas deliberadamente incompletas. Ese fallo no demuestra dominio; solo confirma el punto de partida.

## Durante el laboratorio

### Parte 1 · Calcular

Completa `calcular_envio(peso, tarifa=3)`. Devuelve el peso multiplicado por la tarifa, redondeado a dos decimales. La tarifa predeterminada es `3`.

Ejemplos públicos:

```python
calcular_envio(2.5)  # 7.5
calcular_envio(2.5, 4)  # 10.0
calcular_envio(0)  # 0.0
calcular_envio(1.234, 2)  # 2.47
calcular_envio(2.5, tarifa=0)  # 0.0
```

### Parte 2 · Componer el recibo

Completa `crear_recibo(destino, peso, tarifa=3)` reutilizando el cálculo anterior. Debe **devolver**, no imprimir, el texto con moneda de dos decimales:

```python
crear_recibo("Loja", 2.5)  # "Envío a Loja: $7.50"
crear_recibo("Quito", 1.234, tarifa=2)  # "Envío a Quito: $2.47"
crear_recibo("Cuenca", 2.5, tarifa=0)  # "Envío a Cuenca: $0.00"
```

**Punto de control:** vuelve a ejecutar el comando de prueba. Debe completar las cuatro pruebas sin salida adicional de tus funciones.

### Parte 3 · Explicar

Muestra al docente una llamada con tarifa predeterminada y otra con `tarifa=`. Explica por qué `crear_recibo` debe llamar a `calcular_envio` en lugar de repetir la operación.

## Después del laboratorio

Entrega el archivo editado, un registro breve de proceso y una explicación oral. En el registro anota: intento, error o duda, cómo lo comprobaste y qué cambiaste. Añade un ejemplo propio con un destino y valores válidos distintos de los ejemplos anteriores.

Reflexiona: ¿qué cambia entre pasar `4` como segundo argumento y pasar `tarifa=4`?

## Rúbrica · 100 puntos

| Criterio | Puntos |
|---|---:|
| `calcular_envio` respeta tarifa predeterminada, argumentos y redondeo | 30 |
| `crear_recibo` compone el cálculo y conserva el formato exacto | 30 |
| Maneja el caso de peso cero y no imprime efectos laterales | 15 |
| Registro de proceso y ejemplo propio | 15 |
| Explicación oral de parámetros y composición | 10 |
