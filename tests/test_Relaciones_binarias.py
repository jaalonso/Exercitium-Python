from src.Relaciones_binarias import (esRelacionBinaria, esRelacionBinaria2,
                                     esRelacionBinaria3)


def test_esRelacionBinaria() -> None:
    for esRelacionBinaria_ in [esRelacionBinaria, esRelacionBinaria2,
                               esRelacionBinaria3]:
        assert esRelacionBinaria_(([1, 3], [(3, 1), (3, 3)]))
        assert not esRelacionBinaria_(([1, 3], [(3, 1), (3, 2)]))
