from src.suma_de_los_cuadrados_de_los_primeros_numeros_naturales import (
    sumaDeCuadrados1, sumaDeCuadrados2, sumaDeCuadrados3, sumaDeCuadrados4,
    sumaDeCuadrados5, sumaDeCuadrados6)


def test_suma_de_los_cuadrados_de_los_primeros_numeros_naturales():
    assert sumaDeCuadrados1(3) == 14
    assert sumaDeCuadrados1(100) == 338350
    assert sumaDeCuadrados2(3) == 14
    assert sumaDeCuadrados2(100) == 338350
    assert sumaDeCuadrados3(3) == 14
    assert sumaDeCuadrados3(100) == 338350
    assert sumaDeCuadrados4(3) == 14
    assert sumaDeCuadrados4(100) == 338350
    assert sumaDeCuadrados5(3) == 14
    assert sumaDeCuadrados5(100) == 338350
    assert sumaDeCuadrados6(3) == 14
    assert sumaDeCuadrados6(100) == 338350
