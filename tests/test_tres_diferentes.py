from src.tres_diferentes import tresDiferentes


def test_tresDiferemtes():
    assert tresDiferentes(3, 5, 2) is True
    assert tresDiferentes(3, 5, 3) is False
