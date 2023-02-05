from src.TAD_Interseccion_de_dos_conjuntos import (inserta, interseccion,
                                                   interseccion2,
                                                   interseccion3,
                                                   interseccion4, vacio)


def test_interseccion() -> None:
    for interseccion_ in [interseccion, interseccion2, interseccion3,
                          interseccion4]:
        ej1 = inserta(3, inserta(5, inserta(2, vacio())))
        ej2 = inserta(2, inserta(4, inserta(3, vacio())))
        assert str(interseccion_(ej1, ej2)) == "{2, 3}"
