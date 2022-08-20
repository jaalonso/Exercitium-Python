# permutacion_ciclica.py
# Permutación cíclica
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 7-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir una función
#    ciclo : (list[A]) -> list[A]
# tal que ciclo(xs) es la lista obtenida permutando cíclicamente los
# elementos de la lista xs, pasando el último elemento al principio de
# la lista. Por ejemplo,
#    ciclo([2, 5, 7, 9])  == [9, 2, 5, 7]
#    ciclo([])            == []
#    ciclo([2])           == [2]
#
# Comprobar que la longitud es un invariante de la función ciclo; es
# decir, la longitud de (ciclo xs) es la misma que la de xs.
# ---------------------------------------------------------------------

from typing import TypeVar
from hypothesis import given, strategies as st

A = TypeVar('A')

def ciclo(xs: list[A]) -> list[A]:
    if xs:
        return [xs[-1]] + xs[:-1]
    return []

# La propiedad de es
@given(st.lists(st.integers()))
def test_equiv_ciclo(xs):
    assert len(ciclo(xs)) == len(xs)

# La comprobación es
#    src> poetry run pytest -q permutacion_ciclica.py
#    1 passed in 0.39s
