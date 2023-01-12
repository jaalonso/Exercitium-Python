from hypothesis import given
from hypothesis import strategies as st
from src.interior_de_una_lista import interior1, interior2


def test_interior():
    assert interior1([2, 5, 3, 7, 3]) == [5, 3, 7]
    assert interior2([2, 5, 3, 7, 3]) == [5, 3, 7]

@given(st.lists(st.integers()))
def test_triangular(xs):
    assert interior1(xs) == interior2(xs)
