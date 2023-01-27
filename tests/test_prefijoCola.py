from src.prefijoCola import (inserta, prefijoCola, prefijoCola2, prefijoCola3,
                             prefijoCola4, vacia)


def test_prefijoCola() -> None:
    ej1 = inserta(4, inserta(2, vacia()))
    ej2 = inserta(5, inserta(4, inserta(2, vacia())))
    ej3 = inserta(5, inserta(2, inserta(4, vacia())))
    for prefijoCola_ in [prefijoCola, prefijoCola2,
                         prefijoCola3, prefijoCola4]:
        assert prefijoCola_(ej1, ej2)
        assert not prefijoCola_(ej1, ej3)
