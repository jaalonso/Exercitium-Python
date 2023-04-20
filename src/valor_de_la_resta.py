# valor_de_la_resta.py
# El tipo de las expresiones aritméticas: Valor de la resta.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 13-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las expresiones aritméticas](https://bit.ly/40vCQUh),
# definir la función
#    resta : (Expr, Expr) -> Expr
# tal que resta(e1, e2) es la expresión correspondiente a la diferencia
# de e1 y e2. Por ejemplo,
#    resta(Lit(42), Lit(2))  ==  Suma(Lit(42), Op(Lit(2)))
#
# Comprobar con Hypothesis que
#    valor(resta(x, y)) == valor(x) - valor(y)
# ---------------------------------------------------------------------

from random import choice, randint

from hypothesis import given
from hypothesis import strategies as st

from src.tipo_expresion_aritmetica import Expr, Lit, Op, SiCero, Suma
from src.valor_de_una_expresion_aritmetica import valor


def resta(x: Expr, y: Expr) -> Expr:
    return Suma(x, Op(y))

# Comprobación de la propiedad
# ============================

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
