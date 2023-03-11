from src.Composicion_de_relaciones_binarias_v2 import (composicion,
                                                       composicion2,
                                                       composicion3)


def test_composicion() -> None:
    assert composicion(([1,2],[(1,2),(2,2)]), ([1,2],[(2,1)]))\
        == ([1, 2], [(1, 1), (2, 1)])
