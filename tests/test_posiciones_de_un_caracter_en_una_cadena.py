from src.posiciones_de_un_caracter_en_una_cadena import \
    posiciones1, posiciones2, posiciones3

def test_posiciones() -> None:
    for posiciones in [posiciones1, posiciones2, posiciones3]:
        assert posiciones('a', "Salamamca") == [1, 3, 5, 8]
