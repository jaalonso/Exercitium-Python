from src.distancia_entre_dos_puntos import distancia


def test_distancia():
    assert distancia((1, 2), (4, 6)) == 5.0
