# sustitucion_en_una_expresion_aritmetica.py
# Sustitución en una expresión aritmética.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 13-enero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Las expresiones aritméticas con variables pueden representarse usando
# el siguiente tipo de datos
#    data Expr = C Int
#              | V Char
#              | S Expr Expr
#              | P Expr Expr
#      deriving (Eq, Show)
# Por ejemplo, la expresión 2*(a+5) se representa por
#    P (C 2) (S (V 'a') (C 5))
#
# Definir la función
#    sustitucion : (Expr, list[tuple[str, int]]) -> Expr
# tal que sustitucion(e s) es la expresión obtenida sustituyendo las
# variables de la expresión e según se indica en la sustitución s. Por
# ejemplo,
#    >>> sustitucion(P(V('z'), S(C(3), V('x'))), [('x', 7), ('z', 9)])
#    P(C(9), S(C(3), C(7)))
#    >>> sustitucion(P(V('z'), S(C(3), V('y'))), [('x', 7), ('z', 9)])
#    P(C(9), S(C(3), V('y')))
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

def sustitucion(e: Expr, ps: list[tuple[str, int]]) -> Expr:
    match (e, ps):
        case(e, []):
            return e
        case (V(c), ps):
            if c == ps[0][0]:
                return C(ps[0][1])
            return sustitucion(V(c), ps[1:])
        case (C(n), _):
            return C(n)
        case (S(e1, e2), ps):
            return S(sustitucion(e1, ps), sustitucion(e2, ps))
        case (P(e1, e2), ps):
            return P(sustitucion(e1, ps), sustitucion(e2, ps))
    assert False
