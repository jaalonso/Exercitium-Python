from src.TAD_subconjunto import (inserta, subconjunto, subconjunto2,
                                 subconjunto3, subconjunto4, subconjunto5,
                                 vacio)


def test_subconjunto() -> None:
    ej1 = inserta(5, inserta(2, vacio()))
    ej2 = inserta(3, inserta(2, inserta(5, vacio())))
    ej3 = inserta(3, inserta(4, inserta(5, vacio())))
    for subconjunto_ in [subconjunto, subconjunto2, subconjunto3,
                         subconjunto4, subconjunto5]:
        assert subconjunto_(ej1, ej2)
        assert not subconjunto_(ej1, ej3)
