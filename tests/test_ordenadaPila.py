from src.ordenadaPila import (apila, ordenadaPila1, ordenadaPila2,
                              ordenadaPila3, ordenadaPila4, vacia)


def test_ordenadaApila() -> None:
    for ordenadaPila in [ordenadaPila1, ordenadaPila2, ordenadaPila3,
                         ordenadaPila4]:
        assert ordenadaPila(apila(1, apila(5, apila(6, vacia()))))
        assert not ordenadaPila(apila(1, apila(0, apila(6, vacia()))))
