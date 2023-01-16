from src.transformaciones_pilas_listas import (apila, listaApila, listaApila2,
                                               pilaAlista, pilaAlista2,
                                               pilaAlista3, vacia)


def test_transfomaciones_pilas_listas() -> None:
    assert str(listaApila([3, 2, 5])) == "5 | 2 | 3"
    assert str(listaApila2([3, 2, 5])) == "5 | 2 | 3"
    ej = apila(5, apila(2, apila(3, vacia())))
    assert pilaAlista(ej) == [3, 2, 5]
    assert pilaAlista2(ej) == [3, 2, 5]
    assert pilaAlista3(ej) == [3, 2, 5]
    assert str(ej) == "5 | 2 | 3"
