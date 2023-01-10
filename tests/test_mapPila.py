from src.mapPila import apila, mapPila1, mapPila2, mapPila3, mapPila4, vacia


def test_mapApila() -> None:
    ej = apila(5, apila(2, apila(7, vacia())))
    for mapPila in [mapPila1, mapPila2, mapPila3, mapPila4]:
        assert str(mapPila(lambda x: x + 1, ej)) == "6 | 3 | 8"
    assert str(ej) == "5 | 2 | 7"
