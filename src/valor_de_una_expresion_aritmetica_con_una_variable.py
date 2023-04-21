# valor_de_una_expresion_aritmetica_con_una_variable.py
# Valor de una expresión aritmética con una variable.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 9-enero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las expresiones aritméticas con una variable](https://bit.ly/40mwjeF),
# definir la función
#    valor : (Expr, int) -> int
# tal que valor(e, n) es el valor de la expresión e cuando se
# sustituye su variable por n. Por ejemplo,
#    valor(P(X(), S(C(13), X())), 2)  ==  30
# ---------------------------------------------------------------------

from src.expresion_aritmetica_con_una_variable import C, Expr, P, S, X


def valor(e: Expr, n: int) -> int:
    match e:
        case X():
            return n
        case C(a):
            return a
        case S(e1, e2):
            return valor(e1, n) + valor(e2, n)
        case P(e1, e2):
            return valor(e1, n) * valor(e2, n)
    assert False
