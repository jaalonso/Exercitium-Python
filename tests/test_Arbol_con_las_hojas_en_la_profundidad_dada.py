from src.arbol_con_las_hojas_en_la_profundidad_dada import \
    Hoja, Nodo, creaArbol

def test_creaArbol() -> None:
    assert creaArbol(2) == \
        Nodo(Nodo(Hoja(None), Hoja(None)), Nodo(Hoja(None), Hoja(None)))
