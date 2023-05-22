from src.Grafo_Incidentes_de_un_vertice import incidentes
from src.TAD.Grafo import Orientacion, creaGrafo_


def test_incidentes() -> None:
    g1 = creaGrafo_(Orientacion.D, (1,3), [(1,2),(2,2),(3,1),(3,2)])
    g2 = creaGrafo_(Orientacion.ND, (1,3), [(1,2),(2,2),(3,1),(3,2)])
    assert incidentes(g1,1) == [3]
    assert incidentes(g1,2) == [1, 2, 3]
    assert incidentes(g1,3) == []
    assert incidentes(g2, 1) == [2, 3]
    assert incidentes(g2, 2) == [1, 2, 3]
    assert incidentes(g2, 3) == [1, 2]
