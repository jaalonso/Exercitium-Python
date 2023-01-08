from src.aplica_segun_propiedad import (filtraAplica1, filtraAplica2,
                                        filtraAplica3, filtraAplica4,
                                        filtraAplica5)


def test_filtraAplica() -> None:
    for filtraAplica in [filtraAplica1, filtraAplica2, filtraAplica3,
                         filtraAplica4, filtraAplica5]:
        assert filtraAplica(lambda x: x + 4,
                            lambda x: x < 3,
                            list(range(1, 7))) == [5, 6]
