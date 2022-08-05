from src.area_corona_circular import areaDeCoronaCircular


def test_areaDeCoronaCircular():
    assert areaDeCoronaCircular(1, 2) == 9.42477796076938
    assert areaDeCoronaCircular(2, 5) == 65.97344572538566
    assert areaDeCoronaCircular(3, 5) == 50.26548245743669
