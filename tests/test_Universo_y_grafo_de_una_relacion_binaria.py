from src.Universo_y_grafo_de_una_relacion_binaria import Rel, grafo, universo


def test_universo_grafo() -> None:
    r = (list(range(1, 10)), [(1, 3), (2, 6), (8, 9), (2, 7)])
    assert universo(r) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert grafo(r) == [(1, 3), (2, 6), (8, 9), (2, 7)]
