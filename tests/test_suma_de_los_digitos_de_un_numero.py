from src.suma_de_los_digitos_de_un_numero import (sumaDigitos1, sumaDigitos2,
                                                  sumaDigitos3, sumaDigitos4,
                                                  sumaDigitos5)


def test_sumaDigitos() -> None:
    for sumaDigitos in [sumaDigitos1, sumaDigitos2, sumaDigitos3,
                        sumaDigitos4, sumaDigitos5]:
        assert sumaDigitos(3) == 3
        assert sumaDigitos(2454) == 15
        assert sumaDigitos(20045) == 11
