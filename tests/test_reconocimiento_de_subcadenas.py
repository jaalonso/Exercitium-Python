from src.reconocimiento_de_subcadenas import \
    esSubcadena1, esSubcadena2, esSubcadena3

def test_esSubcadena() -> None:
    for esSubcadena in [esSubcadena1, esSubcadena2, esSubcadena3]:
        assert esSubcadena("casa", "escasamente") is True
        assert esSubcadena("cante", "escasamente") is False
        assert esSubcadena("", "") is True
