from src.transformaciones_colas_listas import (colaAlista, colaAlista2,
                                               colaAlista3, inserta,
                                               listaAcola, listaAcola2, vacia)


def test_transfomaciones_colas_listas() -> None:
    assert str(listaAcola([3, 2, 5])) == "3 | 2 | 5"
    assert str(listaAcola2([3, 2, 5])) == "3 | 2 | 5"
    ej = inserta(5, inserta(2, inserta(3, vacia())))
    assert colaAlista(ej) == [3, 2, 5]
    assert colaAlista2(ej) == [3, 2, 5]
    assert colaAlista3(ej) == [3, 2, 5]
    assert str(ej) == "3 | 2 | 5"
