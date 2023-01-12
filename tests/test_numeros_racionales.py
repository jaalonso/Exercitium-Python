from hypothesis import assume, given
from hypothesis import strategies as st
from src.numeros_racionales import (formaReducida, igualdadRacional,
                                    productoRacional, sumaRacional)


def test_numeros_racionales():
    assert formaReducida((4, 10)) == (2, 5)
    assert formaReducida((0, 5)) == (0, 1)
    assert sumaRacional((2, 3), (5, 6)) == (3, 2)
    assert sumaRacional((3, 5), (-3, 5)) == (0, 1)
    assert productoRacional((2, 3), (5, 6)) == (5, 9)
    assert igualdadRacional((6, 9), (10, 15)) is True
    assert igualdadRacional((6, 9), (11, 15)) is False
    assert igualdadRacional((0, 2), (0, -5)) is True

@given(st.tuples(st.integers(), st.integers()),
       st.tuples(st.integers(), st.integers()),
       st.tuples(st.integers(), st.integers()))
def test_prop_distributiva(x, y, z):
    (_, x2) = x
    (_, y2) = y
    (_, z2) = z
    assume(x2 != 0 and y2 != 0 and z2 != 0)
    assert igualdadRacional(productoRacional(x, sumaRacional(y, z)),
                            sumaRacional(productoRacional(x, y),
                                         productoRacional(x, z)))
