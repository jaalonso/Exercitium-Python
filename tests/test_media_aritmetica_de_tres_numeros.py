from src.media_aritmetica_de_tres_numeros import media3a, media3b


def test_media3():
    assert media3a(1, 3, 8) == 4.0
    assert media3a(-1, 0, 7) == 2.0
    assert media3a(-3, 0, 3) == 0.0
    assert media3b(1, 3, 8) == 4.0
    assert media3b(-1, 0, 7) == 2.0
    assert media3b(3, 0, -3) == 0.0
