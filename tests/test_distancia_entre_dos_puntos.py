from hypothesis import given, strategies as st
from src.distancia_entre_dos_puntos import distancia


def test_distancia():
    assert distancia((1, 2), (4, 6)) == 5.0


@given(st.tuples(st.integers(), st.integers()),
       st.tuples(st.integers(), st.integers()),
       st.tuples(st.integers(), st.integers()))
def test_triangular(p1, p2, p3):
    assert distancia(p1, p3) <= distancia(p1, p2) + distancia(p2, p3)
