# expresiones_aritmeticas_reducibles.py
# Expresiones aritméticas reducibles.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 14-enero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Las expresiones aritméticas con variables pueden representarse usando
# el siguiente tipo de datos
#    @dataclass
#    class Expr:
#        pass
#
#    @dataclass
#    class C(Expr):
#        x: int
#
#    @dataclass
#    class V(Expr):
#        x: str
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
#
# Por ejemplo, la expresión 2*(a+5) se representa por
#    P(C(2), S(V('a'), C(5)))
#
# Definir la función
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

from dataclasses import dataclass


@dataclass
class Expr:
    pass

@dataclass
class C(Expr):
    x: int

@dataclass
class V(Expr):
    x: str

@dataclass
class S(Expr):
    x: Expr
    y: Expr

@dataclass
class P(Expr):
    x: Expr
    y: Expr

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
