from hypothesis import given
from hypothesis import strategies as st

from src.distancia_entre_dos_puntos import distancia


def test_distancia():
    assert distancia((1, 2), (4, 6)) == 5.0


cota = 2 ** 30


@given(st.tuples(st.integers(min_value=0, max_value=cota),
                 st.integers(min_value=0, max_value=cota)),
       st.tuples(st.integers(min_value=0, max_value=cota),
                 st.integers(min_value=0, max_value=cota)),
       st.tuples(st.integers(min_value=0, max_value=cota),
                 st.integers(min_value=0, max_value=cota)))
def test_triangular(p1, p2, p3):
    assert distancia(p1, p3) <= distancia(p1, p2) + distancia(p2, p3)
