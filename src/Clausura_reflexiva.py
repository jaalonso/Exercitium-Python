# Clausura_reflexiva.py
# Clausura reflexiva.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 12-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las relaciones binarias](https://bit.ly/3IVVqOT),
# definir la función
#    clausuraReflexiva : (Rel[A]) -> Rel[A]
# tal que clausuraReflexiva(r) es la clausura reflexiva de r; es
# decir, la menor relación reflexiva que contiene a r. Por ejemplo,
#    >>> clausuraReflexiva (([1,3],[(1,1),(3,1)]))
#    ([1, 3], [(3, 1), (1, 1), (3, 3)])
# ---------------------------------------------------------------------

from typing import TypeVar

from src.Relaciones_binarias import Rel

A = TypeVar('A')

def clausuraReflexiva(r: Rel[A]) -> Rel[A]:
    (u, g) = r
    return (u, list(set(g) | {(x, x) for x in u}))
