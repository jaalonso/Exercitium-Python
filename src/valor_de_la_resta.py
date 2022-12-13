# valor_de_la_resta.py
# El tipo de las expresiones aritméticas: Valor de la resta.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 13-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Se considera el tipo de las expresiones aritméticas definido por
#    @dataclass
#    class Expr:
#        pass
#
#    @dataclass
#    class Lit(Expr):
#        x: int
#
#    @dataclass
#    class Suma(Expr):
#        x: Expr
#        y: Expr
#
#    @dataclass
#    class Op(Expr):
#        x: Expr
#
#    @dataclass
#    class SiCero(Expr):
#        x: Expr
#        y: Expr
#        z: Expr
#
# formado por
# + literales (p.e. Lit 7),
# + sumas (p.e. Suma (Lit 7) (Suma (Lit 3) (Lit 5)))
# + opuestos (p.e. Op (Suma (Op (Lit 7)) (Suma (Lit 3) (Lit 5))))
# + expresiones condicionales (p.e. (SiCero (Lit 3) (Lit 4) (Lit 5))
#
# La función para calcular el valor de una expresión es
#    def valor(e: Expr) -> int:
#        match e:
#            case Lit(n):
#                return n
#            case Suma(x, y):
#                return valor(x) + valor(y)
#            case Op(x):
#                return -valor(x)
#            case SiCero(x, y, z):
#                return valor(y) if valor(x) == 0 else valor(z)
#        assert False
#
# Definir la función
#    resta : (Expr, Expr) -> Expr
# tal que resta(e1, e2) es la expresión correspondiente a la diferencia
# de e1 y e2. Por ejemplo,
#    resta(Lit(42), Lit(2))  ==  Suma(Lit(42), Op(Lit(2)))
#
# Comprobar con Hypothesis que
#    valor(resta(x, y)) == valor(x) - valor(y)
# ---------------------------------------------------------------------

from dataclasses import dataclass
from random import choice, randint

from hypothesis import given
from hypothesis import strategies as st


@dataclass
class Expr:
    pass

@dataclass
class Lit(Expr):
    x: int

@dataclass
class Suma(Expr):
    x: Expr
    y: Expr

@dataclass
class Op(Expr):
    x: Expr

@dataclass
class SiCero(Expr):
    x: Expr
    y: Expr
    z: Expr

def valor(e: Expr) -> int:
    match e:
        case Lit(n):
            return n
        case Suma(x, y):
            return valor(x) + valor(y)
        case Op(x):
            return -valor(x)
        case SiCero(x, y, z):
            return valor(y) if valor(x) == 0 else valor(z)
    assert False

def resta(x: Expr, y: Expr) -> Expr:
    return Suma(x, Op(y))

# -- Comprobación de la propiedad
# -- ============================

# exprArbitraria(n) es una expresión aleatoria de tamaño n. Por
# ejemplo,
#    >>> exprArbitraria(3)
#    Op(x=Op(x=Lit(x=9)))
#    >>> exprArbitraria(3)
#    Op(x=SiCero(x=Lit(x=6), y=Lit(x=2), z=Lit(x=6)))
#    >>> exprArbitraria(3)
#    Suma(x=Lit(x=8), y=Lit(x=2))
def exprArbitraria(n: int) -> Expr:
    if n <= 1:
        return Lit(randint(0, 10))
    m = n // 2
    return choice([Lit(randint(0, 10)),
                   Suma(exprArbitraria(m), exprArbitraria(m)),
                   Op(exprArbitraria(n - 1)),
                   SiCero(exprArbitraria(m),
                          exprArbitraria(m),
                          exprArbitraria(m))])

# La propiedad es
@given(st.integers(min_value=1, max_value=10),
       st.integers(min_value=1, max_value=10))
def test_mismaForma(n1: int, n2: int) -> None:
    x = exprArbitraria(n1)
    y = exprArbitraria(n2)
    assert valor(resta(x, y)) == valor(x) - valor(y)

# La comprobación es
#    src> poetry run pytest -q valor_de_la_resta.py
#    1 passed in 0.21s
