# maximos_valores_de_una_expresion_aritmetica.py
# Máximos valores de una expresión aritmética.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 17-enero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Las expresiones aritméticas generales se pueden definir usando el
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
#    class X(Expr):
#        pass
#
#    @dataclass
#    class S(Expr):
#        x: Expr
#        y: Expr
#
#    @dataclass
#    class R(Expr):
#        x: Expr
#        y: Expr
#
#    @dataclass
#    class P(Expr):
#        x: Expr
#        y: Expr
#
#    @dataclass
#    class E(Expr):
#        x: Expr
#        y: int
# Por ejemplo, la expresión
#    3*x - (x+2)^7
# se puede definir por
#    R(P(C(3), X()), E(S(X(), C(2)), 7))
#
# Definir la función
#    maximo : (Expr, list[int]) -> tuple[int, list[int]]
# tal que maximo(e, xs) es el par formado por el máximo valor de la
# expresión e para los puntos de xs y en qué puntos alcanza el
# máximo. Por ejemplo,
#    >>> maximo(E(S(C(10), P(R(C(1), X()), X())), 2), range(-3, 4))
#    (100, [0, 1])
# ---------------------------------------------------------------------

from dataclasses import dataclass


@dataclass
class Expr:
    pass

@dataclass
class C(Expr):
    x: int

@dataclass
class X(Expr):
    pass

@dataclass
class S(Expr):
    x: Expr
    y: Expr

@dataclass
class R(Expr):
    x: Expr
    y: Expr

@dataclass
class P(Expr):
    x: Expr
    y: Expr

@dataclass
class E(Expr):
    x: Expr
    y: int

def valor(e: Expr, n: int) -> int:
    match e:
        case C(a):
            return a
        case X():
            return n
        case S(e1, e2):
            return valor(e1, n) + valor(e2, n)
        case R(e1, e2):
            return valor(e1, n) - valor(e2, n)
        case P(e1, e2):
            return valor(e1, n) * valor(e2, n)
        case E(e1, m):
            return valor(e1, n) ** m
    assert False

def maximo(e: Expr, ns: list[int]) -> tuple[int, list[int]]:
    m = max((valor(e, n) for n in ns))
    return (m, [n for n in ns if valor(e, n) == m])
