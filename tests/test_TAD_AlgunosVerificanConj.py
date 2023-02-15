from src.TAD_AlgunosVerificanConj import (algunos, algunos2, algunos3,
                                          algunos4, inserta, vacio)


def test_algunos() -> None:
    for algunos_ in [algunos, algunos2, algunos3, algunos4]:
        assert algunos_(lambda x: x % 2 == 0,
                        inserta(4, inserta(7, vacio())))
        assert not algunos_(lambda x: x % 2 == 0,
                            inserta(3, inserta(7, vacio())))
