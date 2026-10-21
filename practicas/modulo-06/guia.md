# M6 · ¡Tu voto cuenta! Elige al representante

Analizarás una lista de votos para contar candidatos, eliminar repetidos y decidir si existe un ganador único. Edita `practicas/modulo-06/m06_votacion_club.py` siguiendo los TODO numerados.

## Objetivo

Usar diccionarios y sets para resumir una colección, reconocer duplicados y resolver un máximo único sin modificar las entradas.

## Antes del laboratorio

1. Repasa [crear diccionarios](https://statick88.github.io/Course_of_python/content/modulo-06/01-crear-diccionarios.html), [iterar diccionarios](https://statick88.github.io/Course_of_python/content/modulo-06/03-iterar-diccionarios.html), [sets](https://statick88.github.io/Course_of_python/content/modulo-06/04-sets.html) y el [desafío de votaciones](https://statick88.github.io/Course_of_python/content/modulo-06/desafio-05-votaciones.html).
2. Abre solo `practicas/modulo-06/m06_votacion_club.py` y revisa sus TODO.
3. Ejecuta:

```bash
python3 -m unittest discover -s practicas/modulo-06 -p 'test_m06_votacion_club.py' -v
```

Las pruebas iniciales fallan por las plantillas vacías. Ese resultado es esperado y no acredita dominio.

## Durante el laboratorio

### Parte 1 · Contar y reconocer candidatos

Completa `contar_votos(votos)` para devolver un diccionario de cantidades y `candidatos_unicos(votos)` para devolver un set. Una lista vacía es válida y no debe cambiarse.

```python
votos = ["Ana", "Luis", "Ana", "Mia"]
contar_votos(votos)        # {"Ana": 2, "Luis": 1, "Mia": 1}
candidatos_unicos(votos)   # {"Ana", "Luis", "Mia"}
contar_votos([])           # {}
candidatos_unicos([])      # set()
```

### Parte 2 · Decidir el ganador

Completa `ganador(conteo)`. Devuelve el nombre solo si la cantidad máxima pertenece a un único candidato. Devuelve `None` si no hay votos o el máximo está empatado. No modifiques el diccionario recibido.

```python
ganador({"Luis": 1, "Ana": 3, "Mia": 2})  # "Ana"
ganador({"Ana": 2})                          # "Ana"
ganador({"Ana": 2, "Luis": 2, "Mia": 1}) # None
ganador({})                                 # None
```

**Punto de control:** ejecuta el comando de prueba otra vez. Deben pasar las seis pruebas sin texto impreso por las funciones.

### Parte 3 · Explicar

Demuestra al docente por qué el orden de un set no importa para esta práctica y cómo detectaste que un empate no tiene ganador único.

## Después del laboratorio

Entrega el archivo editado, un registro de proceso y una explicación oral. En el registro describe una prueba con votos repetidos y una con empate. Agrega un ejemplo propio con nombres válidos diferentes y anota el resultado esperado antes de ejecutar tu código.

Reflexiona: ¿por qué contar votos requiere un diccionario mientras que conocer nombres distintos puede usar un set?

## Rúbrica · 100 puntos

| Criterio | Puntos |
|---|---:|
| Conteo correcto de repetidos y colección vacía | 25 |
| Set correcto de candidatos únicos | 20 |
| Ganador único, empate y conteo vacío | 30 |
| Conservación de listas y diccionarios de entrada | 10 |
| Registro, ejemplo propio y explicación oral | 15 |
