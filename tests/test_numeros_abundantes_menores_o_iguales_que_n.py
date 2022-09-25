from src.numeros_abundantes_menores_o_iguales_que_n import \
    numerosAbundantesMenores1, numerosAbundantesMenores2

def test_numerosAbundantesMenores() -> None:
    r = [12, 18, 20, 24, 30, 36, 40, 42, 48]
    assert numerosAbundantesMenores1(50) == r
    assert numerosAbundantesMenores1(48) == r
    assert numerosAbundantesMenores2(50) == r
    assert numerosAbundantesMenores2(48) == r
