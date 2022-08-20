from src.numero_de_raices_de_la_ecuacion_de_segundo_grado import numeroDeRaices

def test_numeroDeRaices():
    assert numeroDeRaices(2, 0, 3) == 0
    assert numeroDeRaices(4, 4, 1) == 1
    assert numeroDeRaices(5, 23, 12) == 2
