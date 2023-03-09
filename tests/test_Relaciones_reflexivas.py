from src.Relaciones_reflexivas import reflexiva


def test_reflexiva() -> None:
    assert reflexiva(([1, 3], [(1, 1),(1, 3),(3, 3)]))
    assert not reflexiva(([1, 2, 3], [(1, 1),(1, 3),(3, 3)]))
