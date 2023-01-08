from src.segmentos_cuyos_elementos_cumple_una_propiedad import (segmentos1,
                                                                segmentos2)


def test_segmentos() -> None:
    for segmentos in [segmentos1, segmentos2]:
        def par(x: int) -> bool:
            return x % 2 == 0

        def impar(x: int) -> bool:
            return x % 2 == 1

        xs = [1, 2, 0, 4, 9, 6, 4, 5, 7, 2]
        assert segmentos(par, xs) == [[2, 0, 4], [6, 4], [2]]
        assert segmentos(impar, xs) == [[1], [9], [5, 7]]
