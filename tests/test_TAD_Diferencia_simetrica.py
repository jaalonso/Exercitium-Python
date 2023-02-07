from src.TAD_Diferencia_simetrica import (diferenciaSimetrica,
                                          diferenciaSimetrica2,
                                          diferenciaSimetrica3, inserta, vacio)


def test_diferenciaSimetrica() -> None:
    ej1 = inserta(5, inserta(3, inserta(2, inserta(7, vacio()))))
    ej2 = inserta(7, inserta(4, inserta(3, vacio())))
    for diferenciaSimetrica_ in [diferenciaSimetrica,
                                 diferenciaSimetrica2,
                                 diferenciaSimetrica3]:
        assert str(diferenciaSimetrica_(ej1, ej2)) == "{2, 4, 5}"
