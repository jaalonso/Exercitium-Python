from src.suma_de_monedas import sumaMonedas

def test_sumaMonedas():
    assert sumaMonedas(0, 0, 0, 0, 1) == 20
    assert sumaMonedas(0, 0, 8, 0, 3) == 100
    assert sumaMonedas(1, 1, 1, 1, 1) == 38
