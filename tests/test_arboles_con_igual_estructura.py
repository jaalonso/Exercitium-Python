from src.arboles_con_igual_estructura import \
    ej3arbol1, ej3arbol2, ej3arbol3, ej3arbol4, igualEstructura

def test_igualEstructura() -> None:
    assert igualEstructura(ej3arbol1, ej3arbol2) is True
    assert igualEstructura(ej3arbol1, ej3arbol3) is False
    assert igualEstructura(ej3arbol1, ej3arbol4) is False
