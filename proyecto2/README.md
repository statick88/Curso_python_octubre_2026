# Tetris: miniproyecto del curso

Ejemplo de Tetris de escritorio dentro del repositorio del curso. La lógica de
partida vive en `src/core/` y se prueba sin abrir una ventana; `src/ui/` solo
renderiza su estado con Tkinter.

## Funcionalidades implementadas

- Tablero de 10 × 20, siete tetrominós, colisiones, limpieza de líneas y caída
  suave o rápida.
- Puntuación por líneas y por caída, tres niveles, velocidad creciente y tres
  vidas.
- Pausa con `P`, reinicio solo tras `GAME OVER` con `R`, y overlays de ambos
  estados.
- HUD con `PUNTOS`, `NIVEL`, `VIDAS`, `LÍNEAS` y la siguiente pieza.
- Feedback visual breve al completar líneas y al subir de nivel.
- Música de fondo y efectos opcionales: al pausar se pausa la música y al
  reanudar se continúa. Si falta pygame, un dispositivo de audio o un recurso,
  el juego continúa en silencio y emite un único aviso con rutas absolutas.

## Dependencias

- Python 3.10 o superior con `tkinter` disponible para ejecutar la interfaz.
  La comprobación local se realizó con `../.venv/bin/python` (Python 3.12.16 y
  Tk 9.1). El Python del sistema 3.15 no dispone de `_tkinter` utilizable aquí.
- `customtkinter` y `pygame`, declarados en `requirements.txt`.
- `pytest`, declarado en `requirements-dev.txt`, para la suite completa.

Instalación en un entorno virtual propio:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
```

## Ejecución

```bash
../.venv/bin/python src/main.py
```

Controles: `←`/`→` mover, `↓` caída suave, `↑` rotar, `ESPACIO` caída rápida,
`P` pausar o reanudar y `R` reiniciar únicamente después de `GAME OVER`.

## Pruebas sin interfaz

La lógica y los fakes de audio/Canvas son deterministas y no requieren abrir
una ventana ni disponer de audio:

```bash
../.venv/bin/python -m pytest -q
../.venv/bin/python -m compileall -q src
```

Si el entorno no tiene pytest, puede comprobarse el nuevo conjunto aislado con
el intérprete disponible:

```bash
PYTHONPATH=. python -m unittest discover -s tests -p 'test_audio_ui.py'
```

## Limitaciones de ejecución local

Los directorios `assets/sounds/` y `assets/fonts/` contienen marcadores, no
medios de audio funcionales. La suite demuestra la degradación silenciosa y la
coordinación con fakes, pero no sustituye una prueba manual con pantalla Tk,
recursos de audio reales y un dispositivo de salida disponible.

## Referencia de trabajo

El comportamiento intencional del miniproyecto se documenta en
`odd/tasks/tetris-odd-rdd.md`. Este proyecto es una carpeta del repositorio
único del curso; no crea ni requiere un repositorio independiente.
