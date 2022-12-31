# valor_de_expresiones_aritmeticas_generales.py
# Valor de expresiones aritméticas generales.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 18-enero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Las operaciones de suma, resta y  multiplicación se pueden
# representar mediante el siguiente tipo de datos
#    Op = Enum('Op', ['S', 'R', 'M'])
# La expresiones aritméticas con dichas operaciones se pueden
# representar mediante el siguiente tipo de dato algebraico
#    @dataclass
#    class Expr:
#        pass
#
#    @dataclass
#    class C(Expr):
#        x: int
#
#    @dataclass
#    class A(Expr):
#        o: Op
#        x: Expr
#        y: Expr
# Por ejemplo, la expresión
#    (7-3)+(2*5)
# se representa por
#    A(Op.S, A(Op.R, C(7), C(3)), A(Op.M, C(2), C(5)))
#
# Definir la función
#    valor : (Expr) -> int
# tal que valor(e) es el valor de la expresión e. Por ejemplo,
#    >>> valor(A(Op.S, A(Op.R, C(7), C(3)), A(Op.M, C(2), C(5))))
#    14
#    >>> valor(A(Op.M, A(Op.R, C(7), C(3)), A(Op.S, C(2), C(5))))
#    28
# ---------------------------------------------------------------------

from dataclasses import dataclass
from enum import Enum

Op = Enum('Op', ['S', 'R', 'M'])

@dataclass
class Expr:
    pass

@dataclass
class C(Expr):
    x: int

@dataclass
class A(Expr):
    o: Op
    x: Expr
    y: Expr

def aplica(o: Op, x: int, y: int) -> int:
    match o:
        case Op.S:
            return x + y
        case Op.R:
            return x - y
        case Op.M:
            return x * y
    assert False

def valor(e: Expr) -> int:
    match e:
        case C(x):
            return x
        case A(o, e1, e2):
            return aplica(o, valor(e1), valor(e2))
    assert False
