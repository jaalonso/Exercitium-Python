from src.Grafo_Grafos_ciclos import grafoCiclo


def test_grafoCiclo() -> None:
    assert str(grafoCiclo(3)) == \
        "G ND ([1, 2, 3], [(1, 2), (1, 3), (2, 3)])"
