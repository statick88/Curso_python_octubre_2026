"""Revisión estructural docente de la planificación del módulo 0.

Estas pruebas revisan que el documento esté listo para una conversación. No
califican la calidad del razonamiento: esa valoración corresponde a la revisión
oral del docente.
"""

import re
import unittest
from pathlib import Path

SECCIONES_REQUERIDAS = (
    "Problema",
    "Entradas",
    "Salidas",
    "Subproblemas",
    "Pseudocódigo",
    "Alternativas",
    "Justificación",
)
MARCADOR = "[COMPLETA:"


def _leer_plan():
    """Devuelve el plan del estudiante como texto UTF-8."""
    return Path(__file__).with_name("m00_planificador.md").read_text(encoding="utf-8")


def _extraer_secciones(texto):
    """Relaciona cada encabezado requerido con el texto que le sigue."""
    coincidencias = list(re.finditer(r"^## (.+)$", texto, flags=re.MULTILINE))
    secciones = {}
    for indice, coincidencia in enumerate(coincidencias):
        final = (
            coincidencias[indice + 1].start()
            if indice + 1 < len(coincidencias)
            else len(texto)
        )
        secciones[coincidencia.group(1)] = texto[coincidencia.end() : final]
    return secciones


def _contenido_util(texto):
    """Descarta comentarios y marcadores para detectar contenido escrito."""
    sin_comentarios = re.sub(r"<!--.*?-->", "", texto, flags=re.DOTALL)
    sin_marcadores = re.sub(r"\[COMPLETA:.*?\]", "", sin_comentarios)
    return sin_marcadores.strip()


def _elementos_no_vacios(texto):
    """Obtiene elementos Markdown con contenido, sin decidir si son buenos."""
    elementos = []
    for linea in texto.splitlines():
        coincidencia = re.match(r"^\s*[-*]\s+(.*)$", linea)
        if coincidencia and _contenido_util(coincidencia.group(1)):
            elementos.append(coincidencia.group(1))
    return elementos


class TestM00Planificador(unittest.TestCase):
    def setUp(self):
        self.texto = _leer_plan()
        self.secciones = _extraer_secciones(self.texto)
        self.encabezados = tuple(
            re.findall(r"^## (.+)$", self.texto, flags=re.MULTILINE)
        )

    def test_conserva_los_siete_encabezados_requeridos(self):
        self.assertCountEqual(self.encabezados, SECCIONES_REQUERIDAS)

    def test_no_conserva_marcadores_visibles(self):
        self.assertNotIn(MARCADOR, self.texto)

    def test_secciones_y_subproblemas_tienen_contenido(self):
        for seccion in SECCIONES_REQUERIDAS:
            if seccion == "Alternativas":
                continue
            with self.subTest(seccion=seccion):
                self.assertTrue(_contenido_util(self.secciones.get(seccion, "")))
        self.assertGreaterEqual(
            len(_elementos_no_vacios(self.secciones.get("Subproblemas", ""))), 4
        )

    def test_alternativas_tiene_dos_opciones_no_vacias(self):
        self.assertGreaterEqual(
            len(_elementos_no_vacios(self.secciones.get("Alternativas", ""))), 2
        )
