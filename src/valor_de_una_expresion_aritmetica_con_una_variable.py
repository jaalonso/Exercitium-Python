# valor_de_una_expresion_aritmetica_con_una_variable.py
# Valor de una expresión aritmética con una variable.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 9-enero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Las expresiones aritméticas construidas con una variable (denotada
# por X), los números enteros y las operaciones de sumar y multiplicar
# se pueden representar mediante el tipo de datos Expr definido por
#    @dataclass
#    class Expr:
#        pass
#
#    @dataclass
#    class X(Expr):
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
# Por ejemplo, la expresión X*(13+X) se representa por
#    P X (S (C 13) X)
#
# Definir la función
#    valor : (Expr, int) -> int
# tal que valor(e, n) es el valor de la expresión e cuando se
# sustituye su variable por n. Por ejemplo,
#    valor(P(X(), S(C(13), X())), 2)  ==  30
# ---------------------------------------------------------------------

from dataclasses import dataclass


@dataclass
class Expr:
    pass

@dataclass
class X(Expr):
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
