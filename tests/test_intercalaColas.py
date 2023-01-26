from src.intercalaColas import (inserta, intercalaColas, intercalaColas2,
                                intercalaColas3, intercalaColas4,
                                intercalaColas5, vacia)


def test_intercalaColas() -> None:
    ej1 = inserta(3, inserta(5, vacia()))
    ej2 = inserta(0, inserta(7, inserta(4, inserta(9, vacia()))))
    for intercalaColas_ in [intercalaColas, intercalaColas2,
                            intercalaColas3, intercalaColas4,
                            intercalaColas5]:
        assert str(intercalaColas_(ej1, ej2)) == "5 | 9 | 3 | 4 | 7 | 0"
        assert str(intercalaColas_(ej2, ej1)) == "9 | 5 | 4 | 3 | 7 | 0"
