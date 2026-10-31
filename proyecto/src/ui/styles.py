"""Estilos y paleta de colores."""
from src.utils.constants import COLORS

class Styles:
    """Estilos para la interfaz."""
    BG = COLORS['bg']
    GRID = COLORS['grid']
    BORDER = COLORS['border']
    GLOW = COLORS['glow']
    TEXT = COLORS['text']
    ALERT = COLORS['alert']
    PIECE_COLORS = {k: v for k, v in COLORS.items() if k not in ['bg', 'grid', 'border', 'glow', 'text', 'alert']}
