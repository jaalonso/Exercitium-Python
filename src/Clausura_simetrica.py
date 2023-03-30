# Clausura_simetrica.py
# Clausura simétrica.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 13-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las relaciones binarias](https://bit.ly/3IVVqOT),
# definir la función
#    clausuraSimetrica : (Rel[A]) -> Rel[A]
# tal que clausuraSimetrica(r) es la clausura simétrica de r; es
# decir, la menor relación simétrica que contiene a r. Por ejemplo,
#    >>> clausuraSimetrica(([1, 3, 5], [(1, 1), (3, 1), (1, 5)]))
#    ([1, 3, 5], [(1, 5), (3, 1), (1, 1), (1, 3), (5, 1)])
#
# Comprobar con Hypothesis que clausuraSimetrica es simétrica.
# ---------------------------------------------------------------------

from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.Relaciones_binarias import Rel, relacionArbitraria
from src.Relaciones_simetricas import simetrica

A = TypeVar('A')

def clausuraSimetrica(r: Rel[A]) -> Rel[A]:
    (u, g) = r
    return (u, list(set(g) | {(y, x) for (x,y) in g}))

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=0, max_value=10))
def test_irreflexiva(n: int) -> None:
    r = relacionArbitraria(n)
    assert simetrica(clausuraSimetrica(r))

# La función simetrica está definida en el ejercicio
# "Relaciones simétricas" que se encuentra en
# https://bit.ly/3zlO2rH

# La comprobación es
#    > poetry run pytest -q Clausura_simetrica.py
#    1 passed in 0.12s
