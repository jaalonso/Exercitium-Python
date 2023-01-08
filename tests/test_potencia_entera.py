from src.potencia_entera import (potencia1, potencia2, potencia3, potencia4,
                                 potencia6)


def test_potencia() -> None:
    for potencia in [potencia1, potencia2, potencia3, potencia4,
                     potencia4, potencia6]:
        assert potencia(2, 3) == 8
