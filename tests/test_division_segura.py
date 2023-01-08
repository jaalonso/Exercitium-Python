from hypothesis import given
from hypothesis import strategies as st

from src.division_segura import divisionSegura1, divisionSegura2


def test_divisionSegura():
    assert divisionSegura1(7, 2) == 3.5
    assert divisionSegura1(7, 0) == 9999.0
    assert divisionSegura2(7, 2) == 3.5
    assert divisionSegura2(7, 0) == 9999.0

@given(st.floats(allow_nan=False, allow_infinity=False),
       st.floats(allow_nan=False, allow_infinity=False))
def test_equiv_divisionSegura(x, y):
    assert divisionSegura1(x, y) == divisionSegura2(x, y)
