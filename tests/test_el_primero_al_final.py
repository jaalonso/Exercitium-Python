from hypothesis import given
from hypothesis import strategies as st
from src.el_primero_al_final import rota1a, rota1b


def test_rota1():
    assert rota1a([3, 2, 5, 7]) == [2, 5, 7, 3]
    assert rota1a(['a', 'b', 'c']) == ['b', 'c', 'a']
    assert rota1b([3, 2, 5, 7]) == [2, 5, 7, 3]
    assert rota1b(['a', 'b', 'c']) == ['b', 'c', 'a']

@given(st.lists(st.integers()))
def test_equiv_rota1(xs):
    assert rota1a(xs) == rota1b(xs)
