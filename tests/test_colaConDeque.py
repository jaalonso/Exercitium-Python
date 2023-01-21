from src.TAD.colaConDeque import Cola, esVacia, inserta, primero, resto, vacia


def test_cola() -> None:
    c: Cola[int] = Cola()
    assert str(c) == "-"
    c.inserta(5)
    c.inserta(2)
    c.inserta(3)
    c.inserta(4)
    assert str(c) == "5 | 2 | 3 | 4"
    assert c.primero() == 5
    c.resto()
    assert str(c) == "2 | 3 | 4"
    assert not c.esVacia()
    c = Cola()
    assert c.esVacia()
    assert str(vacia()) == "-"
    assert str(inserta(4, inserta(3, inserta(2, inserta(5, vacia()))))) \
        == "5 | 2 | 3 | 4"
    assert primero(inserta(4, inserta(3, inserta(2, inserta(5, vacia()))))) \
        == 5
    assert str(resto(inserta(4, inserta(3, inserta(2, inserta(5, vacia()))))))\
        == "2 | 3 | 4"
    assert not esVacia(inserta(4, inserta(3, inserta(2, inserta(5, vacia())))))
    assert esVacia(vacia())
