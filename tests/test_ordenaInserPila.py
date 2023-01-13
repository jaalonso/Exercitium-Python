from src.ordenaInserPila import (apila, ordenaInserPila1, ordenaInserPila2,
                                 ordenaInserPila3, vacia)


def test_ordenaInserApila() -> None:
    for ordenaInserPila in [ordenaInserPila1, ordenaInserPila2,
                            ordenaInserPila3]:
        assert str(ordenaInserPila(apila(4, apila(1, apila(3, vacia())))))\
            == "1 | 3 | 4"
