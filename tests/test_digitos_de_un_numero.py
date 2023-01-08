from src.digitos_de_un_numero import (digitos1, digitos2, digitos3, digitos4,
                                      digitos5, digitos6, digitos7)


def test_digitos() -> None:
    for digitos in [digitos1, digitos2, digitos3, digitos4, digitos5,
                    digitos6, digitos7]:
        assert digitos(320274) == [3, 2, 0, 2, 7, 4]
