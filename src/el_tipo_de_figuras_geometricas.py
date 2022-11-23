# el_tipo_de_figuras_geometricas.oy
# El tipo de figuras geométricas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 24-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Se consideran las figuras geométricas formadas por circulos
# (definidos por su radio) y rectángulos (definidos por su base y su
# altura). El tipo de las figura geométricas se define por
#    @dataclass
#    class Figura:
#        """Figuras geométricas"""
#
#    @dataclass
#    class Circulo(Figura):
#        r: float
#
#    @dataclass
#    class Rect(Figura):
#        x: float
#        y: float
#
# Definir las funciones
#    area     : (Figura) -> float
#    cuadrado : (float) -> Figura
# tales que
# + area(f) es el área de la figura f. Por ejemplo,
#      area(Circulo(1))  ==  3.141592653589793
#      area(Circulo(2))  ==  12.566370614359172
#      area(Rect(2, 5))  ==  10
# + cuadrado(n) es el cuadrado de lado n. Por ejemplo,
#      area(cuadrado(3))  ==  9.0
# ---------------------------------------------------------------------

from dataclasses import dataclass
from math import pi

@dataclass
class Figura:
    """Figuras geométricas"""

@dataclass
class Circulo(Figura):
    r: float

@dataclass
class Rect(Figura):
    x: float
    y: float

def area(f: Figura) -> float:
    match f:
        case Circulo(r):
            return pi * r**2
        case Rect(x, y):
            return x * y
    assert False

def cuadrado(n: float) -> Figura:
    return Rect(n, n)
