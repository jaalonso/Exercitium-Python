from src.Pol_Division_de_Ruffini_con_representacion_densa import ruffiniDensa


def test_ruffiniDensa() -> None:
    assert ruffiniDensa(2, [1, 2, -1, -2]) == [1, 4, 7, 12]
    assert ruffiniDensa(1, [1, 2, -1, -2]) == [1, 3, 2, 0]
