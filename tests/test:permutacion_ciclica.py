from src.permutacion_ciclica import ciclo

def test_ciclo():
    assert ciclo([2, 5, 7, 9]) == [9, 2, 5, 7]
    assert ciclo([]) == []
    assert ciclo([2]) == [2]
