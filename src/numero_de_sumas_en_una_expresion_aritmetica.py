# numero_de_sumas_en_una_expresion_aritmetica.py
# Número de sumas en una expresión aritmética.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 12-enero-2023
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
#    sumas : (Expr) -> int
# tal que sumas(e) es el número de sumas en la expresión e. Por
# ejemplo,
#    sumas(P(V('z'), S(C(3), V('x')))) == 1
#    sumas(S(V('z'), S(C(3), V('x')))) == 2
#    sumas(P(V('z'), P(C(3), V('x')))) == 0
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

def sumas(e: Expr) -> int:
    match e:
        case C(_):
            return 0
        case V(_):
            return 0
        case S(e1, e2):
            return 1 + sumas(e1) + sumas(e2)
        case P(e1, e2):
            return sumas(e1) + sumas(e2)
    assert False
