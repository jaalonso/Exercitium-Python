from src.TAD_Transformaciones_conjuntos_listas import (conjuntoAlista,
                                                       conjuntoAlista2,
                                                       conjuntoAlista3,
                                                       inserta, listaAconjunto,
                                                       listaAconjunto2, vacio)


def test_transformaciones_conjuntos_listas() -> None:
    assert str(listaAconjunto([3, 2, 5])) == "{2, 3, 5}"
    assert str(listaAconjunto2([3, 2, 5])) == "{2, 3, 5}"
    ej = inserta(5, inserta(2, inserta(3, vacio())))
    assert conjuntoAlista(ej) == [2, 3, 5]
    assert conjuntoAlista2(ej) == [2, 3, 5]
    assert conjuntoAlista3(ej) == [2, 3, 5]
    assert str(ej) == "{2, 3, 5}"
