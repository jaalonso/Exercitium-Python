from src.ultimoCola import (inserta, ultimoCola, ultimoCola2, ultimoCola3,
                            ultimoCola4, ultimoCola5, vacia)


def test_ultimoCola() -> None:
    for ultimoCola_ in [ultimoCola, ultimoCola2, ultimoCola3,
                        ultimoCola4, ultimoCola5]:
        assert ultimoCola_(inserta(3, inserta(5, inserta(2, vacia())))) == 3
        assert ultimoCola(inserta(2, vacia())) == 2
