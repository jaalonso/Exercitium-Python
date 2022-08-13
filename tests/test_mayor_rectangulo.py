from src.mayor_rectangulo import mayorRectangulo


def test_mayorRectangulo():
    assert mayorRectangulo((4, 6),  (3, 7)) == (4, 6)
    assert mayorRectangulo((4, 6),  (3, 8)) == (4, 6)
    assert mayorRectangulo((4, 6),  (3, 9)) == (3, 9)
