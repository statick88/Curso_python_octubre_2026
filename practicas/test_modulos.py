"""Agrega las prácticas por módulo sin cambiar los comandos globales docentes."""

import unittest
from pathlib import Path


def load_tests(loader, suite, pattern):
    """Descubre cada carpeta con un cargador independiente y el mismo filtro."""
    base = Path(__file__).resolve().parent
    for carpeta in sorted(base.glob("modulo-[0-9][0-9]")):
        cargador = unittest.TestLoader()
        cargador.testNamePatterns = loader.testNamePatterns
        cargador.testMethodPrefix = loader.testMethodPrefix
        cargador.sortTestMethodsUsing = loader.sortTestMethodsUsing
        cargador.suiteClass = loader.suiteClass
        suite.addTests(
            cargador.discover(
                start_dir=str(carpeta),
                pattern=pattern or "test_m*.py",
                top_level_dir=str(carpeta),
            )
        )
    return suite
