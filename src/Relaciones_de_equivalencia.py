# Relaciones_de_equivalencia.py
# Relaciones de equivalencia.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 06-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las relaciones binarias](https://bit.ly/3IVVqOT),
# definir la función
#    esEquivalencia : (Rel[A]) -> bool
# tal que esEquivalencia(r) se verifica si la relación r es de
# equivalencia. Por ejemplo,
#    >>> esEquivalencia (([1,3,5],[(1,1),(1,3),(3,1),(3,3),(5,5)]))
#    True
#    >>> esEquivalencia (([1,2,3,5],[(1,1),(1,3),(3,1),(3,3),(5,5)]))
#    False
#    >>> esEquivalencia (([1,3,5],[(1,1),(1,3),(3,3),(5,5)]))
#    False
# ---------------------------------------------------------------------

from typing import TypeVar

from src.Relaciones_binarias import Rel, relacionArbitraria
from src.Relaciones_reflexivas import reflexiva
from src.Relaciones_simetricas import simetrica
from src.Relaciones_transitivas import transitiva

A = TypeVar('A')

def esEquivalencia(r: Rel[A]) -> bool:
    return reflexiva(r) and simetrica(r) and transitiva(r)
