from src.elemento_mediano import mediano


def test_mediano():
    assert mediano(3, 2, 5) == 3
    assert mediano(2, 4, 5) == 4
    assert mediano(2, 6, 5) == 5
    assert mediano(2, 6, 6) == 6
