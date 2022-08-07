from src.reconocimiento_de_palindromos import palindromo


def test_palindromo():
    assert palindromo([3, 2, 5, 2, 3]) is True
    assert palindromo([3, 2, 5, 6, 2, 3]) is False
