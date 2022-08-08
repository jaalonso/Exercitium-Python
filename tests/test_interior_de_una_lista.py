from src.interior_de_una_lista import interior1, interior2


def test_interior():
    assert interior1([2, 5, 3, 7, 3]) == [5, 3, 7]
    assert interior2([2, 5, 3, 7, 3]) == [5, 3, 7]
