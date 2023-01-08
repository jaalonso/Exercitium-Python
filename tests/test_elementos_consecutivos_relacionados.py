from src.elementos_consecutivos_relacionados import (relacionados1,
                                                     relacionados2)


def test_relacionados() -> None:
    for relacionados in [relacionados1, relacionados2]:
        assert relacionados(lambda x, y: x < y, [2, 3, 7, 9])
        assert not relacionados(lambda x, y: x < y, [2, 3, 1, 9])
