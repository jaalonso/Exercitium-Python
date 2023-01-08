from src.aplicacion_de_una_funcion_a_un_arbol import Hoja, Nodo, mapArbol


def test_mapArbol() -> None:
    assert mapArbol(lambda x: 1 + x, Nodo(Hoja(2), Hoja(4))) == \
        Nodo(Hoja(3), Hoja(5))
