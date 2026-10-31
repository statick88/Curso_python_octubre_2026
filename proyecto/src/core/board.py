"""Lógica del tablero de Tetris."""
from typing import List, Tuple
from src.utils.constants import BOARD_WIDTH, BOARD_HEIGHT

class Board:
    """Representa el tablero del juego."""
    def __init__(self):
        """Inicializa una cuadrícula vacía con las dimensiones configuradas."""
        self.width = BOARD_WIDTH
        self.height = BOARD_HEIGHT
        self.grid: List[List] = [[0 for _ in range(self.width)] for _ in range(self.height)]

    def is_valid_position(self, shape: List[List[int]], offset: Tuple[int, int]) -> bool:
        """Verifica si una pieza puede colocarse en una posición."""
        off_x, off_y = offset
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = x + off_x
                    new_y = y + off_y
                    if new_x < 0 or new_x >= self.width or new_y >= self.height:
                        return False
                    if new_y >= 0 and self.grid[new_y][new_x] != 0:
                        return False
        return True

    def add_piece(self, shape: List[List[int]], offset: Tuple[int, int], color: str):
        """Añade una pieza ya validada al tablero con el color indicado."""
        off_x, off_y = offset
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    if off_y + y >= 0:
                        self.grid[off_y + y][off_x + x] = color

    def clear_lines(self) -> int:
        """Limpia líneas completas y retorna el número de líneas limpiadas."""
        new_grid = []
        lines_cleared = 0
        for row in self.grid:
            if all(cell != 0 for cell in row):
                lines_cleared += 1
            else:
                new_grid.append(row)
        # Añadir filas vacías al inicio
        while len(new_grid) < self.height:
            new_grid.insert(0, [0 for _ in range(self.width)])
        self.grid = new_grid
        return lines_cleared

    def is_game_over(self) -> bool:
        """Verifica si hay piezas en la fila superior."""
        for cell in self.grid[0]:
            if cell != 0:
                return True
        return False
