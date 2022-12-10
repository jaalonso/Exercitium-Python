from src.arboles_con_la_misma_forma import \
    Hoja, Nodo, mismaForma1, mismaForma2

def test_mismaForma() -> None:
    for mismaForma in [mismaForma1, mismaForma2]:
        arbol1 = Hoja(5)
        arbol2 = Hoja(3)
        assert mismaForma(arbol1, arbol2)
        arbol3 = Nodo(Hoja(6), Hoja(7))
        assert not mismaForma(arbol1, arbol3)
        arbol4 = Nodo(Hoja(9), Hoja(5))
        assert mismaForma(arbol3, arbol4)
