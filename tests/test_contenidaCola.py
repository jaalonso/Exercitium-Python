from src.contenidaCola import (contenidaCola1, contenidaCola2, contenidaCola3,
                               contenidaCola4, inserta, vacia)


def test_contenidaCola() -> None:
    ej1 = inserta(3, inserta(2, vacia()))
    ej2 = inserta(3, inserta(4, vacia()))
    ej3 = inserta(5, inserta(2, inserta(3, vacia())))
    for contenidaCola in [contenidaCola1, contenidaCola2,
                          contenidaCola3, contenidaCola4]:
        assert contenidaCola(ej1, ej3)
        assert not contenidaCola(ej2, ej3)
