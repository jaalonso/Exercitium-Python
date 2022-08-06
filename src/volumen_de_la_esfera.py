# Volumen_de_la_esfera.py
# Volumen de la esfera.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 10-agosto-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    volumenEsfera : (float) -> float
# tal que volumenEsfera(r) es el volumen de la esfera de radio r. Por
# ejemplo,
#    volumenEsfera(10)  ==  4188.790204786391
# ---------------------------------------------------------------------

from math import pi


def volumenEsfera(r):
    return (4 / 3) * pi * r ** 3
