from src.pertenecePila import (apila, pertenecePila, pertenecePila2,
                               pertenecePila3, pertenecePila4, vacia)


def test_pertenecePila() -> None:
    for pertenecePila_ in [pertenecePila, pertenecePila2,
                           pertenecePila3, pertenecePila4]:
        assert pertenecePila_(2, apila(5, apila(2, apila(3, vacia()))))
        assert not pertenecePila_(4, apila(5, apila(2, apila(3, vacia()))))
