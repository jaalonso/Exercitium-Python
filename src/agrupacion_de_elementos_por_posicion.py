# agrupacion_de_elementos_por_posicion.py
# Agrupación de elementos por posición.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 17-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    agrupa : (list[list[A]]) -> list[list[A]]
# tal que agrupa(xss) es la lista de las listas obtenidas agrupando
# los primeros elementos, los segundos, ... Por ejemplo,
#    >>> agrupa([[1,6],[7,8,9],[3,4,5]])
#    [[1, 7, 3], [6, 8, 4]]
#
# Comprobar con QuickChek que la longitud de todos los elementos de
# (agrupa xs) es igual a la longitud de xs.
# ---------------------------------------------------------------------

from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st
from numpy import array, transpose

setrecursionlimit(10**6)

A = TypeVar('A')

# 1ª solución
# ===========

# primeros(xss) es la lista de los primeros elementos de xss. Por
# ejemplo,
#    primeros([[1,6],[7,8,9],[3,4,5]])  ==  [1, 7, 3]
def primeros(xss: list[list[A]]) -> list[A]:
    return [xs[0] for xs in xss]

# restos(xss) es la lista de los restos de elementos de xss. Por
# ejemplo,
#    >>> restos([[1,6],[7,8,9],[3,4,5]])
#    [[6], [8, 9], [4, 5]]
def restos(xss: list[list[A]]) -> list[list[A]]:
    return [xs[1:] for xs in xss]

def agrupa1(xss: list[list[A]]) -> list[list[A]]:
    if not xss:
        return []
    if [] in xss:
        return []
    return [primeros(xss)] + agrupa1(restos(xss))

# 2ª solución
# ===========

# conIgualLongitud(xss) es la lista obtenida recortando los elementos
# de xss para que todos tengan la misma longitud. Por ejemplo,
#    >>> conIgualLongitud([[1,6],[7,8,9],[3,4,5]])
#    [[1, 6], [7, 8], [3, 4]]
def conIgualLongitud(xss: list[list[A]]) -> list[list[A]]:
    n = min(map(len, xss))
    return [xs[:n] for xs in xss]

def agrupa2(xss: list[list[A]]) -> list[list[A]]:
    yss = conIgualLongitud(xss)
    return [[ys[i] for ys in yss] for i in range(len(yss[0]))]

# 3ª solución
# ===========

def agrupa3(xss: list[list[A]]) -> list[list[A]]:
    yss = conIgualLongitud(xss)
    return list(map(list, zip(*yss)))

# 4ª solución
# ===========

def agrupa4(xss: list[list[A]]) -> list[list[A]]:
    yss = conIgualLongitud(xss)
    return (transpose(array(yss))).tolist()

# 5ª solución
# ===========

def agrupa5(xss: list[list[A]]) -> list[list[A]]:
    yss = conIgualLongitud(xss)
    r = []
    for i in range(len(yss[0])):
        f = []
        for xs in xss:
            f.append(xs[i])
        r.append(f)
    return r

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(st.lists(st.integers()), min_size=1))
def test_agrupa(xss: list[list[int]]) -> None:
    r = agrupa1(xss)
    assert agrupa2(xss) == r
    assert agrupa3(xss) == r
    assert agrupa4(xss) == r
    assert agrupa5(xss) == r

# La comprobación es
#    src> poetry run pytest -q agrupacion_de_elementos_por_posicion.py
#    1 passed in 0.74s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('agrupa1([list(range(10**3)) for _ in range(10**3)])')
#    4.44 segundos
#    >>> tiempo('agrupa2([list(range(10**3)) for _ in range(10**3)])')
#    0.10 segundos
#    >>> tiempo('agrupa3([list(range(10**3)) for _ in range(10**3)])')
#    0.10 segundos
#    >>> tiempo('agrupa4([list(range(10**3)) for _ in range(10**3)])')
#    0.12 segundos
#    >>> tiempo('agrupa5([list(range(10**3)) for _ in range(10**3)])')
#    0.15 segundos
#
#    >>> tiempo('agrupa2([list(range(10**4)) for _ in range(10**4)])')
#    21.25 segundos
#    >>> tiempo('agrupa3([list(range(10**4)) for _ in range(10**4)])')
#    20.82 segundos
#    >>> tiempo('agrupa4([list(range(10**4)) for _ in range(10**4)])')
#    13.46 segundos
#    >>> tiempo('agrupa5([list(range(10**4)) for _ in range(10**4)])')
#    21.70 segundos

# La propiedad es
@given(st.lists(st.lists(st.integers()), min_size=1))
def test_agrupa_length(xss: list[list[int]]) -> None:
    n = len(xss)
    assert all((len(xs) == n for xs in agrupa2(xss)))

# La comprobación es
#    src> poetry run pytest -q agrupacion_de_elementos_por_posicion.py
#    2 passed in 1.25s
