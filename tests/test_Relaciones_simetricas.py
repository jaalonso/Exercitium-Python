from src.Relaciones_simetricas import simetrica


def test_simetrica() -> None:
    assert simetrica(([1, 3], [(1, 1), (1, 3), (3, 1)]))
    assert not simetrica(([1, 3], [(1, 1), (1, 3), (3, 2)]))
    assert simetrica(([1, 3], []))
