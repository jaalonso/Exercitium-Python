from src.todosVerifican import (inserta, todosVerifican1, todosVerifican2,
                                todosVerifican3, todosVerifican4,
                                todosVerifican5, vacia)


def test_todosVerifica() -> None:
    for todosVerifican in [todosVerifican1, todosVerifican2,
                           todosVerifican3, todosVerifican4,
                           todosVerifican5]:
        assert todosVerifican(lambda x: x > 0, inserta(3, inserta(2, vacia())))
        assert not todosVerifican(lambda x: x > 0,
                                  inserta(3, inserta(-2, vacia())))
