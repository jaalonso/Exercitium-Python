from src.numeros_libres_de_cuadrados import \
    libreDeCuadrados1, \
    libreDeCuadrados2, \
    libreDeCuadrados3, \
    libreDeCuadrados4

def test_libreDeCuadrados():
    assert libreDeCuadrados1(70) is True
    assert libreDeCuadrados1(40) is False
    assert libreDeCuadrados2(70) is True
    assert libreDeCuadrados2(40) is False
    assert libreDeCuadrados3(70) is True
    assert libreDeCuadrados3(40) is False
    assert libreDeCuadrados4(70) is True
    assert libreDeCuadrados4(40) is False
