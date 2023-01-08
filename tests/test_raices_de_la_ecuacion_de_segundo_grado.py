from src.raices_de_la_ecuacion_de_segundo_grado import raices


def test_raices():
    assert raices(1, 3, 2) == [-1.0, -2.0]
    assert raices(1, (-2), 1) == [1.0, 1.0]
    assert not raices(1, 0, 1)
