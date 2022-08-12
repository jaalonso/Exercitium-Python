from src.disyuncion_excluyente import xor1, xor2, xor3, xor4, xor5


def test_xor():
    for xor in [xor1, xor2, xor3, xor4, xor5]:
        assert xor(True, True) is False
        assert xor(True, False) is True
        assert xor(False, True) is True
        assert xor(False, False) is False
