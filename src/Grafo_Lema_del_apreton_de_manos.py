# Grafo_Lema_del_apreton_de_manos.py
# TAD de los grafos: Lema del apretón de manos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 7-junio-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# En la teoría de grafos, se conoce como "Lema del apretón de manos" la
# siguiente propiedad: la suma de los grados de los vértices de g es el
# doble del número de aristas de g.
#
# Comprobar con QuickCheck que para cualquier grafo g, se verifica
# dicha propiedad.
# ---------------------------------------------------------------------

from hypothesis import given

from src.TAD.Grafo import (nodos)
from src.TAD.GrafoGenerador import gen_grafo
from src.Grafo_Grado_de_un_vertice import (grado)
from src.Grafo_Numero_de_aristas_de_un_grafo import (nAristas)

# La propiedad es
@given(gen_grafo())
def test_apreton(g):
    assert sum((grado(g, v) for v in nodos(g))) == 2 * nAristas(g)

# La comprobación es
#    src> poetry run pytest -q Grafo_Lema_del_apreton_de_manos.py
#    1 passed in 0.32s
