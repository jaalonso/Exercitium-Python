# aplicacion_de_una_funcion_a_una_expresion_aritmetica.py
# Aplicación de una función a una expresión aritmética.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 6-enero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las expresiones aritméticas básicas]
# (https://bit.ly/43EuWL4), definir la función
#    aplica : (Callable[[int], int], Expr) -> Expr
# tal que aplica(f, e) es la expresión obtenida aplicando la función f
# a cada uno de los números de la expresión e. Por ejemplo,
#    >>> aplica(lambda x: 2 + x, S(P(C(3), C(5)), P(C(6), C(7))))
#    S(P(C(5), C(7)), P(C(8), C(9)))
#    >>> aplica(lambda x: 2 * x, S(P(C(3), C(5)), P(C(6), C(7))))
#    S(P(C(6), C(10)), P(C(12), C(14)))
# ---------------------------------------------------------------------

from typing import Callable

from src.expresion_aritmetica_basica import C, Expr, P, S


def aplica(f: Callable[[int], int], e: Expr) -> Expr:
    match e:
        case C(x):
            return C(f(x))
        case S(x, y):
            return S(aplica(f, x), aplica(f, y))
        case P(x, y):
            return P(aplica(f, x), aplica(f, y))
    assert False
