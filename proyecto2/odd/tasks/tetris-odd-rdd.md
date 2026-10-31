# Feature: Tetris ODD + RDD

Objetivo: implementar el Tetris descrito en `agents` con Python/Tkinter y reescribir `agents` para regirse por ODD + RDD en lugar de SDD.
Rama: `feat/tetris-odd-rdd` (repo aislado en `proyecto2`).
Entrega: `single-pr` local; no hay remoto configurado, así que la rama es la entrega hasta que exista uno.
Runner: `python -m pytest -q` con `.venv/bin/python` (Python 3.12.16, Tk 9.1, customtkinter 6.0.0, pygame 2.6.1).

## Specs

- **S1** Runtime y stack: Python 3.10+; `tkinter` con `Canvas`; `customtkinter` para HUD; `pygame.mixer` para audio; type hints en todo el código; loop con `root.after()` y sin `while True` bloqueante.
- **S2** Tablero de **10 columnas x 20 filas**; detección de colisiones con bordes y con piezas fijadas; al completar una fila se elimina y las superiores bajan.
- **S3** Siete tetrominos `I, J, L, O, S, T, Z` con sus rotaciones correctas y colores de la paleta.
- **S4** Movimiento: izquierda/derecha, bajar suave, caída rápida (hard drop) y rotación. La caída rápida se detiene en la posición más baja válida y no atraviesa piezas.
- **S5** **3 niveles** (1, 2, 3). Se sube de nivel cada **10 líneas**; la velocidad de descenso aumenta con el nivel y el nivel 3 es el máximo.
- **S6** **3 vidas**. Cuando la pieza recién generada no cabe en el tablero se resta una vida. Con **0 vidas** el estado es Game Over definitivo.
- **S7** Puntuación exacta: 1 línea `100 * nivel`; 2 líneas `300 * nivel`; 3 líneas `500 * nivel`; 4 líneas `800 * nivel`; hard drop `+2` por celda descendida; soft drop `+1` por celda. El multiplicador usa el nivel activo antes de la limpieza.
- **S8** Pausa con `P` (congela descenso y música); reanudar con `P`. Reinicio con `R` únicamente en Game Over. En pausa no se aceptan movimientos de pieza; en Game Over solo `R`.
- **S9** Audio: bucle continuo de `assets/sounds/bg_music.ogg` y SFX `move.wav`, `rotate.wav`, `line_clear.wav`, `game_over.wav` con `pygame.mixer`. Si no hay dispositivo de audio o faltan archivos, el juego sigue en silencio y avisa una sola vez por consola.
- **S10** UI con paleta exacta: fondo `#000814`; grid `#001D3D`; borde/glow `#00E0FF` y `#00FFFF`; piezas `#0099FF`, `#00BFFF`, `#33FFFF`; texto `#E6FFFF`; alerta `#FF3366`. Layout `SIGUIENTE | TABLERO | HUD`. Tipografía monoespaciada (`Consolas`, `Courier New`, `JetBrains Mono`). Feedback: highlight al limpiar línea, parpadeo al subir de nivel, overlays `PAUSA` y `GAME OVER`. Textos exactos: `TETRIS`, `SIGUIENTE`, `PUNTOS`, `NIVEL`, `VIDAS`, `LÍNEAS`, `PAUSA`, `GAME OVER`, `R PARA REINICIAR`.
- **S11** Estructura de carpetas: `agents`, `assets/sounds/`, `assets/fonts/`, `src/main.py`, `src/core/{board,game,piece,tetrominos}.py`, `src/ui/{renderer,styles,hud}.py`, `src/utils/{audio,constants}.py`, `src/config.py`, `requirements.txt`; se añaden `tests/`, `requirements-dev.txt` y `odd/tasks/`.
- **S12** Separación UI/lógica: `core/` no importa `tkinter` ni `ui/`; constantes centralizadas; PEP 8; redibujado mínimo del Canvas; sin excepciones silenciadas.
- **S13** `agents` documenta ODD (autorizar, explorar, incertidumbre, clasificar, registrar, implementar, cerrar), tamaño de tarea, `Risk`, test-first y unidades de trabajo; no conserva el plan SDD.
- **S14** `agents` documenta RDD: `gentle-ai review mode enable|disable|status`, assessment por commit con `--base-ref`/`--committed-only`, lectura de `review_due`/`review_due_reason`, consentimiento por candidato y revisión sin autoridad de entrega.
- **S15** Suite `pytest` que cubre tablero, piezas, colisiones, limpieza, puntuación, niveles, vidas, pausa y game over sin abrir ventana.
- **S16** `README.md` con instalación, ejecución, controles, pruebas y evidencia ODD/RDD.
- **S17** Commits Conventional Commits sin `Co-Authored-By` ni atribución de IA.

