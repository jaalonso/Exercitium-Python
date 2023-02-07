from src.TAD_Diferencia_de_conjuntos import (diferencia, diferencia2,
                                             diferencia3, diferencia4, inserta,
                                             vacio)


def test_diferencia() -> None:
    ej1 = inserta(5, inserta(3, inserta(2, inserta(7, vacio()))))
    ej2 = inserta(7, inserta(4, inserta(3, vacio())))
    for diferencia_ in [diferencia, diferencia2, diferencia3,
                        diferencia4]:
        assert str(diferencia_(ej1, ej2)) == "{2, 5}"
        assert str(diferencia_(ej2, ej1)) == "{4}"
        assert str(diferencia_(ej1, ej1)) == "{}"
