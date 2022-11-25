from src.el_tipo_de_los_numeros_naturales import \
    nat2int, int2nat, suma, Cero, Suc

def test_naturales() -> None:
    assert nat2int(Suc(Suc(Suc(Cero())))) == 3
    assert int2nat(3) == Suc(Suc(Suc(Cero())))
    assert suma(Suc(Suc(Cero())), Suc(Cero())) == Suc(Suc(Suc(Cero())))
    assert nat2int(suma(Suc(Suc(Cero())), Suc(Cero()))) == 3
    assert nat2int(suma(int2nat(2), int2nat(1))) == 3
