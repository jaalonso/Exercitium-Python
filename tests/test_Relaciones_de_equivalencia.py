from src.Relaciones_de_equivalencia import esEquivalencia


def test_equivalencia() -> None:
    assert esEquivalencia (([1,3,5],[(1,1),(1,3),(3,1),(3,3),(5,5)]))
    assert not esEquivalencia (([1,2,3,5],[(1,1),(1,3),(3,1),(3,3),(5,5)]))
    assert not esEquivalencia (([1,3,5],[(1,1),(1,3),(3,3),(5,5)]))
