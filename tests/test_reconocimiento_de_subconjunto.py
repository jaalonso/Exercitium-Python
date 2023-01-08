from src.reconocimiento_de_subconjunto import (subconjunto1, subconjunto2,
                                               subconjunto3, subconjunto4)


def test_subconjunto():
    assert subconjunto1([3, 2, 3], [2, 5, 3, 5]) is True
    assert subconjunto1([3, 2, 3], [2, 5, 6, 5]) is False
    assert subconjunto2([3, 2, 3], [2, 5, 3, 5]) is True
    assert subconjunto2([3, 2, 3], [2, 5, 6, 5]) is False
    assert subconjunto3([3, 2, 3], [2, 5, 3, 5]) is True
    assert subconjunto3([3, 2, 3], [2, 5, 6, 5]) is False
    assert subconjunto4([3, 2, 3], [2, 5, 3, 5]) is True
    assert subconjunto4([3, 2, 3], [2, 5, 6, 5]) is False
