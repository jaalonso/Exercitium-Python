# distancia_entre_dos_puntos.py
# Distancia entre dos puntos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 6-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    distancia : (tuple[float, float], tuple[float, float]) -> float
# tal que distancia(p1, p2) es la distancia entre los puntos p1 y
# p2. Por ejemplo,
#    distancia((1, 2), (4, 6)) == 5.0
# ---------------------------------------------------------------------

from math import sqrt


def distancia(p1, p2):
    # type: (tuple[float, float], tuple[float, float]) -> float
    (x1, y1) = p1
    (x2, y2) = p2
    return sqrt((x1-x2)**2+(y1-y2)**2)