## Tasks

| ID | Specs | Ruta | Estado | Evidencia |
|---|---|---|---|---|
| T1 | S13, S14, S17 | inline | hecho | `docs: rewrite specification with ODD and RDD workflow` |
| T2 | S1, S3, S11, S12 | inline | hecho | RED: `ModuleNotFoundError: No module named 'src'`. GREEN: 57 tests. `50de9e4`. RDD: `medium`, `under_budget` |
| T3 | S2, S4, S12 | inline | hecho | RED: `ModuleNotFoundError: No module named 'src.core.board'`. GREEN: 74 tests. `b51f318`. RDD: `medium`, `under_budget` |
| T4 | S5, S6, S7, S8 | inline | hecho | RED: `ModuleNotFoundError: No module named 'src.core.game'`. GREEN: 95 tests. `17d1e7e`. RDD: `medium`, `under_budget` |
| T5 | S10, S12 | inline | hecho | `src/ui/{styles,renderer,hud}.py`. 95 tests. |
| T6 | S8, S11 | inline | hecho | input bindings in `src/main.py`. |
| T7 | S9, S11 | inline | hecho | `src/utils/audio.py`. |
| T8 | S15 | inline | hecho | 95 tests, no window. |
| T9 | S16, S1–S17 | inline | hecho | `README.md`. |

Pronóstico de líneas autorizadas: ~1300 (app + tests + docs). Estrategia registrada: `single-pr` local sin remoto.

## Log

- **L1** Petición original (reconstruida desde el checkpoint de sesión porque la compactación descartó el texto literal): «Crea el juego de Tetris descrito en `agents` usando Python/Tkinter dentro de `proyecto2`, y reescribe `agents` para que el flujo de trabajo use ODD y RDD en lugar de SDD.» El resto de requisitos vive en `agents`, que se conserva como fuente de verdad funcional.
- **L2** Decisiones de entorno: Python 3.12.16 en `.venv` del proyecto (3.13/3.14/3.15 no tienen `_tkinter` utilizable y 3.14 rompe `pygame.mixer`); customtkinter 6.0.0 y pygame 2.6.1 verificados con Tk 9.1 y mixer a 44100 Hz. Repositorio git aislado dentro de `proyecto2` para no mezclar el material del repo padre.
- **L3** Restricción de idioma: respuestas al usuario en español neutro; identificadores, comentarios, UI y artefactos técnicos en inglés, salvo los textos de interfaz exigidos por S10 y este documento.
- **L4** Frontera base de RDD: commit `9dab319` (`chore: scaffold python project`). Cada unidad de trabajo se evalúa contra la última frontera revisada.
- **L5** T1 cerrado: `agents` reescrito conservando todos los requisitos y sustituyendo el plan SDD por ODD + RDD; scaffold con `requirements.txt`, `requirements-dev.txt`, `.gitignore` y este documento.
- **L6** T2 y T3 cerrados. T2: RED `ModuleNotFoundError: No module named 'src'`, GREEN 57 tests, commit `50de9e4`, RDD `medium` / `under_budget`. T3: RED `ModuleNotFoundError: No module named 'src.core.board'`, GREEN 74 tests, `compileall` limpio. Dos correcciones de prueba antes de GREEN: el escenario de limpieza colocaba la pieza fuera del tablero y luego solapaba una celda ocupada; se ajustó a ocho celdas fijas en la fila 19 y la `O` en la columna 8.
