from src.TAD_Interseccion_de_varios_conjuntos import (inserta, interseccionG,
                                                      interseccionG2,
                                                      interseccionG3, vacio)


def test_interseccionG() -> None:
    ej1 = inserta(2, inserta(3, inserta(5, vacio())))
    ej2 = inserta(5, inserta(2, inserta(7, vacio())))
    ej3 = inserta(3, inserta(2, inserta(5, vacio())))
    for interseccionG_ in [interseccionG, interseccionG2,
                           interseccionG3]:
        assert str(interseccionG_([ej1, ej2, ej3])) == "{2, 5}"
