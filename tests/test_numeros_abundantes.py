from src.numeros_abundantes import numeroAbundante1, numeroAbundante2

def test_numeroAbundante():
    assert not numeroAbundante1(5)
    assert numeroAbundante1(12)
    assert not numeroAbundante1(28)
    assert numeroAbundante1(30)
    assert not numeroAbundante2(5)
    assert numeroAbundante2(12)
    assert not numeroAbundante2(28)
    assert numeroAbundante2(30)
