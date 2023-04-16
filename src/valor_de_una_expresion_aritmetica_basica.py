# valor_de_una_expresion_aritmetica_basica.py
# Valor de una expresión aritmética básica.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 5-enero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las expresiones aritméticas básicas]
# (https://bit.ly/43EuWL4), definir la función
#    valor : (Expr) -> int:
# tal que valor(e) es el valor de la expresión aritmética e. Por
# ejemplo,
#    valor(P(C(2), S(C(3), C(7))))  ==  20
# ---------------------------------------------------------------------

from src.expresion_aritmetica_basica import C, Expr, P, S


def valor(e: Expr) -> int:
    match e:
        case C(x):
            return x
        case S(x, y):
            return valor(x) + valor(y)
        case P(x, y):
            return valor(x) * valor(y)
    assert False
