from src.TAD_Particion_por_una_propiedad import (inserta, particion,
                                                 particion2, particion3, vacio)


def test_particion() -> None:
    ej = inserta(5, inserta(4, inserta(7, inserta(2, vacio()))))
    for particion_ in [particion, particion2, particion3]:
        assert str(particion_(lambda x: x % 2 == 0, ej)) == "({2, 4}, {5, 7})"
