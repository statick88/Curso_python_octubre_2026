# M2: presupuesto de viaje

Transforma datos de texto en un costo y en un mensaje listo para mostrar después.

## Objetivo y requisitos previos

Practicar conversión numérica, cadenas, métodos y `round()`. Revisa las lecciones oficiales de [operadores aritméticos](https://statick88.github.io/Course_of_python/content/modulo-02/01-operadores-aritmeticos.html), [conversión](https://statick88.github.io/Course_of_python/content/modulo-02/04-casting-avanzado.html) y [cadenas](https://statick88.github.io/Course_of_python/content/modulo-02/05-strings-avanzado.html). Esta práctica usa solo Python 3.

## Antes del laboratorio

1. ¿Por qué `"12"` no es todavía el número 12?
2. ¿Qué resultado esperas al multiplicar distancia 12 por tarifa 0.35?
3. ¿Para qué sirven dos decimales en un costo?

## Durante el laboratorio

Edita **solo** `practicas/m02_presupuesto_viaje.py`. Completa las tres funciones sin `print()`, `input()` ni manejo de entradas inválidas. Los textos válidos representan números finitos no negativos.

| Llamada | Resultado |
| --- | --- |
| `calcular_costo('12', '0.35')` | `4.2` |
| `calcular_costo('0', '2.5')` | `0.0` |
| `calcular_costo('12', '0')` | `0.0` |
| `normalizar_destino(' loja ')` | `'Loja'` |
| `formatear_presupuesto(' loja ', 4.2)` | `'Viaje a Loja: $4.20'` |

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s practicas -p 'test_m02_presupuesto_viaje.py' -v
```

**Checkpoint:** RED inicial significa que los `return` provisionales aún no cumplen el contrato, no un error de sintaxis. GREEN tras tu solución confirma ejemplos, cero, redondeo, formato, ausencia de salida y conservación de argumentos.

## Después del laboratorio

Registra las conversiones que probaste y los fallos que corregiste. En la defensa oral explica una conversión y por qué las funciones devuelven valores. Añade dos ejemplos propios válidos, incluido uno con costo cero.

## Rúbrica (100 puntos)

| Criterio | Puntos |
| --- | ---: |
| Cálculo y redondeo | 30 |
| Normalización de destino | 20 |
| Formato exacto del presupuesto | 25 |
| Registro y ejemplos propios | 10 |
| Defensa oral | 15 |

Las pruebas son del docente y no se modifican. Añadir esta práctica no constituye evidencia de enseñanza o dominio previo.
