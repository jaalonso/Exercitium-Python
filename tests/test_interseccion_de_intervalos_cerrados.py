from src.interseccion_de_intervalos_cerrados import interseccion

def test_interseccion():
    assert not interseccion([], [3, 5])
    assert not interseccion([3, 5], [])
    assert not interseccion([2, 4], [6, 9])
    assert interseccion([2, 6], [6, 9]) == [6, 6]
    assert interseccion([2, 6], [0, 9]) == [2, 6]
    assert interseccion([2, 6], [0, 4]) == [2, 4]
    assert interseccion([4, 6], [0, 4]) == [4, 4]
    assert not interseccion([5, 6], [0, 4])
