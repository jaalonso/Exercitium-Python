from src.representacion_densa_de_polinomios import densa1, densa2, densa3


def test_densa() -> None:
    for densa in [densa1, densa2, densa3]:
        assert densa([6, 0, -5, 4, -7]) == [(4, 6), (2, -5), (1, 4), (0, -7)]
        assert densa([6, 0, 0, 3, 0, 4]) == [(5, 6), (2, 3), (0, 4)]
        assert densa([0]) == [(0, 0)]
