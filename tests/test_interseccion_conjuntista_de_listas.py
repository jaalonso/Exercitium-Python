from src.interseccion_conjuntista_de_listas\
    import interseccion1, interseccion2, interseccion3, interseccion4

def test_interseccion():
    assert interseccion1([3, 2, 5], [5, 7, 3, 4]) == [3, 5]
    assert interseccion1([3, 2, 5], [9, 7, 6, 4]) == []
    assert interseccion2([3, 2, 5], [5, 7, 3, 4]) == [3, 5]
    assert interseccion2([3, 2, 5], [9, 7, 6, 4]) == []
    assert interseccion3([3, 2, 5], [5, 7, 3, 4]) == [3, 5]
    assert interseccion3([3, 2, 5], [9, 7, 6, 4]) == []
    assert interseccion4([3, 2, 5], [5, 7, 3, 4]) == [3, 5]
    assert interseccion4([3, 2, 5], [9, 7, 6, 4]) == []
