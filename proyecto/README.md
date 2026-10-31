# Tetris legado

Este miniproyecto conserva la primera versión independiente del Tetris del curso. Implementa un tablero de 10×20, los siete tetrominos, rotación, detección de colisiones, limpieza de líneas, tres vidas y tres niveles con una interfaz de Tkinter y estilo visual cian.

> `proyecto` es la versión inicial monolítica del ejemplo. El miniproyecto `proyecto2` mantiene su propia arquitectura modular y sus importaciones no se mezclan.

## Requisitos

- Python 3.10 o posterior.
- Un entorno gráfico disponible para Tkinter.
- Las dependencias declaradas en `requirements.txt`.

## Instalación y ejecución

Desde esta carpeta:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m src.main
```

La demostración gráfica requiere `customtkinter`, `pygame-ce` y una sesión de escritorio. No se instala ninguna dependencia ni se valida manualmente la GUI como parte de las pruebas automáticas.

## Controles

| Tecla | Acción |
| --- | --- |
| Flechas izquierda/derecha | Mover la pieza |
| Flecha arriba | Rotar |
| Flecha abajo | Bajar una celda |
| Espacio | Caída rápida |
| `P` | Pausar o reanudar |
| `R` | Reiniciar después de terminar las vidas |

## Estructura

- `src/core/board.py`: modelo del tablero, colisiones y limpieza de filas.
- `src/core/tetrominos.py`: formas y rotaciones de las piezas.
- `src/ui/renderer.py`: dibujo en el `Canvas` de Tkinter.
- `src/utils/audio.py`: reproducción opcional de música y efectos.
- `src/main.py`: controlador, interfaz y bucle con `root.after`.

## Pruebas de lógica

Desde la raíz del repositorio se puede validar la parte pura sin abrir la GUI:

```bash
python3 -m unittest discover -s tests -p 'test_legacy_tetris.py' -v
python3 -m compileall -q proyecto/src
```

Las pruebas ejecutan la lógica en un proceso aislado para no contaminar el paquete `src` de `proyecto2`.
