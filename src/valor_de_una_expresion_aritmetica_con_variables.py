# valor_de_una_expresion_aritmetica_con_variables.py
# Valor de una expresión aritmética con variables.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 11-enero-2023.
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las expresiones aritméticas con variables]
# (https://bit.ly/3HfB0QO), definir la función
#    valor : (Expr, list[tuple[str, int]]) -> int
# tal que valor(x, e) es el valor de la expresión x en el entorno e (es
# decir, el valor de la expresión donde las variables de x se sustituyen
# por los valores según se indican en el entorno e). Por ejemplo,
#    λ> valor(P(C(2), S(V('a'), V('b'))), [('a', 2), ('b', 5)])
#    14
# ---------------------------------------------------------------------

from src.expresion_aritmetica_con_variables import C, Expr, P, S, V


def valor(e: Expr, xs: list[tuple[str, int]]) -> int:
    match e:
        case C(a):
            return a
        case V(x):
            return [y for (z, y) in xs if z == x][0]
        case S(e1, e2):
            return valor(e1, xs) + valor(e2, xs)
        case P(e1, e2):
            return valor(e1, xs) * valor(e2, xs)
    assert False
