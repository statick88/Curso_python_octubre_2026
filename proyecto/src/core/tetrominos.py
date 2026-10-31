"""Definición de las piezas Tetromino."""
from typing import List
import copy

TETROMINOS = {
    'I': [
        [[1,1,1,1]],
        [[1],[1],[1],[1]]
    ],
    'J': [
        [[1,0,0],[1,1,1]],
        [[1,1],[1,0],[1,0]],
        [[1,1,1],[0,0,1]],
        [[0,1],[0,1],[1,1]]
    ],
    'L': [
        [[0,0,1],[1,1,1]],
        [[1,0],[1,0],[1,1]],
        [[1,1,1],[1,0,0]],
        [[1,1],[0,1],[0,1]]
    ],
    'O': [
        [[1,1],[1,1]]
    ],
    'S': [
        [[0,1,1],[1,1,0]],
        [[1,0],[1,1],[0,1]]
    ],
    'T': [
        [[0,1,0],[1,1,1]],
        [[1,0],[1,1],[1,0]],
        [[1,1,1],[0,1,0]],
        [[0,1],[1,1],[0,1]]
    ],
    'Z': [
        [[1,1,0],[0,1,1]],
        [[0,1],[1,1],[1,0]]
    ]
}

class Tetromino:
    """Representa un tipo de tetromino."""
    def __init__(self, shape_key: str):
        """Crea un tetromino en su primera rotación para la clave indicada."""
        self.shape_key = shape_key
        self.shapes = TETROMINOS[shape_key]
        self.rotation = 0

    def get_shape(self):
        """Devuelve la matriz de celdas de la rotación actual."""
        return self.shapes[self.rotation % len(self.shapes)]

    def rotate(self):
        """Avanza una rotación y vuelve al inicio al terminar el ciclo."""
        self.rotation = (self.rotation + 1) % len(self.shapes)

    def get_width(self):
        """Devuelve el ancho de la matriz de la rotación actual."""
        shape = self.get_shape()
        return len(shape[0]) if shape else 0

    def get_height(self):
        """Devuelve la altura de la matriz de la rotación actual."""
        shape = self.get_shape()
        return len(shape) if shape else 0
