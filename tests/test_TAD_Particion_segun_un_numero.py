from src.TAD_Particion_segun_un_numero import (divide, divide2, divide3,
                                               divide4, inserta, vacio)


def test_particion() -> None:
    for divide_ in [divide, divide2, divide3, divide4]:
        assert str(divide_(5, inserta(7, inserta(2, inserta(8, vacio())))))\
            == "({2}, {7, 8})"
