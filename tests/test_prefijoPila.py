from src.prefijoPila import (apila, prefijoPila1, prefijoPila2, prefijoPila3,
                             prefijoPila4, vacia)


def test_prefijoPila() -> None:
    ej1 = apila(4, apila(2, vacia()))
    ej2 = apila(4, apila(2, apila(5, vacia())))
    ej3 = apila(5, apila(4, apila(2, vacia())))
    for prefijoPila in [prefijoPila1, prefijoPila2,
                        prefijoPila3, prefijoPila4]:
        assert prefijoPila(ej1, ej2)
        assert not prefijoPila(ej1, ej3)
