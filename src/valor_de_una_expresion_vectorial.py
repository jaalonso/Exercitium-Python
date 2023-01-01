# valor_de_una_expresion_vectorial.py
# Valor de una expresión vectorial.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 19-enero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Se consideran las expresiones vectoriales formadas por un vector, la
# suma de dos expresiones vectoriales o el producto de un entero por
# una expresión vectorial. El siguiente tipo de dato define las
# expresiones vectoriales
#    @dataclass
#    class ExpV:
#        pass
#
#    @dataclass
#    class Vec(ExpV):
#        x: int
#        y: int
#
#    @dataclass
#    class Sum(ExpV):
#        x: ExpV
#        y: ExpV
#
#    @dataclass
#    class Mul(ExpV):
#        x: int
#        y: ExpV
#
# Definir la función
#    valorEV : (ExpV) -> tuple[int, int]
# tal que valorEV(e) es el valorEV de la expresión vectorial c. Por
# ejemplo,
#    valorEV(Vec(1, 2))                                  ==  (1,2)
#    valorEV(Sum(Vec(1, 2), Vec(3, 4)))                  ==  (4,6)
#    valorEV(Mul(2, Vec(3, 4)))                          ==  (6,8)
#    valorEV(Mul(2, Sum(Vec(1, 2), Vec(3, 4))))          ==  (8,12)
#    valorEV(Sum(Mul(2, Vec(1, 2)), Mul(2, Vec(3, 4))))  ==  (8,12)
# ---------------------------------------------------------------------

from dataclasses import dataclass


@dataclass
class ExpV:
    pass

@dataclass
class Vec(ExpV):
    x: int
    y: int

@dataclass
class Sum(ExpV):
    x: ExpV
    y: ExpV

@dataclass
class Mul(ExpV):
    x: int
    y: ExpV

# 1ª solución
# ===========

def valorEV1(e: ExpV) -> tuple[int, int]:
    match e:
        case Vec(x, y):
            return (x, y)
        case Sum(e1, e2):
            x1, y1 = valorEV1(e1)
            x2, y2 = valorEV1(e2)
            return (x1 + x2, y1 + y2)
        case Mul(n, e):
            x, y = valorEV1(e)
            return (n * x, n * y)
    assert False

# 2ª solución
# ===========

def suma(p: tuple[int, int], q: tuple[int, int]) -> tuple[int, int]:
    a, b = p
    c, d = q
    return (a + c, b + d)

def multiplica(n: int, p: tuple[int, int]) -> tuple[int, int]:
    a, b = p
    return (n * a, n * b)

def valorEV2(e: ExpV) -> tuple[int, int]:
    match e:
        case Vec(x, y):
            return (x, y)
        case Sum(e1, e2):
            return suma(valorEV2(e1), valorEV2(e2))
        case Mul(n, e):
            return multiplica(n, valorEV2(e))
    assert False
