# Grafo_Coloreado_correcto_de_un_mapa.py
# TAD de los grafos: Coloreado correcto de un mapa.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 19-junio-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
#  Un mapa se puede representar mediante un grafo donde los vértices
#  son las regiones del mapa y hay una arista entre dos vértices si las
#  correspondientes regiones son vecinas. Por ejemplo, el mapa siguiente
#    +----------+----------+
#    |    1     |     2    |
#    +----+-----+-----+----+
#    |    |           |    |
#    | 3  |     4     | 5  |
#    |    |           |    |
#    +----+-----+-----+----+
#    |    6     |     7    |
#    +----------+----------+
# se pueden representar por
#    mapa: Grafo = creaGrafo_(Orientacion.ND,
#                             (1,7),
#                             [(1,2),(1,3),(1,4),(2,4),(2,5),(3,4),
#                              (3,6),(4,5),(4,6),(4,7),(5,7),(6,7)])
#
# Para colorear el mapa se dispone de 4 colores definidos por
#    Color = Enum('Color', ['A', 'B', 'C', 'E'])
#
# Usando el [tipo abstracto de datos de los grafos](https://bit.ly/45cQ3Fo),
# definir la función,
#    correcta : (list[tuple[int, Color]], Grafo) -> bool
# tal que (correcta ncs m) se verifica si ncs es una coloración del
# mapa m tal que todos las regiones vecinas tienen colores distintos.
# Por ejemplo,
#    correcta [(1,A),(2,B),(3,B),(4,C),(5,A),(6,A),(7,B)] mapa == True
#    correcta [(1,A),(2,B),(3,A),(4,C),(5,A),(6,A),(7,B)] mapa == False
# ---------------------------------------------------------------------


from enum import Enum

from src.TAD.Grafo import Grafo, Orientacion, aristas, creaGrafo_

mapa: Grafo = creaGrafo_(Orientacion.ND,
                         (1,7),
                         [(1,2),(1,3),(1,4),(2,4),(2,5),(3,4),
                          (3,6),(4,5),(4,6),(4,7),(5,7),(6,7)])

Color = Enum('Color', ['A', 'B', 'C', 'E'])

def correcta(ncs: list[tuple[int, Color]], g: Grafo) -> bool:
    def color(x: int) -> Color:
        return [c for (y, c) in ncs if y == x][0]
    return all(color(x) != color(y) for ((x, y), _) in aristas(g))

# Verificación
# ============

def test_correcta() -> None:
    assert correcta([(1,Color.A),
                     (2,Color.B),
                     (3,Color.B),
                     (4,Color.C),
                     (5,Color.A),
                     (6,Color.A),
                     (7,Color.B)],
                    mapa)
    assert not correcta([(1,Color.A),
                         (2,Color.B),
                         (3,Color.A),
                         (4,Color.C),
                         (5,Color.A),
                         (6,Color.A),
                         (7,Color.B)],
                        mapa)
    print("Verificado")

# La verificación es
#    >>> test_correcta()
#    Verificado
