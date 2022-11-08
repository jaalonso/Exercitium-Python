from src.mayuscula_inicial import \
    mayusculaInicial1, mayusculaInicial2, mayusculaInicial3

def test_mayusculaInicial() -> None:
    for mayusculaInicial in [mayusculaInicial1, mayusculaInicial2,
                             mayusculaInicial3]:
        assert mayusculaInicial("sEviLLa") == "Sevilla"
        assert mayusculaInicial("") == ""
