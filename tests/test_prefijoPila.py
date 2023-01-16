from src.prefijoPila import (apila, prefijoPila, prefijoPila2, prefijoPila3,
                             prefijoPila4, vacia)


def test_prefijoPila() -> None:
    ej1 = apila(4, apila(2, vacia()))
    ej2 = apila(4, apila(2, apila(5, vacia())))
    ej3 = apila(5, apila(4, apila(2, vacia())))
    for prefijoPila_ in [prefijoPila, prefijoPila2,
                         prefijoPila3, prefijoPila4]:
        assert prefijoPila_(ej1, ej2)
        assert not prefijoPila_(ej1, ej3)
