from src.numeros_perfectos import \
    perfectos1, \
    perfectos2

def test_perfectos():
    assert perfectos1(500) == [6, 28, 496]
    assert perfectos2(500) == [6, 28, 496]
