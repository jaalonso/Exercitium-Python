# numero_de_variables_de_una_expresion_aritmetica.py
# Número de variables de una expresión aritmética.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 10-enero-2023.
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las expresiones aritméticas con una variable](https://bit.ly/40mwjeF),
# definir la función
#    numVars : (Expr) -> int
# tal que numVars(e) es el número de variables en la expresión e. Por
# ejemplo,
#    numVars(C(3))                   ==  0
#    numVars(X())                    ==  1
#    numVars(P(X(), S(C(13), X())))  ==  2
# ---------------------------------------------------------------------

from src.expresion_aritmetica_con_una_variable import C, Expr, P, S, X


def numVars(e: Expr) -> int:
    match e:
        case X():
            return 1
        case C(_):
            return 0
        case S(e1, e2):
            return numVars(e1) + numVars(e2)
        case P(e1, e2):
            return numVars(e1) + numVars(e2)
    assert False
