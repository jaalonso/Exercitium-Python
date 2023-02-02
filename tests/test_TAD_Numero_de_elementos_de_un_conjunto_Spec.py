from src.TAD_Numero_de_elementos_de_un_conjunto import (cardinal, cardinal2,
                                                        cardinal3, cardinal4,
                                                        inserta, vacio)


def test_cardinal() -> None:
    for cardinal_ in [cardinal, cardinal2, cardinal3, cardinal4]:
        assert cardinal_(inserta(4, inserta(5, vacio()))) == 2
        assert cardinal_(inserta(4, inserta(5, inserta(4, vacio())))) == 2
