from src.igualdad_de_conjuntos import iguales1, iguales2


def test_iguales():
    assert iguales1([3, 2, 3], [2, 3])
    assert iguales1([3, 2, 3], [2, 3, 2])
    assert not iguales1([3, 2, 3], [2, 3, 4])
    assert not iguales1([2, 3], [4, 5])
    assert iguales2([3, 2, 3], [2, 3])
    assert iguales2([3, 2, 3], [2, 3, 2])
    assert not iguales2([3, 2, 3], [2, 3, 4])
    assert not iguales2([2, 3], [4, 5])
