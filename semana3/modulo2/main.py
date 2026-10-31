# main.py — Usar el paquete utils

# Forma 1: Importar funciones específicas del paquete
from utils import limpiar_texto, formatear_moneda
# Forma 2: Importar submódulos completos
from utils import numeros
# Forma 3: Importar el paquete completo
import utils

texto = limpiar_texto("  Hola   Mundo  ")
print(texto)  # "hola mundo"

precio = formatear_moneda(1234.5)
print(precio)  # "$1,234.50"


promedio = numeros.calcular_promedio([85, 90, 78, 92])
print(f"Promedio: {promedio}")  # Promedio: 86.25


texto_limpio = utils.limpiar_texto("  Python  ")
print(texto_limpio)  # "python"
