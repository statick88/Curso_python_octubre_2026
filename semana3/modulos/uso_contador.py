# uso_contador.py
from contador import registrar_accion, obtener_total

registrar_accion("Inicio de sesión")  # [1] Inicio de sesión
registrar_accion("Archivo guardado")  # [2] Archivo guardado
registrar_accion("Email enviado")
print(f"Total: {obtener_total()}")    # Total: 2