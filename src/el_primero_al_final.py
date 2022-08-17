# el_primero_al_final.py
# El primero al final.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 16-agosto-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    rota1 : (List[A]) -> List[A]
# tal que rota1(xs) es la lista obtenida poniendo el primer elemento de
# xs al final de la lista. Por ejemplo,
#    rota1([3, 2, 5, 7]) == [2, 5, 7, 3]
#    rota1(['a', 'b', 'c']) == ['b', 'c', 'a']
# ---------------------------------------------------------------------

from typing import List, TypeVar
from hypothesis import given, strategies as st

A = TypeVar('A')

# 1ª solución
def rota1a(xs):
    # type: (List[A]) -> List[A]
    if xs == []:
        return []
    return xs[1:] + [xs[0]]

# 2ª solución
def rota1b(xs):
    # type: (List[A]) -> List[A]
    if xs == []:
        return []
    ys = xs[1:]
    ys.append(xs[0])
    return ys

# La equivalencia de las definiciones es
@given(st.lists(st.integers()))
def test_rota1(xs):
    assert rota1a(xs) == rota1b(xs)

# La comprobación es
#    src> poetry run pytest -q el_primero_al_final.py
#    1 passed in 0.20s
