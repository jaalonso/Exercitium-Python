# Grafo_Recorridos_en_un_grafo_completo.py
# TAD de los grafos: Recorridos en un grafo completo.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 12-junio-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    recorridos : (list[A]) -> list[list[A]]
# tal que recorridos(xs) es la lista de todos los posibles recorridos
# por el grafo cuyo conjunto de vértices es xs y cada vértice se
# encuentra conectado con todos los otros y los recorridos pasan por
# todos los vértices una vez y terminan en el vértice inicial. Por
# ejemplo,
#    >>> recorridos([2, 5, 3])
#    [[2, 5, 3, 2], [2, 3, 5, 2], [5, 2, 3, 5], [5, 3, 2, 5],
#     [3, 2, 5, 3], [3, 5, 2, 3]]
# ---------------------------------------------------------------------

from itertools import permutations
from typing import TypeVar

A = TypeVar('A')

def recorridos(xs: list[A]) -> list[list[A]]:
    return [(list(y) + [y[0]]) for y in permutations(xs)]

# Verificación
# ============

def test_recorridos() -> None:
    assert recorridos([2, 5, 3]) \
        == [[2, 5, 3, 2], [2, 3, 5, 2], [5, 2, 3, 5], [5, 3, 2, 5],
            [3, 2, 5, 3], [3, 5, 2, 3]]
    print("Verificado")

# La verificación es
#    >>> test_recorridos()
#    Verificado
