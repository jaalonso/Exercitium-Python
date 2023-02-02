from src.TAD_Union_de_dos_conjuntos import (inserta, union, union2, union3,
                                            union4, vacio)


def test_union() -> None:
    ej1 = inserta(3, inserta(5, vacio()))
    ej2 = inserta(4, inserta(3, vacio()))
    for union_ in [union, union2, union3, union4]:
        assert str(union_(ej1, ej2)) == "{3, 4, 5}"
