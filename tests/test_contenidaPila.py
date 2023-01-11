from src.contenidaPila import (contenidaPila1, contenidaPila2,
                               contenidaPila3, contenidaPila4, apila,
                               vacia)

def test_contenidaPila() -> None:
    ej1 = apila(3, apila(2, vacia()))
    ej2 = apila(3, apila(4, vacia()))
    ej3 = apila(5, apila(2, apila(3, vacia())))
    for contenidaPila in [contenidaPila1, contenidaPila2,
                          contenidaPila3, contenidaPila4]:
        assert contenidaPila(ej1, ej3)
        assert not contenidaPila(ej2, ej3)
