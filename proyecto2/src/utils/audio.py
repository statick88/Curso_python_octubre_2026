"""Gestor tolerante a fallos para música y efectos de sonido de Tetris."""

from __future__ import annotations

from pathlib import Path
from typing import Mapping

from src.config import (
    BACKGROUND_MUSIC,
    GAME_OVER_SOUND,
    LINE_CLEAR_SOUND,
    MOVE_SOUND,
    MUSIC_VOLUME,
    ROTATE_SOUND,
    SFX_VOLUME,
)

try:
    import pygame

    _PYGAME_AVAILABLE = True
except Exception:  # pragma: no cover - depende de la instalación local
    pygame = None  # type: ignore[assignment]
    _PYGAME_AVAILABLE = False


AudioPaths = Mapping[str, Path]


def default_audio_paths() -> dict[str, Path]:
    """Devuelve las rutas absolutas configuradas para música y efectos."""
    return {
        "music": BACKGROUND_MUSIC,
        "move": MOVE_SOUND,
        "rotate": ROTATE_SOUND,
        "line_clear": LINE_CLEAR_SOUND,
        "game_over": GAME_OVER_SOUND,
    }


class AudioManager:
    """Carga audio opcionalmente y mantiene el juego operativo sin sonido."""

    def __init__(self, audio_paths: AudioPaths | None = None) -> None:
        """Inicializa pygame y carga únicamente los recursos disponibles."""
        self._paths = dict(default_audio_paths() if audio_paths is None else audio_paths)
        self._available = False
        self._warned = False
        self._music_loaded = False
        self._music_started = False
        self._sounds: dict[str, object] = {}
        self._init()

    def _warn_once(self, message: str) -> None:
        """Informa una sola vez de una degradación de audio no bloqueante."""
        if not self._warned:
            print(message)
            self._warned = True

    def _missing_paths(self) -> tuple[Path, ...]:
        """Devuelve los recursos configurados que no existen en el disco."""
        return tuple(path for path in self._paths.values() if not path.exists())

    def _init(self) -> None:
        """Prepara el mezclador y avisa si no puede ofrecer audio completo."""
        if not _PYGAME_AVAILABLE:
            self._warn_once("Audio sin disponibilidad: pygame no está instalado.")
            return
        try:
            pygame.mixer.init()
        except Exception as exc:  # pragma: no cover - depende del dispositivo local
            self._warn_once(f"Audio sin disponibilidad: {exc}")
            return
        self._available = True
        missing = self._missing_paths()
        if missing:
            formatted = ", ".join(str(path.resolve()) for path in missing)
            self._warn_once(f"Audio sin recursos: {formatted}")
        self._load_music()
        self._load_sounds()

    def _load_music(self) -> None:
        """Carga la música de fondo si la ruta configurada está disponible."""
        path = self._paths.get("music")
        if path is None or not path.exists():
            return
        try:
            pygame.mixer.music.load(str(path))
            pygame.mixer.music.set_volume(MUSIC_VOLUME)
        except Exception as exc:  # pragma: no cover - codec y dispositivo locales
            self._warn_once(f"Audio sin disponibilidad: no se pudo cargar {path.resolve()}: {exc}")
            return
        self._music_loaded = True

    def _load_sounds(self) -> None:
        """Carga los efectos disponibles sin impedir el resto de la partida."""
        for name in ("move", "rotate", "line_clear", "game_over"):
            path = self._paths.get(name)
            if path is None or not path.exists():
                continue
            try:
                sound = pygame.mixer.Sound(str(path))
                sound.set_volume(SFX_VOLUME)
            except Exception as exc:  # pragma: no cover - codec y dispositivo locales
                self._warn_once(
                    f"Audio sin disponibilidad: no se pudo cargar {path.resolve()}: {exc}"
                )
                continue
            self._sounds[name] = sound

    def play_music(self) -> None:
        """Inicia el bucle musical cuando la pista fue cargada correctamente."""
        if not self._available or not self._music_loaded:
            return
        try:
            pygame.mixer.music.play(-1)
        except Exception as exc:  # pragma: no cover - dispositivo local
            self._warn_once(f"Audio sin disponibilidad: {exc}")
            return
        self._music_started = True

    def pause_music(self) -> None:
        """Pausa el bucle activo al pausar la partida."""
        if not self._available or not self._music_started:
            return
        try:
            pygame.mixer.music.pause()
        except Exception as exc:  # pragma: no cover - dispositivo local
            self._warn_once(f"Audio sin disponibilidad: {exc}")

    def resume_music(self) -> None:
        """Reanuda el bucle activo al continuar una partida pausada."""
        if not self._available or not self._music_started:
            return
        try:
            pygame.mixer.music.unpause()
        except Exception as exc:  # pragma: no cover - dispositivo local
            self._warn_once(f"Audio sin disponibilidad: {exc}")

    def stop_music(self) -> None:
        """Detiene la música de fondo al finalizar la partida."""
        if not self._available or not self._music_started:
            return
        try:
            pygame.mixer.music.stop()
        except Exception as exc:  # pragma: no cover - dispositivo local
            self._warn_once(f"Audio sin disponibilidad: {exc}")
        self._music_started = False

    def play_sfx(self, name: str) -> None:
        """Reproduce un efecto cargado sin fallar si el recurso no está disponible."""
        if not self._available:
            return
        sound = self._sounds.get(name)
        if sound is None:
            return
        try:
            sound.play()  # type: ignore[union-attr]
        except Exception as exc:  # pragma: no cover - dispositivo local
            self._warn_once(f"Audio sin disponibilidad: {exc}")
