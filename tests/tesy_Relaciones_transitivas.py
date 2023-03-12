from src.Relaciones_transitivas import transitiva1, transitiva2, transitiva3


def test_transitiva() -> None:
    for transitiva_ in [transitiva1, transitiva2, transitiva3]:
        assert transitiva_(([1, 3, 5], [(1, 1), (1, 3), (3, 1), (3, 3), (5, 5)]))
        assert not transitiva_(([1, 3, 5], [(1, 1), (1, 3), (3, 1), (5, 5)]))
