from src.Reconocimiento_de_subconjunto import (subconjunto1, subconjunto2,
                                               subconjunto3, subconjunto4)


def test_subconjunto() -> None:
    for subconjunto_ in [subconjunto1, subconjunto2, subconjunto3,
                        subconjunto4]:
        assert subconjunto_([3, 2, 3], [2, 5, 3, 5])
        assert not subconjunto_([3, 2, 3], [2, 5, 6, 5])
