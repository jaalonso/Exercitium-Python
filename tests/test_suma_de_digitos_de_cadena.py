from src.suma_de_digitos_de_cadena import (sumaDigitos1, sumaDigitos2,
                                           sumaDigitos3)


def test_sumaDigitos() -> None:
    for sumaDigitos in [sumaDigitos1, sumaDigitos2, sumaDigitos3]:
        assert sumaDigitos("SE 2431 X") == 10
