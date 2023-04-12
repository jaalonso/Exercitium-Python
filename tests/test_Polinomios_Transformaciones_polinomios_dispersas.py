from src.Polinomios_Transformaciones_polinomios_dispersas import \
    (dispersaApolinomio, dispersaApolinomio2, polinomioAdispersa)

from src.TAD.Polinomio import (polCero, consPol)

def test_Transformaciones_polinomios_dispersas() -> None:
    for dispersaApolinomio_ in [dispersaApolinomio,
                                dispersaApolinomio2]:
        assert str(dispersaApolinomio_([(6, 9), (3, 5), (1, 4), (0, 7)]))\
            == "9*x^6 + 5*x^3 + 4*x + 7"
    ejPol = consPol(6, 9, consPol(3, 5, consPol(1, 4, consPol(0, 7, polCero()))))
    assert polinomioAdispersa(ejPol) == [(6, 9), (3, 5), (1, 4), (0, 7)]
