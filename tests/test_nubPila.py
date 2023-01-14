from src.nubPila import (apila, nubPila1, nubPila2,
                         nubPila3, vacia)


def test_nubApila() -> None:
    for nubPila in [nubPila1, nubPila2, nubPila3]:
        assert str(nubPila(apila(3, apila(1, apila(3, apila(5, vacia()))))))\
            == "1 | 3 | 5"
