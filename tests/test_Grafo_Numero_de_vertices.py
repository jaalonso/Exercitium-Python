from src.Grafo_Numero_de_vertices import nVertices
from src.TAD.Grafo import Orientacion, creaGrafo_


def test_nVertices() -> None:
    assert nVertices(creaGrafo_(Orientacion.D, (1,5), [(1,2),(3,1)])) == 5
    assert nVertices(creaGrafo_(Orientacion.ND, (2,4), [(1,2),(3,1)])) == 3
