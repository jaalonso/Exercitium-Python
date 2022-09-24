# intercambio_de_componentes_de_un_par.py
# Intercambio de componentes de un par.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 5-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    intercambia : (tuple[A, B]) -> tuple[B, A]
# tal que intercambia(p)  es el punto obtenido intercambiando las
# coordenadas del punto p. Por ejemplo,
#    intercambia((2,5))  ==  (5,2)
#    intercambia((5,2))  ==  (2,5)
#
# Comprobar con Hypothesis que la función intercambia es
# idempotente; es decir, si se aplica dos veces es lo mismo que no
# aplicarla ninguna.
# ---------------------------------------------------------------------

from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

A = TypeVar('A')
B = TypeVar('B')

def intercambia(p: tuple[A, B]) -> tuple[B, A]:
    (x, y) = p
    return (y, x)

# La propiedad de es
@given(st.tuples(st.integers(), st.integers()))
def test_equiv_intercambia(p: tuple[int, int]) -> None:
    assert intercambia(intercambia(p)) == p

# La comprobación es
#    src> poetry run pytest -q intercambio_de_componentes_de_un_par.py
#    1 passed in 0.15s
