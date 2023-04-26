# expresiones_aritmeticas_reducibles.py
# Expresiones aritméticas reducibles.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 14-enero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las expresiones aritméticas con variables]
# (https://bit.ly/3HfB0QO), definir la función
#    reducible : (Expr) -> bool
# tal que reducible(a) se verifica si a es una expresión reducible; es
# decir, contiene una operación en la que los dos operandos son números.
# Por ejemplo,
#    reducible(S(C(3), C(4)))            == True
#    reducible(S(C(3), V('x')))          == False
#    reducible(S(C(3), P(C(4), C(5))))   == True
#    reducible(S(V('x'), P(C(4), C(5)))) == True
#    reducible(S(C(3), P(V('x'), C(5)))) == False
#    reducible(C(3))                     == False
#    reducible(V('x'))                   == False
# ---------------------------------------------------------------------

from src.expresion_aritmetica_con_variables import C, Expr, P, S, V


def reducible(e: Expr) -> bool:
    match e:
        case C(_):
            return False
        case V(_):
            return False
        case S(C(_), C(_)):
            return True
        case S(a, b):
            return reducible(a) or reducible(b)
        case P(C(_), C(_)):
            return True
        case P(a, b):
            return reducible(a) or reducible(b)
    assert False
