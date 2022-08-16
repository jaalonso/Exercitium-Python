from hypothesis import given, strategies as st
from src.elementos_finales import finales1, finales2, finales3

def test_finales():
    assert finales1(3, [2, 5, 4, 7, 9, 6]) == [7, 9, 6]
    assert finales2(3, [2, 5, 4, 7, 9, 6]) == [7, 9, 6]
    assert finales3(3, [2, 5, 4, 7, 9, 6]) == [7, 9, 6]

@given(st.integers(), st.lists(st.integers()))
def test_equiv_finales(n, xs):
    assert finales1(n, xs) == finales2(n, xs) == finales3(n, xs)
