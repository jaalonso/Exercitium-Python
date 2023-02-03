from src.TAD_Union_de_varios_conjuntos import (inserta, unionG, unionG2,
                                               unionG3, vacio)


def test_unionG() -> None:
    ej1 = inserta(3, inserta(5, vacio()))
    ej2 = inserta(5, inserta(6, vacio()))
    ej3 = inserta(3, inserta(6, vacio()))
    for unionG_ in [unionG, unionG2, unionG3]:
        assert str(unionG_([ej1, ej2, ej3])) == "{3, 5, 6}"
