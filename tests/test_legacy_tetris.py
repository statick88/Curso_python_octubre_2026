"""Pruebas de interfaz para la lógica pura del Tetris legado."""

from __future__ import annotations

import ast
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROYECTO = ROOT / "proyecto"
FUENTE = PROYECTO / "src"


def funciones_sin_docstring(ruta: Path) -> list[str]:
    """Devuelve los métodos sin docstring dentro del código legado."""
    arbol = ast.parse(ruta.read_text(encoding="utf-8"), filename=str(ruta))
    faltantes: list[str] = []
    for nodo in ast.walk(arbol):
        if isinstance(nodo, (ast.FunctionDef, ast.AsyncFunctionDef)) and not ast.get_docstring(nodo):
            faltantes.append(f"{ruta.relative_to(ROOT)}:{nodo.name}")
    return faltantes


def ejecutar_logica(codigo: str) -> dict[str, object]:
    """Ejecuta la lógica legado en un proceso sin compartir paquetes src."""
    resultado = subprocess.run(
        [sys.executable, "-c", codigo],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
    )
    if resultado.returncode != 0:
        raise AssertionError(resultado.stderr)
    return json.loads(resultado.stdout)


class TestDocumentacionDelTetrisLegado(unittest.TestCase):
    """Comprueba que la API del miniproyecto conserva documentación útil."""

    def test_todas_las_funciones_tienen_docstrings(self) -> None:
        """Exige docstrings en funciones y métodos del Tetris legado."""
        faltantes = [
            faltante
            for ruta in FUENTE.rglob("*.py")
            for faltante in funciones_sin_docstring(ruta)
        ]
        self.assertEqual(faltantes, [])


class TestLogicaPuraDelTetrisLegado(unittest.TestCase):
    """Comprueba tablero y tetrominos sin iniciar la interfaz gráfica."""

    def test_tetromino_rota_y_recupera_su_forma_inicial(self) -> None:
        """Verifica el ciclo público de rotación de la pieza T."""
        datos = ejecutar_logica(
            "import json, sys; sys.path.insert(0, 'proyecto'); "
            "from src.core.tetrominos import Tetromino; pieza = Tetromino('T'); "
            "inicial = pieza.get_shape(); [pieza.rotate() for _ in range(4)]; "
            "print(json.dumps({'inicial': inicial, 'final': pieza.get_shape(), "
            "'ancho': pieza.get_width(), 'alto': pieza.get_height()}))"
        )
        self.assertEqual(datos["inicial"], datos["final"])
        self.assertEqual((datos["ancho"], datos["alto"]), (3, 2))

    def test_tablero_rechaza_colisiones_y_limpia_una_fila(self) -> None:
        """Verifica colisiones de borde, fijación y limpieza de líneas."""
        datos = ejecutar_logica(
            "import json, sys; sys.path.insert(0, 'proyecto'); "
            "from src.core.board import Board; tablero = Board(); forma = [[1]]; "
            "valida = tablero.is_valid_position(forma, (0, 0)); "
            "tablero.add_piece(forma, (0, 0), '#00FFFF'); "
            "ocupada = tablero.is_valid_position(forma, (0, 0)); "
            "borde = tablero.is_valid_position(forma, (-1, 0)); "
            "tablero.grid[-1] = ['#00FFFF'] * tablero.width; "
            "lineas = tablero.clear_lines(); "
            "print(json.dumps({'valida': valida, 'ocupada': ocupada, 'borde': borde, "
            "'lineas': lineas, 'fila_superior_vacia': tablero.grid[0] == [0] * tablero.width}))"
        )
        self.assertTrue(datos["valida"])
        self.assertFalse(datos["ocupada"])
        self.assertFalse(datos["borde"])
        self.assertEqual(datos["lineas"], 1)
        self.assertTrue(datos["fila_superior_vacia"])


