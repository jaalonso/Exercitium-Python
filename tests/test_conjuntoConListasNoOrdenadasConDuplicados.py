from src.TAD.conjuntoConListasNoOrdenadasConDuplicados import (Conj, elimina,
                                                               esVacio,
                                                               inserta, menor,
                                                               pertenece,
                                                               vacio)


def test_conjuntos() -> None:
    c = Conj()
    assert str(c) == "{}"
    c.inserta(5)
    c.inserta(2)
    c.inserta(3)
    c.inserta(4)
    c.inserta(5)
    assert str(c) == "{2, 3, 4, 5}"
    assert c.menor() == 2
    c.elimina(3)
    assert str(c) == "{2, 4, 5}"
    assert c.pertenece(4)
    assert not c.pertenece(3)
    assert not c.esVacio()
    c = Conj()
    assert c.esVacio()
    c = Conj()
    c.inserta(2)
    c.inserta(5)
    d = Conj()
    d.inserta(5)
    d.inserta(2)
    d.inserta(5)
    assert c == d
    assert str(vacio()) == "{}"
    assert str(inserta(5, inserta(3, inserta(2, inserta(5, vacio())))))\
        == "{2, 3, 5}"
    assert menor(inserta(5, inserta(3, inserta(2, inserta(5, vacio())))))\
        == 2
    assert str(elimina(5, inserta(5, inserta(3, inserta(2, inserta(5, vacio()))))))\
        == "{2, 3}"
    assert pertenece(5, inserta(5, inserta(3, inserta(2, inserta(5, vacio())))))
    assert not pertenece(1, inserta(5, inserta(3, inserta(2, inserta(5, vacio())))))
    assert not esVacio(inserta(5, inserta(3, inserta(2, inserta(5, vacio())))))
    assert esVacio(vacio())
    assert inserta(5, inserta(2, vacio())) == inserta(2, inserta(5, (inserta(2, vacio()))))
