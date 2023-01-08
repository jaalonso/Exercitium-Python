from src.producto_cartesiano_de_dos_conjuntos import producto1, producto2


def test_producto() -> None:
    for producto in [producto1, producto2]:
        assert producto([1, 3], [2, 4]) == [(1, 2), (1, 4), (3, 2), (3, 4)]
