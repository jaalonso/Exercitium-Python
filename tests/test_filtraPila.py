from src.filtraPila import (apila, filtraPila1, filtraPila2, filtraPila3,
                            filtraPila4, vacia)


def test_filtraApila() -> None:
    ej = apila(3, apila(4, apila(6, apila(5, vacia()))))
    for filtraPila in [filtraPila1, filtraPila2, filtraPila3, filtraPila4]:
        assert str(filtraPila(lambda x: x % 2 == 0, ej)) == "4 | 6"
        assert str(filtraPila(lambda x: x % 2 == 1, ej)) == "3 | 5"
    assert str(ej) == "3 | 4 | 6 | 5"
