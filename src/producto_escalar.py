# producto_escalar.py
# Producto escalar
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 19-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El producto escalar de dos listas de enteros xs y ys de longitud n
# viene dado por la suma de los productos de los elementos
# correspondientes.
#
# Definir la función
#    productoEscalar : (list[int], list[int]) -> int
# tal que productoEscalar(xs, ys) es el producto escalar de las listas
# xs e ys. Por ejemplo,
#    productoEscalar([1, 2, 3], [4, 5, 6])  ==  32
# ---------------------------------------------------------------------

from timeit import Timer, default_timer
from operator import mul
from numpy import dot
from sys import setrecursionlimit

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

def productoEscalar1(xs: list[int], ys: list[int]) -> int:
    return sum(x * y for (x, y) in zip(xs, ys))

# 2ª solución
# ===========

def productoEscalar2(xs: list[int], ys: list[int]) -> int:
    return sum(map(mul, xs, ys))

# 3ª solución
# ===========

def productoEscalar3(xs: list[int], ys: list[int]) -> int:
    if xs and ys:
        return xs[0] * ys[0] + productoEscalar3(xs[1:], ys[1:])
    return 0

# 4ª solución
# ===========

def productoEscalar4(xs: list[int], ys: list[int]) -> int:
    return dot(xs, ys)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(st.integers(min_value=1, max_value=100)),
       st.lists(st.integers(min_value=1, max_value=100)))
def test_productoEscalar(xs: list[int], ys: list[int]) -> None:
    r = productoEscalar1(xs, ys)
    assert productoEscalar2(xs, ys) == r
    assert productoEscalar3(xs, ys) == r
    n = min(len(xs), len(ys))
    xs1 = xs[:n]
    ys1 = ys[:n]
    assert productoEscalar4(xs1, ys1) == r

# La comprobación es
#    src> poetry run pytest -q producto_escalar.py
#    1 passed in 0.37s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('productoEscalar1([1]*(10**4), [1]*(10**4))')
#    0.00 segundos
#    >>> tiempo('productoEscalar3([1]*(10**4), [1]*(10**4))')
#    0.55 segundos
#
#    >>> tiempo('productoEscalar1([1]*(10**7), [1]*(10**7))')
#    0.60 segundos
#    >>> tiempo('productoEscalar2([1]*(10**7), [1]*(10**7))')
#    0.26 segundos
#    >>> tiempo('productoEscalar4([1]*(10**7), [1]*(10**7))')
#    1.73 segundos
