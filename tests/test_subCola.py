from src.subCola import inserta, subCola1, subCola2, subCola3, vacia


def test_subCola() -> None:
    ej1 = inserta(2, inserta(3, vacia()))
    ej2 = inserta(7, inserta(2, inserta(3, inserta(5, vacia()))))
    ej3 = inserta(2, inserta(7, inserta(3, inserta(5, vacia()))))
    for subCola in [subCola1, subCola2, subCola3]:
        assert subCola(ej1, ej2)
        assert not subCola(ej1, ej3)
