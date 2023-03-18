from src.Relaciones_irreflexivas import irreflexiva, irreflexiva2, irreflexiva3


def test_irreflexiva() -> None:
    for irreflexiva_ in [irreflexiva, irreflexiva2, irreflexiva3]:
        assert irreflexiva_(([1, 2, 3], [(1, 2), (2, 1), (2, 3)]))
        assert not irreflexiva_(([1, 2, 3], [(1, 2), (2, 1), (3, 3)]))
