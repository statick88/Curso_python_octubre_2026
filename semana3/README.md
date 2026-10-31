# Semana 3: programación orientada a objetos y módulos

Los archivos de esta carpeta son ejemplos independientes para practicar clases, encapsulamiento, herencia, polimorfismo e importación de módulos. Se mantienen como miniproyectos dentro del repositorio del curso; no son paquetes que deban mezclarse con los dos ejemplos de Tetris.

## Ejecución rápida

Desde la raíz del repositorio, cada ejemplo se ejecuta con Python 3:

```bash
python3 semana3/perro.py
python3 semana3/encapsulamiento.py
python3 semana3/herencia.py
python3 semana3/polimorfismo.py
python3 semana3/poo.py
python3 semana3/modulos/calculadora.py
python3 semana3/modulos/uso_contador.py
python3 semana3/modulo2/main.py
```

`semana3/modulos/uso_contador.py` importa `contador.py` desde su propia carpeta. De igual modo, `semana3/modulo2/main.py` importa el paquete local `utils`; por ello deben ejecutarse usando las rutas anteriores y no mediante imports globales desde otro miniproyecto.

## Contenido

- `encapsulamiento.py`: atributo privado y método público para actualizarlo.
- `herencia.py`: herencia múltiple de `Animal` y `Mamifero`.
- `polimorfismo.py`: distintas implementaciones de `hablar`.
- `perro.py` y `poo.py`: clases, atributos, métodos y representación de objetos.
- `modulos/`: módulos simples, importación y estado de módulo.
- `modulo2/`: paquete `utils` con operaciones de texto y números.

Las clases base `Mamifero` y `Animal.hablar` usan `pass` de forma intencional: son puntos de partida didácticos para mostrar herencia y polimorfismo, no comportamiento de producción incompleto.

## Verificación

Desde la raíz del repositorio:

```bash
python3 -m unittest discover -s tests -p 'test_weekly_examples.py' -v
python3 -m compileall -q semana1 semana2 semana3
```
