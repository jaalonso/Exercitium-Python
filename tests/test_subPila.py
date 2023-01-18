from src.subPila import apila, subPila1, subPila2, subPila3, vacia


def test_subPila() -> None:
    ej1 = apila(2, apila(3, vacia()))
    ej2 = apila(7, apila(2, apila(3, apila(5, vacia()))))
    ej3 = apila(2, apila(7, apila(3, apila(5, vacia()))))
    for subPila in [subPila1, subPila2, subPila3]:
        assert subPila(ej1, ej2)
        assert not subPila(ej1, ej3)
