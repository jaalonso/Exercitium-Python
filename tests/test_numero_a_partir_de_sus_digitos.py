from src.numero_a_partir_de_sus_digitos import \
    listaNumero1, \
    listaNumero2, \
    listaNumero3, \
    listaNumero4, \
    listaNumero5, \
    listaNumero6

def test_listaNumero() -> None:
    for listaNumero in [listaNumero1, listaNumero2, listaNumero3,
                        listaNumero4, listaNumero5, listaNumero6]:
        assert listaNumero([5]) == 5
        assert listaNumero([1, 3, 4, 7]) == 1347
        assert listaNumero([0, 0, 1]) == 1
