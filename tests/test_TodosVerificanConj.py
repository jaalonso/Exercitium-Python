from src.TodosVerificanConj import (inserta, todos, todos2, todos3, todos4,
                                    vacio)


def test_todos() -> None:
    for todos_ in [todos, todos2, todos3, todos4]:
        assert todos_(lambda x: x % 2 == 0,
                      inserta(4, inserta(6, vacio())))
        assert not todos_(lambda x: x % 2 == 0,
                          inserta(4, inserta(7, vacio())))
