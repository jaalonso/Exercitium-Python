# numero_de_variables_de_una_expresion_aritmetica.py
# Número de variables de una expresión aritmética.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 10-enero-2023.
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
#    P(X(), S(C(13), X()))
#
# Definir la función
#    numVars : (Expr) -> int
# tal que numVars(e) es el número de variables en la expresión e. Por
# ejemplo,
#    numVars(C(3))                   ==  0
#    numVars(X())                    ==  1
#    numVars(P(X(), S(C(13), X())))  ==  2
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
