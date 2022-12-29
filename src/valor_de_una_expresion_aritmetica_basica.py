# valor_de_una_expresion_aritmetica_basica.py
# Valor de una expresión aritmética básica.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 5-enero-2023
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
#    valor : (Expr) -> int:
# tal que valor(e) es el valor de la expresión aritmética e. Por
# ejemplo,
#    valor(P(C(2), S(C(3), C(7))))  ==  20
# ---------------------------------------------------------------------

from dataclasses import dataclass


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

def valor(e: Expr) -> int:
    match e:
        case C(x):
            return x
        case S(x, y):
            return valor(x) + valor(y)
        case P(x, y):
            return valor(x) * valor(y)
    assert False
