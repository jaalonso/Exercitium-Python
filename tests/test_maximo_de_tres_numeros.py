from src.maximo_de_tres_numeros import maxTres


def test_maxTres():
    assert maxTres(6, 2, 4) == 6
    assert maxTres(6, 7, 4) == 7
    assert maxTres(6, 7, 9) == 9
