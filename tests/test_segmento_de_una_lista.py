from hypothesis import given, strategies as st
from src.segmento_de_una_lista import segmento1, segmento2

def test_segmento():
    assert segmento1(3, 4, [3, 4, 1, 2, 7, 9, 0]) == [1, 2]
    assert segmento1(3, 5, [3, 4, 1, 2, 7, 9, 0]) == [1, 2, 7]
    assert segmento1(5, 3, [3, 4, 1, 2, 7, 9, 0]) == []
    assert segmento2(3, 4, [3, 4, 1, 2, 7, 9, 0]) == [1, 2]
    assert segmento2(3, 5, [3, 4, 1, 2, 7, 9, 0]) == [1, 2, 7]
    assert segmento2(5, 3, [3, 4, 1, 2, 7, 9, 0]) == []

@given(st.integers(), st.integers(), st.lists(st.integers()))
def test_equiv_segmento(m, n, xs):
    assert segmento1(m, n, xs) == segmento2(m, n, xs)
