from src.transformaciones_pilas_listas import (listaApila1, listaApila2,
                                               pilaAlista1, pilaAlista2,
                                               pilaAlista3, apila, vacia)

def test_transfomaciones_pilas_listas() -> None:
    assert str(listaApila1([3, 2, 5])) == "5 | 2 | 3"
    assert str(listaApila2([3, 2, 5])) == "5 | 2 | 3"
    ej = apila(5, apila(2, apila(3, vacia())))
    assert pilaAlista1(ej) == [3, 2, 5]
    assert pilaAlista2(ej) == [3, 2, 5]
    assert pilaAlista3(ej) == [3, 2, 5]
    assert str(ej) == "5 | 2 | 3"
