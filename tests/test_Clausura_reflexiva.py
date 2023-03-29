from src.Clausura_reflexiva import clausuraReflexiva


def test_clausuraReflexiva() -> None:
    assert clausuraReflexiva (([1,3],[(1,1),(3,1)]))\
        == ([1, 3], [(3, 1), (1, 1), (3, 3)])
