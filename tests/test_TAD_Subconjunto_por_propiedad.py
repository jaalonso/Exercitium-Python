from src.TAD_Subconjunto_por_propiedad import (filtra, filtra2, filtra3,
                                               filtra4, inserta, vacio)


def test_filtra() -> None:
    ej = inserta(5, inserta(4, inserta(7, inserta(2, vacio()))))
    for filtra_ in [filtra, filtra2, filtra3, filtra4]:
        assert str(filtra_(lambda x: x % 2 == 0, ej)) == "{2, 4}"
        assert str(filtra_(lambda x: x % 2 == 1, ej)) == "{5, 7}"
