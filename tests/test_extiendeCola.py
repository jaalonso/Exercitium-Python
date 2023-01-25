from src.extiendeCola import (extiendeCola, extiendeCola2, extiendeCola3,
                              extiendeCola4, extiendeCola5, inserta, vacia)


def test_extiendeCola() -> None:
    ej1 = inserta(3, inserta(2, vacia()))
    ej2 = inserta(5, inserta(3, inserta(4, vacia())))
    for extiendeCola_ in [extiendeCola, extiendeCola2, extiendeCola3,
                          extiendeCola4, extiendeCola5]:
        assert str(extiendeCola_(ej1, ej2)) == "2 | 3 | 4 | 3 | 5"
        assert str(extiendeCola_(ej2, ej1)) == "4 | 3 | 5 | 2 | 3"
