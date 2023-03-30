from src.Clausura_simetrica import clausuraSimetrica


def test_clausuraSimetrica() -> None:
    assert clausuraSimetrica(([1, 3, 5], [(1, 1), (3, 1), (1, 5)]))\
        == ([1, 3, 5], [(1, 5), (3, 1), (1, 1), (1, 3), (5, 1)])
