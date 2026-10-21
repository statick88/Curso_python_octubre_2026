# M5 · La maleta inteligente: prepara tu aventura

Organizarás pesos y paradas sin cambiar los datos originales. Edita solo `practicas/modulo-05/m05_maleta.py` y sigue los TODO numerados.

## Objetivo

Practicar listas, tuplas, recorrido, filtrado, orden y creación de resultados nuevos.

## Antes del laboratorio

1. Repasa [crear listas](https://statick88.github.io/Course_of_python/content/modulo-05/01-crear-listas.html), [métodos de listas](https://statick88.github.io/Course_of_python/content/modulo-05/03-metodos-listas.html), [iterar listas](https://statick88.github.io/Course_of_python/content/modulo-05/04-iterar-listas.html) y [tuplas](https://statick88.github.io/Course_of_python/content/modulo-05/05-tuplas.html).
2. Abre `practicas/modulo-05/m05_maleta.py`; no borres las firmas ni los TODO.
3. Ejecuta:

```bash
python3 -m unittest discover -s practicas/modulo-05 -p 'test_m05_maleta.py' -v
```

El resultado inicial debe fallar porque las plantillas están vacías. No infieras dominio a partir de ese estado inicial.

## Durante el laboratorio

### Parte 1 · Peso total

Completa `peso_total(pesos)` para devolver la suma. Una colección vacía suma cero.

```python
peso_total([1.2, 2.3, 0.5])  # 4.0
peso_total([])               # 0
```

### Parte 2 · Elegir artículos ligeros

Completa `seleccionar_livianos(pesos, limite)`. Devuelve una **lista nueva** con cada peso menor o igual que el límite y en el mismo orden. No modifiques `pesos`.

```python
seleccionar_livianos([5, 2, 5, 1], 5)  # [5, 2, 5, 1]
seleccionar_livianos([1, 4, 7], 4)     # [1, 4]
seleccionar_livianos([], 4)            # []
```

### Parte 3 · Regresar por el itinerario

Completa `invertir_itinerario(paradas)`. Recibe una tupla y devuelve una lista nueva en orden inverso; la tupla no cambia.

```python
invertir_itinerario(("Quito", "Ambato", "Loja"))  # ["Loja", "Ambato", "Quito"]
invertir_itinerario(())                              # []
invertir_itinerario(("Cuenca",))                    # ["Cuenca"]
```

**Punto de control:** ejecuta de nuevo la prueba. Deben pasar las cinco pruebas y las colecciones de entrada deben permanecer iguales.

## Después del laboratorio

Entrega el archivo editado, un registro de proceso y una explicación oral. Registra al menos una decisión sobre `<=`, orden o creación de una lista nueva. Añade un ejemplo propio válido y explica por qué modificar el resultado de `seleccionar_livianos` no debe cambiar la lista original.

Reflexiona: ¿por qué una tupla es apropiada para las paradas de este ejercicio?

## Rúbrica · 100 puntos

| Criterio | Puntos |
|---|---:|
| Suma correcta, incluida colección vacía | 20 |
| Filtro con igualdad, orden y lista nueva | 30 |
| Inversión de tupla en una lista nueva | 25 |
| Conservación de las entradas | 10 |
| Registro, ejemplo propio y explicación oral | 15 |
