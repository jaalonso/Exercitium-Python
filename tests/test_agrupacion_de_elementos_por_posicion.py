from src.agrupacion_de_elementos_por_posicion import (agrupa1, agrupa2,
                                                      agrupa3, agrupa4,
                                                      agrupa5)


def test_agrupa() -> None:
    for agrupa in [agrupa1, agrupa2, agrupa3, agrupa4, agrupa5]:
        assert agrupa([[1, 6], [7, 8, 9], [3, 4, 5]]) == \
            [[1, 7, 3], [6, 8, 4]]
