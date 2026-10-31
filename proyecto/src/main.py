"""Punto de entrada del juego Tetris."""
import tkinter as tk
import customtkinter as ctk
from src.utils.constants import BOARD_WIDTH, BOARD_HEIGHT, CELL_SIZE, COLORS, INITIAL_LIVES, MAX_LEVELS
from src.core.board import Board
from src.core.tetrominos import Tetromino, TETROMINOS
from src.ui.renderer import Renderer
from src.utils.audio import AudioManager
import random

class TetrisGame:
    """Controlador principal del juego."""
    def __init__(self, root):
        """Inicializa el estado, la interfaz y el bucle de una partida."""
        self.root = root
        self.root.title("Tetris - Hacker Style")
        self.root.configure(bg=COLORS['bg'])
        self.root.resizable(False, False)

        # Configuración
        self.board = Board()
        self.renderer = None
        self.audio = AudioManager()

        # Estado del juego
        self.score = 0
        self.level = 1
        self.lives = INITIAL_LIVES
        self.lines_cleared_total = 0
        self.game_over = False
        self.paused = False

        # Pieza actual
        self.current_piece = None
        self.current_x = 0
        self.current_y = 0
        self.current_color = COLORS['glow']

        # Velocidad
        self.fall_speed = 500

        self.setup_ui()
        self.new_piece()
        self.bind_keys()
        self.game_loop()

    def setup_ui(self):
        """Configura la interfaz de usuario."""
        # Título
        title = ctk.CTkLabel(self.root, text="TETRIS", font=("Consolas", 24, "bold"),
                            text_color=COLORS['glow'])
        title.grid(row=0, column=0, columnspan=3, pady=10)

        # Canvas del tablero
        self.canvas = tk.Canvas(self.root, width=BOARD_WIDTH*CELL_SIZE,
                               height=BOARD_HEIGHT*CELL_SIZE,
                               bg=COLORS['bg'], highlightthickness=2,
                               highlightbackground=COLORS['border'])
        self.canvas.grid(row=1, column=1, padx=10)
        self.renderer = Renderer(self.canvas)

        # Panel izquierdo - Siguiente pieza
        left_frame = ctk.CTkFrame(self.root, fg_color=COLORS['bg'],
                                 border_width=2, border_color=COLORS['border'])
        left_frame.grid(row=1, column=0, padx=10, sticky="nsew")
        ctk.CTkLabel(left_frame, text="SIGUIENTE", font=("Consolas", 12),
                    text_color=COLORS['text']).pack(pady=5)

        # Panel derecho - HUD
        right_frame = ctk.CTkFrame(self.root, fg_color=COLORS['bg'],
                                  border_width=2, border_color=COLORS['border'])
        right_frame.grid(row=1, column=2, padx=10, sticky="nsew")

        ctk.CTkLabel(right_frame, text="PUNTUACIÓN", font=("Consolas", 12),
                    text_color=COLORS['text']).pack(pady=(10,0))
        self.score_label = ctk.CTkLabel(right_frame, text="0", font=("Consolas", 14, "bold"),
                                       text_color=COLORS['glow'])
        self.score_label.pack()

        ctk.CTkLabel(right_frame, text="NIVEL", font=("Consolas", 12),
                    text_color=COLORS['text']).pack(pady=(10,0))
        self.level_label = ctk.CTkLabel(right_frame, text=f"{self.level}/3", font=("Consolas", 14, "bold"),
                                       text_color=COLORS['glow'])
        self.level_label.pack()

        ctk.CTkLabel(right_frame, text="VIDAS", font=("Consolas", 12),
                    text_color=COLORS['text']).pack(pady=(10,0))
        self.lives_label = ctk.CTkLabel(right_frame, text="♥" * self.lives, font=("Consolas", 14, "bold"),
                                       text_color=COLORS['alert'])
        self.lives_label.pack()

        ctk.CTkLabel(right_frame, text="CONTROLES", font=("Consolas", 10),
                    text_color=COLORS['text']).pack(pady=(20,0))
        controls = "← → Mover\n↑ Rotar\n↓ Bajar\nESPACIO Caída\nP Pausar\nR Reiniciar"
        ctk.CTkLabel(right_frame, text=controls, font=("Consolas", 8),
                    text_color=COLORS['text'], justify="left").pack(pady=5)

    def bind_keys(self):
        """Vincula las teclas."""
        self.root.bind('<Left>', lambda e: self.move(-1, 0))
        self.root.bind('<Right>', lambda e: self.move(1, 0))
        self.root.bind('<Down>', lambda e: self.move(0, 1))
        self.root.bind('<Up>', lambda e: self.rotate())
        self.root.bind('<space>', lambda e: self.hard_drop())
        self.root.bind('p', lambda e: self.toggle_pause())
        self.root.bind('P', lambda e: self.toggle_pause())
        self.root.bind('r', lambda e: self.restart())
        self.root.bind('R', lambda e: self.restart())

    def new_piece(self):
        """Genera una nueva pieza."""
        shape_key = random.choice(list(TETROMINOS.keys()))
        self.current_piece = Tetromino(shape_key)
        self.current_x = BOARD_WIDTH // 2 - self.current_piece.get_width() // 2
        self.current_y = 0
        self.current_color = random.choice([COLORS['I'], COLORS['J'], COLORS['L'],
                                           COLORS['O'], COLORS['S'], COLORS['T'], COLORS['Z']])

        if not self.board.is_valid_position(self.current_piece.get_shape(), (self.current_x, self.current_y)):
            self.lives -= 1
            self.update_hud()
            if self.lives <= 0:
                self.game_over = True
            else:
                self.board = Board()
                self.new_piece()

    def move(self, dx, dy):
        """Mueve la pieza."""
        if self.game_over or self.paused:
            return
        if self.board.is_valid_position(self.current_piece.get_shape(), (self.current_x + dx, self.current_y + dy)):
            self.current_x += dx
            self.current_y += dy
            self.draw()

    def rotate(self):
        """Rota la pieza."""
        if self.game_over or self.paused:
            return
        old_rotation = self.current_piece.rotation
        self.current_piece.rotate()
        if not self.board.is_valid_position(self.current_piece.get_shape(), (self.current_x, self.current_y)):
            self.current_piece.rotation = old_rotation
        self.draw()

    def hard_drop(self):
        """Caída rápida."""
        if self.game_over or self.paused:
            return
        while self.board.is_valid_position(self.current_piece.get_shape(), (self.current_x, self.current_y + 1)):
            self.current_y += 1
        self.place_piece()

    def place_piece(self):
        """Coloca la pieza en el tablero."""
        self.board.add_piece(self.current_piece.get_shape(), (self.current_x, self.current_y), self.current_color)
        lines = self.board.clear_lines()
        if lines > 0:
            self.lines_cleared_total += lines
            self.score += self.calculate_points(lines)
            self.check_level_up()
        self.new_piece()
        self.update_hud()
        self.draw()

    def calculate_points(self, lines):
        """Calcula puntos por líneas."""
        base = {1: 100, 2: 300, 3: 500, 4: 800}.get(lines, 0)
        return base * self.level

    def check_level_up(self):
        """Verifica si sube de nivel."""
        if self.lines_cleared_total >= self.level * 10 and self.level < MAX_LEVELS:
            self.level += 1
            self.fall_speed = max(100, 500 - (self.level - 1) * 150)

    def toggle_pause(self):
        """Pausa/Reanuda el juego."""
        if not self.game_over:
            self.paused = not self.paused

    def restart(self):
        """Reinicia el juego."""
        if self.game_over:
            self.board = Board()
            self.score = 0
            self.level = 1
            self.lives = INITIAL_LIVES
            self.lines_cleared_total = 0
            self.fall_speed = 500
            self.game_over = False
            self.paused = False
            self.new_piece()
            self.update_hud()
            self.draw()

    def update_hud(self):
        """Actualiza el HUD."""
        self.score_label.configure(text=str(self.score))
        self.level_label.configure(text=f"{self.level}/3")
        self.lives_label.configure(text="♥" * self.lives)

    def draw(self):
        """Dibuja todo."""
        self.renderer.clear()
        self.renderer.draw_grid()
        self.renderer.draw_board(self.board.grid)
        if not self.game_over:
            self.renderer.draw_piece(self.current_piece.get_shape(),
                                    (self.current_x, self.current_y),
                                    self.current_color)

    def game_loop(self):
        """Bucle principal del juego."""
        if not self.game_over and not self.paused:
            if self.board.is_valid_position(self.current_piece.get_shape(), (self.current_x, self.current_y + 1)):
                self.current_y += 1
            else:
                self.place_piece()
            self.draw()
        self.root.after(self.fall_speed, self.game_loop)

def main():
    """Crea la ventana de Tetris e inicia el ciclo de eventos gráfico."""
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    root.geometry("650x650")
    game = TetrisGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
