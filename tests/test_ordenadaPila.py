from src.ordenadaPila import (apila, ordenadaPila, ordenadaPila2,
                              ordenadaPila3, ordenadaPila4, vacia)


def test_ordenadaApila() -> None:
    for ordenadaPila_ in [ordenadaPila, ordenadaPila2, ordenadaPila3,
                          ordenadaPila4]:
        assert ordenadaPila_(apila(1, apila(5, apila(6, vacia()))))
        assert not ordenadaPila_(apila(1, apila(0, apila(6, vacia()))))
