from src.numeros_perfectos import \
    perfectos1, \
    perfectos2, \
    perfectos3

def test_perfectos():
    assert perfectos1(500) == [6, 28, 496]
    assert perfectos2(500) == [6, 28, 496]
    assert perfectos3(500) == [6, 28, 496]
