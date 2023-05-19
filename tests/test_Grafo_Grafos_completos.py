from src.Grafo_Grafos_completos import completo


def test_completo() -> None:
    assert str(completo(4)) == \
        "G ND [1, 2, 3, 4] [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]"
