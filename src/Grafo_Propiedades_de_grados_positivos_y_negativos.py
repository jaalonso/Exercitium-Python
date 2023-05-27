# Grafo_Propiedades_de_grados_positivos_y_negativos.hs
# TAD de los grafos: Propiedades de grados positivos y negativos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 5-junio-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Comprobar con Hypothesis que para cualquier grafo g, las sumas de los
# grados positivos y la de los grados negativos de los vértices de g son
# iguales
# ---------------------------------------------------------------------

from hypothesis import given

from src.Grafo_Grados_positivos_y_negativos import gradoNeg, gradoPos
from src.TAD.Grafo import nodos
from src.TAD.GrafoGenerador import gen_grafo


# La propiedad es
@given(gen_grafo())
def test_sumaGrados(g):
    vs = nodos(g)
    assert sum((gradoPos(g, v) for v in vs)) == sum((gradoNeg(g, v) for v in vs))

# La comprobación es
#    src> poetry run pytest -q Grafo_Propiedades_de_grados_positivos_y_negativos.py
#    1 passed in 0.31s
