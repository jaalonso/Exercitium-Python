# Factorizaciones_de_numeros_de_Hilbert.py
# Factorizaciones de números de Hilbert.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 24-diciembre-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Un [**número de Hilbert**](http://bit.ly/204SW1p) es un entero
# positivo de la forma 4n+1. Los primeros números de Hilbert son 1, 5,
# 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, ...
#
# Un **primo de Hilbert** es un número de Hilbert n que no es divisible
# por ningún número de Hilbert menor que n (salvo el 1). Los primeros
# primos de Hilbert son 5, 9, 13, 17, 21, 29, 33, 37, 41, 49, 53, 57,
# 61, 69, 73, 77, 89, 93, 97, 101, 109, 113, 121, 129, 133, 137, ...
#
# Definir la función
#    factorizacionesH : (int) -> list[list[int]]
# tal que factorizacionesH(n) es la listas de primos de Hilbert cuyo
# producto es el número de Hilbert n. Por ejemplo,
#   factorizacionesH(25)    ==  [[5,5]]
#   factorizacionesH(45)    ==  [[5,9]]
#   factorizacionesH(441)   ==  [[9,49],[21,21]]
#   factorizacionesH(80109) ==  [[9,9,989],[9,69,129]]
#
# Comprobar con Hypothesis que todos los números de Hilbert son
# factorizables como producto de primos de Hilbert (aunque la
# factorización, como para el 441, puede no ser única).
# ---------------------------------------------------------------------

from itertools import takewhile
from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

from src.Numeros_primos_de_Hilbert import primosH1, primosH2

setrecursionlimit(10**6)

# 1ª solución
# ===========

def factorizacionesH1(m: int) -> list[list[int]]:
    ys = list(takewhile(lambda y: y <= m, primosH1()))
    def aux(zs: list[int], n: int) -> list[list[int]]:
        if not zs:
            return []
        x, *xs = zs
        if x == n:
            return [[n]]
        if x > n:
            return []
        if n % x == 0:
            return [[x] + ns for ns in aux(zs, n // x)] + aux(xs, n)
        return aux(xs, n)
    return aux(ys, m)

# 2ª solución
# ===========

def factorizacionesH2(m: int) -> list[list[int]]:
    ys = list(takewhile(lambda y: y <= m, primosH2()))
    def aux(zs: list[int], n: int) -> list[list[int]]:
        if not zs:
            return []
        x, *xs = zs
        if x == n:
            return [[n]]
        if x > n:
            return []
        if n % x == 0:
            return [[x] + ns for ns in aux(zs, n // x)] + aux(xs, n)
        return aux(xs, n)
    return aux(ys, m)

# Verificación
# ============

def test_factorizacionesH() -> None:
    for factorizacionesH in [factorizacionesH1, factorizacionesH2]:
        assert factorizacionesH(25) == [[5,5]]
        assert factorizacionesH(45) == [[5,9]]
        assert factorizacionesH(441) == [[9,49],[21,21]]
    print("Verificado")

# La verificación es
#    >>> test_factorizacionesH()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_factorizacionesH_equiv(n: int) -> None:
    m = 1 + 4 * n
    assert factorizacionesH1(m) == factorizacionesH2(m)

# La comprobación es
#    >>> test_factorizacionesH_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('factorizacionesH1(80109)')
#    25.40 segundos
#    >>> tiempo('factorizacionesH2(80109)')
#    0.27 segundos

# Propiedad de factorización
# ==========================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_factorizable(n: int) -> None:
    assert factorizacionesH2(1 + 4 * n) != []

# La comprobación es
#    >>> test_factorizable()
#    >>>

# Comprobación de todas las propiedades
# =====================================

# La comprobación es
#    src> poetry run pytest -v Factorizaciones_de_numeros_de_Hilbert.py
#    ===== test session starts =====
#    test_factorizacionesH PASSED
#    test_factorizacionesH_equiv PASSED
#    test_factorizable PASSED
#    ===== 3 passed in 2.25s =====

# ---------------------------------------------------------------------
# § Referencias                                                      --
# ---------------------------------------------------------------------

# Basado en el artículo [Failure of unique factorization (A simple
# example of the failure of the fundamental theorem of
# arithmetic)](http://bit.ly/20A2Nyc) de R.J. Lipton en el blog [Gödel's
# Lost Letter and P=NP](https://rjlipton.wordpress.com).
#
# Otras  referencias
#
# + Wikipedia, [Hilbert number](http://bit.ly/204SW1p).
# + E.W. Weisstein, [Hilbert number](http://bit.ly/204T8O4) en MathWorld.
# + N.J.A. Sloane, [Sucesión A057948](https://oeis.org/A057948) en la
#   OEIS.
# + N.J.A. Sloane, [Sucesión A057949](https://oeis.org/A057949) en la
#   OEIS.
