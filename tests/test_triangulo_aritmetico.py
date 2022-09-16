from src.triangulo_aritmetico import \
    triangulo1, \
    triangulo2, \
    triangulo3

def test_triangulo():
    assert triangulo1(3) == [[1], [2, 3], [4, 5, 6]]
    assert triangulo1(4) == [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
    assert triangulo2(3) == [[1], [2, 3], [4, 5, 6]]
    assert triangulo2(4) == [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
    assert triangulo3(3) == [[1], [2, 3], [4, 5, 6]]
    assert triangulo3(4) == [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
