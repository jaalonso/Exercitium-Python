# aplicacion_de_una_funcion_a_una_expresion_aritmetica.py
# Aplicación de una función a una expresión aritmética.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 6-enero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Las expresiones aritméticas básicas pueden representarse usando el
# siguiente tipo de datos
#    @dataclass
#    class Expr:
#        pass
#
#    @dataclass
#    class C(Expr):
#        x: int
#
#    @dataclass
#    class S(Expr):
#        x: Expr
#        y: Expr
#
#    @dataclass
#    class P(Expr):
#        x: Expr
#        y: Expr
# Por ejemplo, la expresión 2*(3+7) se representa por
#    P(C(2), S(C(3), C(7)))
#
# Definir la función
#    aplica : (Callable[[int], int], Expr) -> Expr
# tal que aplica(f, e) es la expresión obtenida aplicando la función f
# a cada uno de los números de la expresión e. Por ejemplo,
#    >>> aplica(lambda x: 2 + x, S(P(C(3), C(5)), P(C(6), C(7))))
#    S(P(C(5), C(7)), P(C(8), C(9)))
#    >>> aplica(lambda x: 2 * x, S(P(C(3), C(5)), P(C(6), C(7))))
#    S(P(C(6), C(10)), P(C(12), C(14)))
# ---------------------------------------------------------------------

from dataclasses import dataclass
from typing import Callable


@dataclass
class Expr:
    pass

@dataclass
class C(Expr):
    x: int

@dataclass
class S(Expr):
    x: Expr
    y: Expr

@dataclass
class P(Expr):
    x: Expr
    y: Expr

def aplica(f: Callable[[int], int], e: Expr) -> Expr:
    match e:
        case C(x):
            return C(f(x))
        case S(x, y):
            return S(aplica(f, x), aplica(f, y))
        case P(x, y):
            return P(aplica(f, x), aplica(f, y))
    assert False
