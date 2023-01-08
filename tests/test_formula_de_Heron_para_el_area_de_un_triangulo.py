from src.formula_de_Heron_para_el_area_de_un_triangulo import area


def test_area():
    assert area(3, 4, 5) == 6.0
