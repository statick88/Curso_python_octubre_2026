"""Constantes del juego Tetris."""
from typing import Tuple

# Tamaño del tablero
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
CELL_SIZE = 30

# Colores estilo hacker
COLORS = {
    'bg': '#000814',
    'grid': '#001D3D',
    'border': '#00E0FF',
    'glow': '#00FFFF',
    'text': '#E6FFFF',
    'alert': '#FF3366',
    'I': '#00FFFF',
    'J': '#0099FF',
    'L': '#00BFFF',
    'O': '#33FFFF',
    'S': '#00E0FF',
    'T': '#1E90FF',
    'Z': '#0066FF',
}

# Configuración del juego
INITIAL_LIVES = 3
MAX_LEVELS = 3
LINES_PER_LEVEL = 10
INITIAL_FALL_SPEED = 500  # ms
FAST_FALL_SPEED = 50  # ms

# Puntos
POINTS = {
    1: 100,
    2: 300,
    3: 500,
    4: 800,
}
SOFT_DROP_POINTS = 1
HARD_DROP_POINTS = 2
