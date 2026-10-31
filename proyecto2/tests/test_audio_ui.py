"""Pruebas deterministas de audio y coordinación visual sin abrir una ventana."""

from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import MagicMock, patch

from src.core.game import GameEvent, GameState
from src.main import App
from src.ui.renderer import Renderer
from src.utils import audio as audio_module


class _MusicaFalsa:
    """Registra llamadas al canal de música sin requerir pygame real."""

    def __init__(self) -> None:
        """Inicializa los registros de reproducción simulada."""
        self.loaded: list[str] = []
        self.play_calls: list[int] = []
        self.pause_calls = 0
        self.unpause_calls = 0
        self.stop_calls = 0

    def load(self, path: str) -> None:
        """Registra el archivo que se cargaría."""
        self.loaded.append(path)

    def set_volume(self, volume: float) -> None:
        """Acepta el volumen configurado sin requerir un dispositivo real."""

    def play(self, loops: int) -> None:
        """Registra el inicio de la reproducción."""
        self.play_calls.append(loops)

    def pause(self) -> None:
        """Registra una pausa de la música."""
        self.pause_calls += 1

    def unpause(self) -> None:
        """Registra una reanudación de la música."""
        self.unpause_calls += 1

    def stop(self) -> None:
        """Registra la detención de la música."""
        self.stop_calls += 1


class _MezcladorFalso:
    """Sustituye al mezclador de pygame en las pruebas sin dispositivo de audio."""

    def __init__(self) -> None:
        """Prepara el canal de música simulado."""
        self.music = _MusicaFalsa()
        self.initialized = 0

    def init(self) -> None:
        """Registra la inicialización del mezclador."""
        self.initialized += 1

    def Sound(self, path: str) -> object:
        """Devuelve un marcador para un efecto de sonido cargado."""
        return object()


class _PygameFalso:
    """Expone solo la parte de pygame utilizada por AudioManager."""

    def __init__(self) -> None:
        """Crea el mezclador falso."""
        self.mixer = _MezcladorFalso()


class _LienzoFalso:
    """Recoge operaciones del Canvas para afirmar feedback sin una interfaz Tk."""

    def __init__(self) -> None:
        """Inicializa el historial de dibujos."""
        self.calls: list[tuple[str, tuple[object, ...], dict[str, object]]] = []

    def __getattr__(self, name: str):
        """Devuelve una función que registra cualquier operación gráfica."""
        def registrar(*args: object, **kwargs: object) -> None:
            """Añade la operación recibida al historial del lienzo falso."""
            self.calls.append((name, args, kwargs))

        return registrar


class AudioManagerTests(unittest.TestCase):
    """Verifica el modo silencioso y el control de pausa con fakes deterministas."""

    def test_advierte_una_vez_las_rutas_absolutas_de_recursos_ausentes(self) -> None:
        """El aviso único enumera recursos faltantes mediante sus rutas absolutas."""
        with TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            paths = {
                "music": root / "bg_music.ogg",
                "move": root / "move.wav",
                "rotate": root / "rotate.wav",
                "line_clear": root / "line_clear.wav",
                "game_over": root / "game_over.wav",
            }
            pygame_falso = _PygameFalso()
            salida = io.StringIO()
            with patch.object(audio_module, "pygame", pygame_falso), patch.object(
                audio_module, "_PYGAME_AVAILABLE", True
            ), redirect_stdout(salida):
                audio_module.AudioManager(audio_paths=paths)

        aviso = salida.getvalue()
        self.assertEqual(aviso.count("Audio sin recursos:"), 1)
        self.assertIn(str(paths["music"]), aviso)
        self.assertIn(str(paths["game_over"]), aviso)

    def test_pausa_y_reanuda_la_musica_iniciada(self) -> None:
        """Pausa y reanuda solo el bucle de música que ya fue iniciado."""
        pygame_falso = _PygameFalso()
        with TemporaryDirectory() as directory:
            music_path = Path(directory, "bg_music.ogg")
            music_path.touch()
            paths = {"music": music_path, "move": Path(directory, "move.wav")}
            with patch.object(audio_module, "pygame", pygame_falso), patch.object(
                audio_module, "_PYGAME_AVAILABLE", True
            ), redirect_stdout(io.StringIO()):
                audio = audio_module.AudioManager(audio_paths=paths)
                audio.play_music()
                audio.pause_music()
                audio.resume_music()

        self.assertEqual(pygame_falso.mixer.music.play_calls, [-1])
        self.assertEqual(pygame_falso.mixer.music.pause_calls, 1)
        self.assertEqual(pygame_falso.mixer.music.unpause_calls, 1)


class AppLayoutTests(unittest.TestCase):
    """Verifica la distribución de paneles sin crear una ventana real."""

    def test_ubica_vista_previa_a_la_izquierda_y_hud_a_la_derecha(self) -> None:
        """El layout separa SIGUIENTE, tablero y HUD en tres columnas."""
        app = object.__new__(App)
        app.root = object()
        hud = MagicMock()
        with patch("src.main.tk.Canvas"), patch("src.main.tk.Label"), patch(
            "src.main.HUD", return_value=hud
        ), patch("src.main.Renderer"):
            app._build_layout()

        hud.next_frame.grid.assert_called_once_with(row=1, column=0, sticky="n", padx=8, pady=8)
        hud.frame.grid.assert_called_once_with(row=1, column=2, sticky="n", padx=8, pady=8)


class AppAudioTests(unittest.TestCase):
    """Verifica que la pausa del juego se propaga al gestor de audio."""

    def test_alternar_pausa_pausa_y_reanuda_la_musica(self) -> None:
        """La tecla de pausa coordina el estado del juego con el bucle de música."""
        class JuegoFalso:
            """Expone una transición de pausa controlada para la aplicación."""

            def __init__(self) -> None:
                """Inicia el juego falso en ejecución."""
                self.state = GameState.PLAYING

            def toggle_pause(self) -> bool:
                """Alterna entre juego activo y pausado."""
                self.state = (
                    GameState.PAUSED
                    if self.state is GameState.PLAYING
                    else GameState.PLAYING
                )
                return True

        class AudioFalso:
            """Registra las órdenes de pausa de la aplicación."""

            def __init__(self) -> None:
                """Inicializa el historial de órdenes de audio."""
                self.calls: list[str] = []

            def pause_music(self) -> None:
                """Registra la pausa solicitada."""
                self.calls.append("pause")

            def resume_music(self) -> None:
                """Registra la reanudación solicitada."""
                self.calls.append("resume")

        app = object.__new__(App)
        app.game = JuegoFalso()
        app.audio = AudioFalso()

        self.assertTrue(app._toggle_pause())
        self.assertTrue(app._toggle_pause())
        self.assertEqual(app.audio.calls, ["pause", "resume"])


class RendererFeedbackTests(unittest.TestCase):
    """Verifica feedback de líneas y nivel a través de un lienzo falso."""

    def test_dibuja_feedback_para_linea_y_subida_de_nivel(self) -> None:
        """Los eventos de línea y nivel generan indicadores visuales visibles."""
        canvas = _LienzoFalso()
        renderer = Renderer(canvas)  # type: ignore[arg-type]

        renderer.notify_events((GameEvent.LINE_CLEAR, GameEvent.LEVEL_UP))
        renderer._draw_feedback(GameState.PLAYING)

        textos = [kwargs.get("text") for name, _, kwargs in canvas.calls if name == "create_text"]
        self.assertIn("LÍNEA COMPLETA", textos)
        self.assertIn("NIVEL SUPERIOR", textos)


if __name__ == "__main__":
    unittest.main()