class TestAudioOpcionalDelTetrisLegado(unittest.TestCase):
    """Comprueba que el audio no bloquee la partida y conserve su API pública."""

    def test_audio_no_interrumpe_sin_dispositivo_y_conserva_efectos_normales(self) -> None:
        """Mantiene controles inofensivos sin mezclador y efectos al haberlo."""
        sin_dispositivo = ejecutar_logica(
            "import json, sys, types; "
            "mixer = types.SimpleNamespace(init=lambda: (_ for _ in ()).throw(RuntimeError('sin dispositivo'))); "
            "sys.modules['pygame'] = types.SimpleNamespace(mixer=mixer); "
            "sys.path.insert(0, 'proyecto'); from src.utils import audio; "
            "audio.os.path.exists = lambda ruta: True; gestor = audio.AudioManager(); "
            "gestor.play_music('musica.ogg'); gestor.stop_music(); gestor.pause_music(); "
            "gestor.unpause_music(); gestor.play_sound('efecto.wav'); "
            "print(json.dumps({'reproduciendo': gestor.music_playing}))"
        )
        self.assertFalse(sin_dispositivo["reproduciendo"])

        con_dispositivo = ejecutar_logica(
            "import json, sys, types; llamadas = []; "
            "musica = types.SimpleNamespace(load=lambda ruta: llamadas.append(('load', ruta)), "
            "set_volume=lambda volumen: llamadas.append(('music_volume', volumen)), "
            "play=lambda bucle: llamadas.append(('play', bucle)), stop=lambda: llamadas.append(('stop',)), "
            "pause=lambda: llamadas.append(('pause',)), unpause=lambda: llamadas.append(('unpause',))); "
            "sonido = types.SimpleNamespace(set_volume=lambda volumen: llamadas.append(('sound_volume', volumen)), "
            "play=lambda: llamadas.append(('sound_play',))); "
            "mixer = types.SimpleNamespace(init=lambda: llamadas.append(('init',)), music=musica, "
            "Sound=lambda ruta: llamadas.append(('sound', ruta)) or sonido); "
            "sys.modules['pygame'] = types.SimpleNamespace(mixer=mixer); sys.path.insert(0, 'proyecto'); "
            "from src.utils import audio; audio.os.path.exists = lambda ruta: True; gestor = audio.AudioManager(); "
            "gestor.play_music('musica.ogg'); gestor.pause_music(); gestor.unpause_music(); gestor.stop_music(); "
            "gestor.play_sound('efecto.wav'); print(json.dumps({'llamadas': llamadas, 'reproduciendo': gestor.music_playing}))"
        )
        self.assertEqual(con_dispositivo["llamadas"], [
            ["init"], ["load", "musica.ogg"], ["music_volume", 0.5], ["play", -1],
            ["pause"], ["unpause"], ["stop"], ["sound", "efecto.wav"],
            ["sound_volume", 0.7], ["sound_play"],
        ])
        self.assertFalse(con_dispositivo["reproduciendo"])

    def test_inicio_normal_solicita_musica_de_fondo_una_vez(self) -> None:
        """Inicia una sola vez la música mediante el administrador existente."""
        datos = ejecutar_logica(
            "import json, sys, types; exec(\"class Widget:\\n def __init__(self, *args, **kwargs): pass\\n def grid(self, *args, **kwargs): pass\\n def pack(self, *args, **kwargs): pass\\n def configure(self, *args, **kwargs): pass\\nclass Root:\\n def title(self, *args): pass\\n def configure(self, **kwargs): pass\\n def resizable(self, *args): pass\\n def bind(self, *args): pass\\n def after(self, *args): pass\\nclass Audio:\\n llamadas = []\\n def __init__(self): pass\\n def play_music(self, ruta): self.llamadas.append(ruta)\"); "
            "sys.modules['tkinter'] = types.SimpleNamespace(Canvas=Widget); "
            "sys.modules['customtkinter'] = types.SimpleNamespace(CTkLabel=Widget, CTkFrame=Widget); "
            "sys.modules['src.utils.audio'] = types.SimpleNamespace(AudioManager=Audio); "
            "sys.modules['src.ui.renderer'] = types.SimpleNamespace(Renderer=type('Renderer', (), {'__init__': lambda self, canvas: None, 'clear': lambda self: None, 'draw_grid': lambda self: None, 'draw_board': lambda self, grid: None, 'draw_piece': lambda self, shape, position, color: None})); "
            "sys.path.insert(0, 'proyecto'); from src.main import TetrisGame; TetrisGame(Root()); "
            "print(json.dumps({'llamadas': Audio.llamadas}))"
        )
        self.assertEqual(datos["llamadas"], ["assets/sounds/bg_music.ogg"])


if __name__ == "__main__":
    unittest.main()
