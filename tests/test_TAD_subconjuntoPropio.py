from src.TAD_subconjuntoPropio import inserta, subconjuntoPropio, vacio


def test_subconjuntoPropio() -> None:
    ej1 = inserta(5, inserta(2, vacio()))
    ej2 = inserta(3, inserta(2, inserta(5, vacio())))
    ej3 = inserta(3, inserta(4, inserta(5, vacio())))
    ej4 = inserta(2, inserta(5, vacio()))
    assert subconjuntoPropio(ej1, ej2)
    assert not subconjuntoPropio(ej1, ej3)
    assert not subconjuntoPropio(ej1, ej4)
