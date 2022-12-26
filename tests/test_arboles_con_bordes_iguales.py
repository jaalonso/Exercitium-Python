from src.arboles_con_bordes_iguales import \
    arbol1, arbol2, arbol3, arbol4, igualBorde

def test_igualBorde() -> None:
    assert igualBorde(arbol1, arbol2) is True
    assert igualBorde(arbol1, arbol3) is False
    assert igualBorde(arbol1, arbol4) is False
