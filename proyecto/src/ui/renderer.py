"""Renderizador del juego."""
import tkinter as tk
from src.utils.constants import BOARD_WIDTH, BOARD_HEIGHT, CELL_SIZE, COLORS

class Renderer:
    """Encargado de renderizar el juego en el Canvas."""
    def __init__(self, canvas: tk.Canvas):
        """Asocia el renderizador con el canvas que recibirá los dibujos."""
        self.canvas = canvas
        self.cell_size = CELL_SIZE

    def draw_grid(self):
        """Dibuja la cuadrícula del tablero."""
        self.canvas.delete("grid")
        for x in range(BOARD_WIDTH + 1):
            self.canvas.create_line(
                x * self.cell_size, 0,
                x * self.cell_size, BOARD_HEIGHT * self.cell_size,
                fill=COLORS['grid'], tags="grid"
            )
        for y in range(BOARD_HEIGHT + 1):
            self.canvas.create_line(
                0, y * self.cell_size,
                BOARD_WIDTH * self.cell_size, y * self.cell_size,
                fill=COLORS['grid'], tags="grid"
            )

    def draw_board(self, grid):
        """Dibuja el tablero con las piezas ya colocadas."""
        self.canvas.delete("board")
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                if grid[y][x] != 0:
                    color = grid[y][x] if isinstance(grid[y][x], str) else COLORS.get(grid[y][x], COLORS['glow'])
                    self.canvas.create_rectangle(
                        x * self.cell_size + 1, y * self.cell_size + 1,
                        (x + 1) * self.cell_size - 1, (y + 1) * self.cell_size - 1,
                        fill=color, outline=COLORS['border'], tags="board"
                    )

    def draw_piece(self, shape, offset, color):
        """Dibuja la pieza activa."""
        self.canvas.delete("piece")
        off_x, off_y = offset
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    px = (off_x + x) * self.cell_size
                    py = (off_y + y) * self.cell_size
                    if 0 <= off_x + x < BOARD_WIDTH and 0 <= off_y + y < BOARD_HEIGHT:
                        self.canvas.create_rectangle(
                            px + 1, py + 1,
                            px + self.cell_size - 1, py + self.cell_size - 1,
                            fill=color, outline=COLORS['glow'], tags="piece"
                        )

    def clear(self):
        """Limpia todos los elementos."""
        self.canvas.delete("all")
