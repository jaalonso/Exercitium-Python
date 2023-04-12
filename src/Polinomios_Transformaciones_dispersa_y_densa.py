# Polinomios_Transformaciones_dispersa_y_densa.py
# TAD de los polinomios: Transformaciones entre las representaciones dispersa y densa.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 18-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir las funciones
#    densaAdispersa : (list[A]) -> list[tuple[int, A]]
#    dispersaAdensa : (list[tuple[int, A]]) -> list[A]
# tales que
# + densaAdispersa(xs) es la representación dispersa del polinomio
#   cuya representación densa es xs. Por ejemplo,
#      >>> densaAdispersa([9, 0, 0, 5, 0, 4, 7])
#      [(6, 9), (3, 5), (1, 4), (0, 7)]
# + dispersaAdensa(ps) es la representación densa del polinomio
#   cuya representación dispersa es ps. Por ejemplo,
#      >>> dispersaAdensa([(6,9),(3,5),(1,4),(0,7)])
#      [9, 0, 0, 5, 0, 4, 7]
#
# Comprobar con Hypothesis que las funciones densaAdispersa y
# dispersaAdensa son inversas.
# ---------------------------------------------------------------------

from itertools import dropwhile
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

A = TypeVar('A', int, float, complex)

# 1ª definición de densaAdispersa
# ===============================

def densaAdispersa(xs: list[A]) -> list[tuple[int, A]]:
    n = len(xs)
    return [(m, a) for (m, a) in zip(range(n-1, -1, -1),  xs) if a != 0]

# 2ª definición de densaAdispersa
# ===============================

def densaAdispersa2(xs: list[A]) -> list[tuple[int, A]]:
    def aux(xs: list[A], n: int) -> list[tuple[int, A]]:
        if not xs:
            return []
        if xs[0] == 0:
            return aux(xs[1:], n + 1)
        return [(n, xs[0])] + aux(xs[1:], n + 1)

    return list(reversed(aux(list(reversed(xs)), 0)))

# 3ª definición de densaAdispersa
# ===============================

def densaAdispersa3(xs: list[A]) -> list[tuple[int, A]]:
    r = []
    n = len(xs) - 1
    for x in xs:
        if x != 0:
            r.append((n, x))
        n -= 1
    return r

# Comprobación de equivalencia de densaAdispersa
# ==============================================

# normalDensa(ps) es la representación dispersa de un polinomio.
def normalDensa(xs: list[A]) -> list[A]:
    return list(dropwhile(lambda x: x == 0, xs))

# densaAleatoria() genera representaciones densas de polinomios
# aleatorios. Por ejemplo,
#    >>> densaAleatoria().example()
#    [-5, 9, -6, -5, 7, -5, -1, 9]
#    >>> densaAleatoria().example()
#    [-4, 9, -3, -3, -5, 0, 6, -8, 8, 6, 0, -9]
#    >>> densaAleatoria().example()
#    [-3, -1, 2, 0, -9]
def densaAleatoria() -> st.SearchStrategy[list[int]]:
    return st.lists(st.integers(min_value=-9, max_value=9))\
             .map(lambda xs: normalDensa(xs))

# La propiedad es
@given(xs=densaAleatoria())
def test_densaADispersa(xs: list[int]) -> None:
    r = densaAdispersa(xs)
    assert densaAdispersa2(xs) == r
    assert densaAdispersa3(xs) == r

# 1ª definición de dispersaAdensa
# ===============================

def dispersaAdensa(ps: list[tuple[int, A]]) -> list[A]:
    if not ps:
        return []
    if len(ps) == 1:
        return [ps[0][1]] + [0] * ps[0][0]
    (n, a) = ps[0]
    (m, b) = ps[1]
    return [a] + [0] * (n-m-1) + dispersaAdensa(ps[1:])

# 2ª definición de dispersaAdensa
# ===============================

# coeficiente(ps, n) es el coeficiente del término de grado n en el
# polinomio cuya representación densa es ps. Por ejemplo,
#    coeficiente([(6, 9), (3, 5), (1, 4), (0, 7)], 3)  ==  5
#    coeficiente([(6, 9), (3, 5), (1, 4), (0, 7)], 4)  ==  0
def coeficiente(ps: list[tuple[int, A]], n: int) -> A:
    if not ps:
        return 0
    (m, a) = ps[0]
    if n > m:
        return 0
    if n == m:
        return a
    return coeficiente(ps[1:], n)

def dispersaAdensa2(ps: list[tuple[int, A]]) -> list[A]:
    if not ps:
        return []
    n = ps[0][0]
    return [coeficiente(ps, m) for m in range(n,-1,-1)]

# 3ª definición de dispersaAdensa
# ===============================

def dispersaAdensa3(ps: list[tuple[int, A]]) -> list[A]:
    if not ps:
        return []
    n = ps[0][0]
    r: list[A] = [0] * (n + 1)
    for (m, a) in ps:
        r[n-m] = a
    return r

# Comprobación de equivalencia de dispersaAdensa
# ==============================================

# normalDispersa(ps) es la representación dispersa de un polinomio.
def normalDispersa(ps: list[tuple[int,A]]) -> list[tuple[int,A]]:
    xs = sorted(list({p[0] for p in ps}), reverse=True)
    ys = [p[1] for p in ps]
    return [(x, y) for (x, y) in zip(xs, ys) if y != 0]

# dispersaAleatoria() genera representaciones densas de polinomios
# aleatorios. Por ejemplo,
#    >>> dispersaAleatoria().example()
#    [(5, -6), (2, -1), (0, 2)]
#    >>> dispersaAleatoria().example()
#    [(6, -7)]
#    >>> dispersaAleatoria().example()
#    [(7, 2), (4, 9), (3, 3), (0, -2)]
def dispersaAleatoria() -> st.SearchStrategy[list[tuple[int, int]]]:
    return st.lists(st.tuples(st.integers(min_value=0, max_value=9),
                              st.integers(min_value=-9, max_value=9)))\
             .map(lambda ps: normalDispersa(ps))

# La propiedad es
@given(ps=dispersaAleatoria())
def test_dispersaAdensa(ps: list[tuple[int, int]]) -> None:
    r = dispersaAdensa(ps)
    assert dispersaAdensa2(ps) == r
    assert dispersaAdensa3(ps) == r

# Propiedad
# =========

# La primera propiedad es
@given(xs=densaAleatoria())
def test_dispersaAdensa_densaAdispersa(xs: list[int]) -> None:
    assert dispersaAdensa(densaAdispersa(xs)) == xs

# La segunda propiedad es
@given(ps=dispersaAleatoria())
def test_densaAdispersa_dispersaAdensa(ps: list[tuple[int, int]]) -> None:
    assert densaAdispersa(dispersaAdensa(ps)) == ps

# La comprobación es
#    > poetry run pytest -v Polinomios_Transformaciones_dispersa_y_densa.py
#    test_densaADispersa PASSED
#    test_dispersaAdensa PASSED
#    test_dispersaAdensa_densaAdispersa PASSED
#    test_densaAdispersa_dispersaAdensa PASSED
