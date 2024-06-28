# Minimo_producto_escalar.py
# Mínimo producto escalar.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 14-junio-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El producto escalar de los vectores [a1,a2,...,an] y [b1,b2,..., bn]
# es
#    a1 * b1 + a2 * b2 + ··· + an * bn.
#
# Definir la función
#    menorProductoEscalar : (list[int], list[int]) -> int
# tal que menorProductoEscalar(xs, ys) es el mínimo de los productos
# escalares de las permutaciones de xs y de las permutaciones de
# ys. Por ejemplo,
#    menorProductoEscalar([3,2,5],   [1,4,6])    == 29
#    menorProductoEscalar([3,2,5],   [1,4,-6])   == -19
#    menorProductoEscalar3(range(10**2), range(10**2)) == 161700
#    menorProductoEscalar3(range(10**3), range(10**3)) == 166167000
#    menorProductoEscalar3(range(10**4), range(10**4)) == 166616670000
#    menorProductoEscalar3(range(10**5), range(10**5)) == 166661666700000
#    menorProductoEscalar3(range(10**6), range(10**6)) == 166666166667000000
# ---------------------------------------------------------------------

from itertools import permutations
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

# 1ª solución
# ===========

def menorProductoEscalar1(xs: list[int], ys: list[int]) -> int:
    return min(sum(x * y for x, y in zip(pxs, pys))
               for pxs in permutations(xs)
               for pys in permutations(ys))

# 2ª solución
# ===========

def menorProductoEscalar2(xs: list[int], ys: list[int]) -> int:
    return min(sum(x * y for x, y in zip(pxs, ys))
               for pxs in permutations(xs))

# 3ª solución
# ===========

def menorProductoEscalar3(xs: list[int], ys: list[int]) -> int:
    return sum(x * y for x, y in zip(sorted(xs),
                                     sorted(ys, reverse=True)))

# Verificación
# ============

def test_menorProductoEscalar() -> None:
    for menorProductoEscalar in [menorProductoEscalar1,
                                 menorProductoEscalar2,
                                 menorProductoEscalar3]:
        assert menorProductoEscalar([3,2,5], [1,4,6])  == 29
        assert menorProductoEscalar([3,2,5], [1,4,-6]) == -19
    print("Verificado")

# La verificación es
#    λ> verifica
#    6 examples, 0 failures

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(st.integers(min_value=1, max_value=1000), max_size = 6),
       st.lists(st.integers(min_value=1, max_value=1000)))
def test_menorProductoEscalar_equiv(xs: list[int], ys: list[int]) -> None:
    n = min(len(xs), len(ys))
    xs_ = xs[:n]
    ys_ = ys[:n]
    r = menorProductoEscalar1(xs_, ys_)
    assert menorProductoEscalar2(xs_, ys_) == r
    assert menorProductoEscalar3(xs_, ys_) == r

# La comprobación es
#    >>> test_menorProductoEscalar_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('menorProductoEscalar1(range(7), range(7))')
#    23.11 segundos
#    >>> tiempo('menorProductoEscalar2(range(7), range(7))')
#    0.01 segundos
#    >>> tiempo('menorProductoEscalar3(range(7), range(7))')
#    0.00 segundos
#
#    >>> tiempo('menorProductoEscalar2(range(10), range(10))')
#    3.93 segundos
#    >>> tiempo('menorProductoEscalar3(range(10), range(10))')
#    0.00 segundos
