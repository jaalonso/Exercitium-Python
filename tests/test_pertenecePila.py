from src.pertenecePila import (pertenecePila1, pertenecePila2,
                               pertenecePila3, pertenecePila4, apila,
                               vacia)

def test_pertenecePila() -> None:
    for pertenecePila in [pertenecePila1, pertenecePila2,
                          pertenecePila3, pertenecePila4]:
        assert pertenecePila(2, apila(5, apila(2, apila(3, vacia()))))
        assert not pertenecePila(4, apila(5, apila(2, apila(3, vacia()))))
