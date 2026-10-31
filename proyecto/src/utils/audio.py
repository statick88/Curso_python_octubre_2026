"""Gestor de audio."""
import pygame
import os

class AudioManager:
    """Gestiona música y efectos de sonido."""
    def __init__(self):
        """Inicializa el mezclador de audio y el estado de reproducción."""
        self.music_playing = False
        try:
            pygame.mixer.init()
        except Exception:
            self.available = False
        else:
            self.available = True

    def play_music(self, music_path: str, volume: float = 0.5):
        """Reproduce música de fondo en loop."""
        if self.available and os.path.exists(music_path):
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(-1)
            self.music_playing = True

    def stop_music(self):
        """Detiene la música."""
        if self.available:
            pygame.mixer.music.stop()
        self.music_playing = False

    def pause_music(self):
        """Pausa la música."""
        if self.available:
            pygame.mixer.music.pause()

    def unpause_music(self):
        """Reanuda la música."""
        if self.available:
            pygame.mixer.music.unpause()

    def play_sound(self, sound_path: str, volume: float = 0.7):
        """Reproduce un efecto de sonido."""
        if self.available and os.path.exists(sound_path):
            sound = pygame.mixer.Sound(sound_path)
            sound.set_volume(volume)
            sound.play()
