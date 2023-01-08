from src.altura_de_un_arbol_binario import Hoja, Nodo, altura


def test_altura() -> None:
    assert altura(Hoja(1)) == \
        0
    assert altura(Nodo(Hoja(1), Hoja(6))) == \
        1
    assert altura(Nodo(Nodo(Hoja(1), Hoja(6)), Hoja(2))) == \
        2
    assert altura(Nodo(Nodo(Hoja(1), Hoja(6)), Nodo(Hoja(2), Hoja(7)))) == \
        2
