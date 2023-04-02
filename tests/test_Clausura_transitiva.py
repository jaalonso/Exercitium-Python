from src.Clausura_transitiva import clausuraTransitiva, clausuraTransitiva2


def test_clausuraTransitiva() -> None:
    for clausuraTransitiva_ in [clausuraTransitiva,
                                clausuraTransitiva2]:
        assert clausuraTransitiva (([1, 2, 3, 4, 5, 6], [(1, 2), (2, 5), (5, 6)]))\
            == ([1, 2, 3, 4, 5, 6], [(1, 2), (2, 5), (5, 6), (2, 6), (1, 5), (1, 6)])
