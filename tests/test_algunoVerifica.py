from src.algunoVerifica import (algunoVerifica1, algunoVerifica2,
                                algunoVerifica3, algunoVerifica4,
                                algunoVerifica5, inserta, vacia)


def test_algunoVerifica() -> None:
    for algunoVerifica in [algunoVerifica1, algunoVerifica2,
                           algunoVerifica3, algunoVerifica4,
                           algunoVerifica5]:
        assert algunoVerifica(lambda x: x > 0,
                              inserta(-3, inserta(2, vacia())))
        assert not algunoVerifica(lambda x: x > 0,
                                  inserta(-3, inserta(-2, vacia())))
