from src.longitudCola import (inserta, longitudCola1, longitudCola2,
                              longitudCola3, longitudCola4, longitudCola5,
                              vacia)


def test_longitudCola() -> None:
    for longitudCola in [longitudCola1, longitudCola2, longitudCola3,
                         longitudCola4, longitudCola5]:
        assert longitudCola(inserta(4, inserta(2, inserta(5, vacia())))) == 3
