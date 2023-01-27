from src.ordenadaCola import (inserta, ordenadaCola, ordenadaCola2,
                              ordenadaCola3, ordenadaCola4, vacia)


def test_ordenadaCola() -> None:
    for ordenadaCola_ in [ordenadaCola, ordenadaCola2, ordenadaCola3,
                          ordenadaCola4]:
        assert ordenadaCola_(inserta(6, inserta(5, inserta(1, vacia()))))
        assert not ordenadaCola_(inserta(1, inserta(0, inserta(6, vacia()))))
