from src.division_segura import divisionSegura1, divisionSegura2


def test_divisionSegura():
    assert divisionSegura1(7, 2) == 3.5
    assert divisionSegura1(7, 0) == 9999.0
    assert divisionSegura2(7, 2) == 3.5
    assert divisionSegura2(7, 0) == 9999.0
