from src.media_aritmetica_de_tres_numeros import media3


def test_media3():
    assert media3(1, 3, 8) == 4.0
    assert media3(-1, 0, 7) == 2.0
    assert media3(-3, 0, 3) == 0.0
