from src.el_tipo_de_figuras_geometricas import \
    area, cuadrado, Circulo, Rect

def test_figura() -> None:
    assert area(Circulo(1)) == 3.141592653589793
    assert area(Circulo(2)) == 12.566370614359172
    assert area(Rect(2, 5)) == 10
    assert area(cuadrado(3)) == 9.0
