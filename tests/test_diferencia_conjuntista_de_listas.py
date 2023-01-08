from src.diferencia_conjuntista_de_listas import (diferencia1, diferencia2,
                                                  diferencia3, diferencia4)


def test_diferencia():
    assert diferencia1([3, 2, 5, 6], [5, 7, 3, 4]) == [2, 6]
    assert diferencia1([3, 2, 5], [5, 7, 3, 2])    == []
    assert diferencia2([3, 2, 5, 6], [5, 7, 3, 4]) == [2, 6]
    assert diferencia2([3, 2, 5], [5, 7, 3, 2])    == []
    assert diferencia3([3, 2, 5, 6], [5, 7, 3, 4]) == [2, 6]
    assert diferencia3([3, 2, 5], [5, 7, 3, 2])    == []
    assert diferencia4([3, 2, 5, 6], [5, 7, 3, 4]) == [2, 6]
    assert diferencia4([3, 2, 5], [5, 7, 3, 2])    == []
