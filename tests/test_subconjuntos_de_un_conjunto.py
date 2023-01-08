from src.subconjuntos_de_un_conjunto import (subconjuntos1, subconjuntos2,
                                             subconjuntos3, subconjuntos4)


def test_subconjuntos() -> None:
    for subconjuntos in [subconjuntos1, subconjuntos2, subconjuntos3,
                         subconjuntos4]:
        assert sorted([sorted(ys) for ys in subconjuntos([1, 2, 3, 4])]) == \
            [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 4], [1, 3],
             [1, 3, 4], [1, 4], [2], [2, 3], [2, 3, 4], [2, 4], [3], [3, 4],
             [4]]
