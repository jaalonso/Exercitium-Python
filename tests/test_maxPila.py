from src.maxPila import (apila, maxPila1, maxPila2,
                         maxPila3, maxPila4, vacia)


def test_ordenaInserApila() -> None:
    for maxPila in [maxPila1, maxPila2,
                    maxPila3, maxPila4]:
        assert maxPila(apila(3, apila(5, apila(1, vacia())))) == 5
