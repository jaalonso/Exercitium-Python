from src.exponente_mayor import \
    mayorExponente1, \
    mayorExponente2, \
    mayorExponente3, \
    mayorExponente4

def test_mayorExponente() -> None:
    for mayorExponente in [mayorExponente1, mayorExponente2,
                           mayorExponente3, mayorExponente4]:
        assert mayorExponente(2, 8) == 3
        assert mayorExponente(2, 9) == 0
        assert mayorExponente(5, 100) == 2
        assert mayorExponente(2, 60) == 2
