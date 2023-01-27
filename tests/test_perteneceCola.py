from src.perteneceCola import inserta, perteneceCola, perteneceCola2, vacia


def test_perteneceCola() -> None:
    for perteneceCola_ in [perteneceCola, perteneceCola2]:
        assert perteneceCola_(2, inserta(5, inserta(2, inserta(3, vacia()))))
        assert not perteneceCola_(4,
                                  inserta(5, inserta(2, inserta(3, vacia()))))
