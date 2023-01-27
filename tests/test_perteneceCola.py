from src.perteneceCola import \
    (perteneceCola, perteneceCola2, vacia, inserta)

def test_perteneceCola() -> None:
    for perteneceCola_ in [perteneceCola, perteneceCola2]:
        assert perteneceCola_(2, inserta(5, inserta(2, inserta(3, vacia()))))
        assert not perteneceCola_(4,
                                  inserta(5, inserta(2, inserta(3, vacia()))))
