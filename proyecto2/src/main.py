"""Punto de entrada de la aplicación de escritorio Tetris."""

from __future__ import annotations

import os
import sys
from collections.abc import Callable

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk

from src.core.game import Game, GameEvent, GameState
from src.ui.hud import HUD
from src.ui.renderer import Renderer
from src.utils.audio import AudioManager
from src.utils.constants import CANVAS_HEIGHT, CANVAS_WIDTH


class App:
    """Coordina interfaz Tk, reglas puras, audio y programación del bucle."""

    def __init__(self) -> None:
        """Crea la ventana, los colaboradores y el primer tick programado."""
        self.root = tk.Tk()
        self.root.title("TETRIS")
        self.root.configure(bg="#000814")
        self.game = Game()
        self.audio = AudioManager()
        self._build_layout()
        self._bind_keys()
        self._schedule_tick()

    def _build_layout(self) -> None:
        """Construye título, tablero y panel lateral sin duplicar reglas de juego."""
        self.canvas = tk.Canvas(
            self.root,
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT,
            bg="#000814",
            highlightthickness=0,
        )
        self.canvas.grid(row=1, column=1, padx=8, pady=8)
        self.renderer = Renderer(self.canvas)
        self.hud = HUD(self.root)
        self.hud.next_frame.grid(row=1, column=0, sticky="n", padx=8, pady=8)
        self.hud.frame.grid(row=1, column=2, sticky="n", padx=8, pady=8)
        title = tk.Label(
            self.root,
            text="TETRIS",
            fg="#00FFFF",
            bg="#000814",
            font=("Consolas", 24, "bold"),
        )
        title.grid(row=0, column=0, columnspan=3, pady=(8, 4))

    def _bind_keys(self) -> None:
        """Asocia teclas a las acciones admitidas por el controlador de juego."""
        self.root.bind("<Left>", lambda _e: self._act(self.game.move_left, "move"))
        self.root.bind("<Right>", lambda _e: self._act(self.game.move_right, "move"))
        self.root.bind("<Down>", lambda _e: self._act(self.game.soft_drop, "soft_drop"))
        self.root.bind("<Up>", lambda _e: self._act(self.game.rotate, "rotate"))
        self.root.bind("<space>", lambda _e: self._handle_hard_drop())
        self.root.bind("p", lambda _e: self._toggle_pause())
        self.root.bind("P", lambda _e: self._toggle_pause())
        self.root.bind("r", lambda _e: self._restart())
        self.root.bind("R", lambda _e: self._restart())

    def _act(self, action: Callable[[], bool], sfx: str) -> None:
        """Ejecuta una acción de pieza y reproduce su efecto cuando tuvo éxito."""
        if action():
            self.audio.play_sfx("move" if sfx == "soft_drop" else sfx)

    def _handle_hard_drop(self) -> None:
        """Procesa la caída rápida y su feedback si la partida sigue activa."""
        distance = self.game.hard_drop()
        if distance >= 0 and self.game.state is GameState.PLAYING:
            self.audio.play_sfx("move")
        self._process_events(self.game.drain_events())

    def _toggle_pause(self) -> bool:
        """Alterna pausa de reglas y música únicamente cuando el juego lo permite."""
        if not self.game.toggle_pause():
            return False
        if self.game.state is GameState.PAUSED:
            self.audio.pause_music()
        else:
            self.audio.resume_music()
        return True

    def _restart(self) -> bool:
        """Reinicia desde Game Over y vuelve a iniciar la música si procede."""
        restarted = self.game.restart()
        if restarted:
            self.audio.play_music()
        return restarted

    def _schedule_tick(self) -> None:
        """Programa el siguiente tick respetando la velocidad del nivel actual."""
        self.root.after(self.game.drop_interval_ms, self._tick)

    def _process_events(self, events: tuple[GameEvent, ...]) -> None:
        """Entrega eventos de reglas a renderer y audio sin alterar el modelo."""
        self.renderer.notify_events(events)
        for event in events:
            if event is GameEvent.LINE_CLEAR:
                self.audio.play_sfx("line_clear")
            elif event is GameEvent.GAME_OVER:
                self.audio.play_sfx("game_over")
                self.audio.stop_music()

    def _tick(self) -> None:
        """Avanza gravedad, consume feedback y solicita un redibujado no bloqueante."""
        if self.game.state is GameState.PLAYING:
            self.game.tick()
        self._process_events(self.game.drain_events())
        self.renderer.draw(self.game)
        self.hud.update(self.game)
        self._schedule_tick()

    def run(self) -> None:
        """Inicia música opcional y entra en el bucle principal de Tk."""
        self.audio.play_music()
        self.root.mainloop()


def main() -> None:
    """Construye y ejecuta la aplicación interactiva."""
    App().run()


if __name__ == "__main__":
    main()
