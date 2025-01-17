# Elementos_minimales.hs
# Determinación de los elementos minimales.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 17-enero-2025
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    minimales :: Ord a => [[a]] -> [[a]]
# tal que (minimales xss) es la lista de los elementos de xss que no
# están contenidos en otros elementos de xss. Por ejemplo,
#    minimales([[1,3],[2,3,1],[3,2,5]])        ==  [[2,3,1],[3,2,5]]
#    minimales([[1,3],[2,3,1],[3,2,5],[3,1]])  ==  [[2,3,1],[3,2,5]]
#    map sum (minimales [[1..n] | n <- [1..300]])  ==  [45150]
# ---------------------------------------------------------------------

from collections import Counter
from timeit import Timer, default_timer
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

A = TypeVar('A')

# 1ª solución
# ===========

# subconjuntoPropio(xs, ys) se verifica si xs es un subconjunto propio
# de ys. Por ejemplo,
#    subconjuntoPropio1([1,3], [3,1,3])    ==  False
#    subconjuntoPropio1([1,3,1], [3,1,2])  ==  True
def subconjuntoPropio1(xs: list[A],
                       ys: list[A]) -> bool:
    def aux(ws: list[A], vs: list[A]) -> bool:
        if not vs:
            return False
        if not ws:
            return True
        u, us = ws[0], ws[1:]
        if u in vs:
            vs.remove(u)
            return aux(us, vs)
        return False
    return aux(list(Counter(xs).keys()), list(Counter(ys).keys()))

def minimales1(xss: list[list[A]]) -> list[list[A]]:
    return [xs for xs in xss
            if not any(subconjuntoPropio1(xs, ys) for ys in xss)]

# 2ª solución
# ===========

# subconjunto(xs, ys) se verifica si xs es un subconjunto de ys. Por
# ejemplo,
#    subconjunto([1,3], [3,1,3])        ==  True
#    subconjunto([1,3,1,3], [3,1,3])    ==  True
#    subconjunto([1,3,2,3], [3,1,3])    ==  False
#    subconjunto([1,3,1,3], [3,1,3,2])  ==  True
def subconjunto(xs: list[A],
                ys: list[A]) -> bool:
    return all(x in ys for x in xs)

def subconjuntoPropio2(xs: list[A],
                       ys: list[A]) -> bool:
    return subconjunto(xs, ys) and not subconjunto(ys, xs)

def minimales2(xss: list[list[A]]) -> list[list[A]]:
    return [xs for xs in xss
            if not any(subconjuntoPropio2(xs, ys) for ys in xss)]

# 3ª solución
# ===========

def subconjuntoPropio3(xs: list[A],
                       ys: list[A]) -> bool:
    return set(xs) < set(ys)

def minimales3(xss: list[list[A]]) -> list[list[A]]:
    return [xs for xs in xss
            if not any(subconjuntoPropio3(xs, ys) for ys in xss)]

# Verificación
# ============

def test_minimales() -> None:
    for minimales in [minimales1, minimales2, minimales3]:
        assert minimales([[1,3],[2,3,1],[3,2,5]]) == [[2,3,1],[3,2,5]]
        assert minimales([[1,3],[2,3,1],[3,2,5],[3,1]]) == [[2,3,1],[3,2,5]]
    print("Verificado")

# La verificación es
#    >>> test_minimales()
#    Verificado

# Equivalencia de las definiciones
# ================================

# La propiedad es
@given(st.lists(st.lists(st.integers()), min_size=1))
def test_minimales_equiv(xss: list[list[int]]) -> None:
    r = minimales1(xss)
    assert minimales2(xss) == r
    assert minimales3(xss) == r

# La comprobación es
#    >>> test_minimales_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('minimales1([range(1, n) for n in range(1, 300)])')
#    3.08 segundos
#    >>> tiempo('minimales2([range(1, n) for n in range(1, 300)])')
#    0.46 segundos
#    >>> tiempo('minimales3([range(1, n) for n in range(1, 300)])')
#    0.21 segundos
#
#    >>> tiempo('minimales2([range(1, n) for n in range(1, 500)])')
#    1.92 segundos
#    >>> tiempo('minimales3([range(1, n) for n in range(1, 500)])')
#    0.96 segundos
