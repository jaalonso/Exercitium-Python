# pylint: disable=line-too-long

from src.Grafo_Grafos_completos import completo


def test_completo() -> None:
    assert str(completo(4)) == \
        "G ND ([1, 2, 3, 4], [((1, 2), 0), ((1, 3), 0), ((1, 4), 0), ((2, 1), 0), ((2, 3), 0), ((2, 4), 0), ((3, 1), 0), ((3, 2), 0), ((3, 4), 0), ((4, 1), 0), ((4, 2), 0), ((4, 3), 0)])"
