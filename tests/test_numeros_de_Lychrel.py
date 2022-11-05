from src.numeros_de_Lychrel import \
    esCapicua, \
    inverso, \
    siguiente, \
    busquedaDeCapicua, \
    capicuaFinal, \
    orden, \
    ordenMayor, \
    ordenEntre, \
    menorDeOrdenMayor, \
    menoresdDeOrdenMayor, \
    islice

def test_Lychrel() -> None:
    assert esCapicua(252) is True
    assert esCapicua(253) is False
    assert inverso(253) == 352
    assert siguiente(253) == 605
    assert busquedaDeCapicua(253) == [253, 605, 1111]
    assert capicuaFinal(253) == 1111
    assert orden(253) == 2
    assert ordenMayor(1186060307891929990, 2) is True
    assert orden(1186060307891929990) == 261
    assert list(islice(ordenEntre(10, 11), 5)) == \
        [829, 928, 9059, 9149, 9239]
    assert menorDeOrdenMayor(2) == 19
    assert menorDeOrdenMayor(20) == 89
    assert menoresdDeOrdenMayor(5) == \
        [(1, 10), (2, 19), (3, 59), (4, 69), (5, 79)]
