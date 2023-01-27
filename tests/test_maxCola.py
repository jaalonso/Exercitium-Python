from src.maxCola import inserta, maxCola1, maxCola2, maxCola3, maxCola4, vacia


def test_maxCola() -> None:
    for maxCola in [maxCola1, maxCola2,
                    maxCola3, maxCola4]:
        assert maxCola(inserta(3, inserta(5, inserta(1, vacia())))) == 5
