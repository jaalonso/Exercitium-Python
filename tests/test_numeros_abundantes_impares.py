from src.numeros_abundantes_impares import (abundantesImpares1,
                                            abundantesImpares2,
                                            abundantesImpares3)


def test_abundantesImpares() -> None:
    assert abundantesImpares1(1000)[0] == 945
    assert abundantesImpares2(1000)[0] == 945
    assert abundantesImpares3(1000)[0] == 945
