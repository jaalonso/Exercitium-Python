from src.TAD_mapC import inserta, mapC, mapC2, mapC3, mapC4, vacio


def test_mapC() -> None:
    for mapC_ in [mapC, mapC2, mapC3, mapC4]:
        assert str(mapC_(lambda x: 2 * x, inserta(3, inserta(1, vacio()))))\
            == "{2, 6}"
