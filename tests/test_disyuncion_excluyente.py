from hypothesis import given
from hypothesis import strategies as st
from src.disyuncion_excluyente import xor1, xor2, xor3, xor4, xor5


def test_xor():
    for xor in [xor1, xor2, xor3, xor4, xor5]:
        assert xor(True, True) is False
        assert xor(True, False) is True
        assert xor(False, True) is True
        assert xor(False, False) is False

@given(st.booleans(), st.booleans())
def test_equiv_xor(x, y):
    assert xor1(x, y) == xor2(x, y) == xor3(x, y) == xor4(x, y) == xor5(x, y)
