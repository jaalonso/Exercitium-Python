from src.Relaciones_totales import total, total2, total3, total4, total5


def test_total() -> None:
    for total_ in [total, total2, total3, total4, total5]:
        assert total_(([1,3],[(1,1),(3,1),(3,3)]))
        assert not total_(([1,3],[(1,1),(3,1)]))
        assert not total_(([1,3],[(1,1),(3,3)]))
