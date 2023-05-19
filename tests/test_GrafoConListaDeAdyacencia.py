# pylint: disable=protected-access
# pylint: disable=line-too-long

from src.TAD.GrafoConListaDeAdyacencia import (Grafo, Orientacion, adyacentes,
                                               aristaEn, aristas, creaGrafo,
                                               dirigido, nodos, peso)

ejGrafoND: Grafo = Grafo(Orientacion.ND,
                         (1, 5),
                         [((1, 2), 12), ((1, 3), 34), ((1, 5), 78),
                          ((2, 4), 55), ((2, 5), 32),
                          ((3, 4), 61), ((3, 5), 44),
                          ((4, 5), 93)])

ejGrafoD: Grafo = Grafo(Orientacion.D,
                        (1,5),
                        [((1, 2), 12), ((1, 3), 34), ((1, 5), 78),
                         ((2, 4), 55), ((2, 5), 32),
                         ((3, 4), 61), ((3, 5), 44),
                         ((4, 5), 93)])

ejGrafoND2: Grafo = creaGrafo(Orientacion.ND,
                              (1,5),
                              [((1,2),12),((1,3),34),((1,5),78),
                               ((2,4),55),((2,5),32),
                               ((3,4),61),((3,5),44),
                               ((4,5),93)])

ejGrafoD2: Grafo = creaGrafo(Orientacion.D,
                             (1,5),
                             [((1,2),12),((1,3),34),((1,5),78),
                              ((2,4),55),((2,5),32),
                              ((3,4),61),((3,5),44),
                              ((4,5),93)])

def test_GrafoConListaDeAdyacencia() -> None:
    assert str(Grafo(Orientacion.D, (1,3), [((1,2),0),((3,2),0),((2,2),0)])) \
        == "G D ([1, 2, 3], [(1, 2), (2, 2), (3, 2)])"
    assert str (Grafo(Orientacion.ND, (1,3), [((1,2),0),((3,2),0),((2,2),0)])) \
        == "G ND ([1, 2, 3], [(1, 2), (2, 2), (2, 3)])"
    assert str(Grafo(Orientacion.ND, (1,3), [((1,2),0),((3,2),5),((2,2),0)])) \
        == "G ND ([1, 2, 3], [((1, 2), 0), ((2, 2), 0), ((2, 3), 5)])"
    assert str(Grafo(Orientacion.D, (1,3), [((1,2),0),((3,2),5),((2,2),0)])) \
        == "G D ([1, 2, 3], [((1, 2), 0), ((2, 2), 0), ((3, 2), 5)])"
    assert str(ejGrafoND) == \
        "G ND ([1, 2, 3, 4, 5], [((1, 2), 12), ((1, 3), 34), ((1, 5), 78), ((2, 4), 55), ((2, 5), 32), ((3, 4), 61), ((3, 5), 44), ((4, 5), 93)])"
    assert str(ejGrafoD) == \
        "G D ([1, 2, 3, 4, 5], [((1, 2), 12), ((1, 3), 34), ((1, 5), 78), ((2, 4), 55), ((2, 5), 32), ((3, 4), 61), ((3, 5), 44), ((4, 5), 93)])"
    assert ejGrafoD.dirigido()
    assert not ejGrafoND.dirigido()
    assert ejGrafoND.nodos() == [1, 2, 3, 4, 5]
    assert ejGrafoD.nodos() == [1, 2, 3, 4, 5]
    assert ejGrafoND.adyacentes(4) == [2, 3, 5]
    assert ejGrafoD.adyacentes(4) == [5]
    assert ejGrafoND.aristaEn((5, 1))
    assert not ejGrafoND.aristaEn((4, 1))
    assert not ejGrafoD.aristaEn((5, 1))
    assert ejGrafoD.aristaEn((1, 5))
    assert ejGrafoND.peso(1, 5) == 78
    assert ejGrafoD.peso(1, 5) == 78
    assert str(ejGrafoD._aristas) == "[((1, 2), 12), ((1, 3), 34), ((1, 5), 78), ((2, 4), 55), ((2, 5), 32), ((3, 4), 61), ((3, 5), 44), ((4, 5), 93)]"
    assert str(ejGrafoND._aristas) == "[((1, 2), 12), ((1, 3), 34), ((1, 5), 78), ((2, 1), 12), ((2, 4), 55), ((2, 5), 32), ((3, 1), 34), ((3, 4), 61), ((3, 5), 44), ((4, 2), 55), ((4, 3), 61), ((4, 5), 93), ((5, 1), 78), ((5, 2), 32), ((5, 3), 44), ((5, 4), 93)]"
    assert str(creaGrafo(Orientacion.D, (1,3), [((1,2),0),((3,2),0),((2,2),0)])) \
        == "G D ([1, 2, 3], [(1, 2), (2, 2), (3, 2)])"
    assert str (creaGrafo(Orientacion.ND, (1,3), [((1,2),0),((3,2),0),((2,2),0)])) \
        == "G ND ([1, 2, 3], [(1, 2), (2, 2), (2, 3)])"
    assert str(creaGrafo(Orientacion.ND, (1,3), [((1,2),0),((3,2),5),((2,2),0)])) \
        == "G ND ([1, 2, 3], [((1, 2), 0), ((2, 2), 0), ((2, 3), 5)])"
    assert str(creaGrafo(Orientacion.D, (1,3), [((1,2),0),((3,2),5),((2,2),0)])) \
        == "G D ([1, 2, 3], [((1, 2), 0), ((2, 2), 0), ((3, 2), 5)])"
    assert str(ejGrafoND2) == \
        "G ND ([1, 2, 3, 4, 5], [((1, 2), 12), ((1, 3), 34), ((1, 5), 78), ((2, 4), 55), ((2, 5), 32), ((3, 4), 61), ((3, 5), 44), ((4, 5), 93)])"
    assert str(ejGrafoD2) == \
        "G D ([1, 2, 3, 4, 5], [((1, 2), 12), ((1, 3), 34), ((1, 5), 78), ((2, 4), 55), ((2, 5), 32), ((3, 4), 61), ((3, 5), 44), ((4, 5), 93)])"
    assert dirigido(ejGrafoD2)
    assert not dirigido(ejGrafoND2)
    assert nodos(ejGrafoND2) == [1, 2, 3, 4, 5]
    assert nodos(ejGrafoD2) == [1, 2, 3, 4, 5]
    assert adyacentes(ejGrafoND2, 4) == [2, 3, 5]
    assert adyacentes(ejGrafoD2, 4) == [5]
    assert aristaEn(ejGrafoND2, (5,1))
    assert not aristaEn(ejGrafoND2, (4,1))
    assert not aristaEn(ejGrafoD2, (5,1))
    assert aristaEn(ejGrafoD2, (1,5))
    assert peso(1, 5, ejGrafoND2) == 78
    assert peso(1, 5, ejGrafoD2) == 78
    assert str(aristas(ejGrafoD2)) == "[((1, 2), 12), ((1, 3), 34), ((1, 5), 78), ((2, 4), 55), ((2, 5), 32), ((3, 4), 61), ((3, 5), 44), ((4, 5), 93)]"
    assert str(aristas(ejGrafoND2)) == "[((1, 2), 12), ((1, 3), 34), ((1, 5), 78), ((2, 1), 12), ((2, 4), 55), ((2, 5), 32), ((3, 1), 34), ((3, 4), 61), ((3, 5), 44), ((4, 2), 55), ((4, 3), 61), ((4, 5), 93), ((5, 1), 78), ((5, 2), 32), ((5, 3), 44), ((5, 4), 93)]"
