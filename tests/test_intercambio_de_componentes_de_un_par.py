from hypothesis import given
from hypothesis import strategies as st

from src.intercambio_de_componentes_de_un_par import intercambia


def test_intercambia():
    assert intercambia((2, 5)) == (5, 2)
    assert intercambia((5, 2)) == (2, 5)

@given(st.tuples(st.integers(), st.integers()))
def test_equiv_intercambia(p):
    assert intercambia(intercambia(p)) == p
