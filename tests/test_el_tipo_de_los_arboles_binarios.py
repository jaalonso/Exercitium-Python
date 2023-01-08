from src.el_tipo_de_los_arboles_binarios import aplana, ejArbol, ocurre


def test_arboles() -> None:
    assert ocurre(4, ejArbol) is True
    assert ocurre(0, ejArbol) is False
    assert aplana(ejArbol) == [1, 3, 4, 5, 6, 7, 9]
