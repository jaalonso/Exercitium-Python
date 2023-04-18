# Pol_Crea_termino.py
# Construcción de términos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 24-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu),
# definir la función
#    creaTermino : (int, A) -> Polinomio[A]
# tal que creaTermino(n, a) es el término a*x^n. Por ejemplo,
#    >>> creaTermino(2, 5)
#    5*x^2
# ---------------------------------------------------------------------

from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.TAD.Polinomio import Polinomio, consPol, polCero

A = TypeVar('A', int, float, complex)

# 1ª solución
# ===========

def creaTermino(n: int, a: A) -> Polinomio[A]:
    return consPol(n, a, polCero())

# 2ª solución
# ===========

def creaTermino2(n: int, a: A) -> Polinomio[A]:
    r: Polinomio[A] = polCero()
    return r.consPol(n, a)

# Equivalencia de las definiciones
# ================================

# La propiedad es
@given(st.integers(min_value=0, max_value=9),
       st.integers(min_value=-9, max_value=9))
def test_creaTermino(n: int, a: int) -> None:
    assert creaTermino(n, a) == creaTermino2(n, a)

# La comprobación es
#    > poetry run pytest -q Pol_Crea_termino.py
#    1 passed in 0.21s
