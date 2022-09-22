# suma_de_divisores.py
# Suma de divisores.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 1-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    sumaDivisores : (int) -> int
# tal que (sumaDivisores x) es la suma de los divisores de x. Por ejemplo,
#    sumaDivisores(12)                ==  28
#    sumaDivisores(25)                ==  31
#    sumaDivisores (reduce(mul, range(1, 26)))  ==  93383273455325195473152000
#    len(str(sumaDivisores6(reduce(mul, range(1, 30001)))))  ==  121289
# ---------------------------------------------------------------------

from operator import mul
from functools import reduce
from timeit import Timer, default_timer
from sys import setrecursionlimit
from sympy import divisors, divisor_sigma, factorint
from hypothesis import given, strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

# divisores(x) es la lista de los divisores de x. Por ejemplo,
#    divisores(60)  ==  [1,5,3,15,2,10,6,30,4,20,12,60]
def divisores(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if n % x == 0]

def sumaDivisores1(n: int) -> int:
    return sum(divisores(n))

# 2ª solución
# ===========

# Sustituyendo la definición de divisores de la solución anterior por
# cada una de las del ejercicio Divisores de un número https://bit.ly/3S1HYwi)
# Se obtiene una nueva definición de sumaDivisores. La usada en la
# definición anterior es la menos eficiente y la que se usa en la
# siguiente definición es la más eficiente.
def sumaDivisores2(n: int) -> int:
    return sum(divisors(n))

# 3ª solución
# ===========

def sumaDivisores3(n: int) -> int:
    def aux(xs: list[int]) -> int:
        if xs:
            if n % xs[0] == 0:
                return xs[0] + aux(xs[1:])
            return aux(xs[1:])
        return 0

    return aux(list(range(1, n + 1)))

# 4ª solución
# ===========

# Si la descomposición de x en factores primos es
#    x = p(1)^e(1) . p(2)^e(2) . .... . p(n)^e(n)
# entonces la suma de los divisores de x es
#    p(1)^(e(1)+1) - 1     p(2)^(e(2)+1) - 1       p(n)^(e(2)+1) - 1
#   ------------------- . ------------------- ... -------------------
#        p(1)-1                p(2)-1                  p(n)-1
# Ver la demostración en http://bit.ly/2zUXZPc

def sumaDivisores4(n: int) -> int:
    return reduce(mul, [(p ** (e + 1) - 1) // (p - 1)
                        for (p, e) in factorint(n).items()])

# 5ª solución
# ===========

def sumaDivisores5(n: int) -> int:
    x = 1
    r1 = 0
    r2 = 0
    while x * x < n:
        if n % x == 0:
            r1 += x
            r2 += n // x
        x += 1
    if x * x == n:
        r1 += x
    return r1 + r2

# 6ª solución
# ===========

def sumaDivisores6(n: int) -> int:
    return divisor_sigma(n, 1)

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=2, max_value=1000))
def test_sumaDivisores(n):
    r = sumaDivisores1(n)
    assert sumaDivisores2(n) == r
    assert sumaDivisores3(n) == r
    assert sumaDivisores4(n) == r
    assert sumaDivisores5(n) == r
    assert sumaDivisores6(n) == r

# La comprobación es
#    src> poetry run pytest -q suma_de_divisores.py
#    1 passed in 0.90s

# Comparación de eficiencia
# =========================

def tiempo(e):
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('sumaDivisores1(5336100)')
#    0.29 segundos
#    >>> tiempo('sumaDivisores2(5336100)')
#    0.00 segundos
#    >>> tiempo('sumaDivisores3(5336100)')
#    Process Python terminado (killed)
#    >>> tiempo('sumaDivisores4(5336100)')
#    0.00 segundos
#    >>> tiempo('sumaDivisores5(5336100)')
#    0.00 segundos
#    >>> tiempo('sumaDivisores6(5336100)')
#    0.00 segundos
#
#    >>> tiempo('sumaDivisores1(2**9 * 3**8 * 5**2)')
#    4.52 segundos
#    >>> tiempo('sumaDivisores2(2**9 * 3**8 * 5**2)')
#    0.00 segundos
#    >>> tiempo('sumaDivisores4(2**9 * 3**8 * 5**2)')
#    0.00 segundos
#    >>> tiempo('sumaDivisores5(2**9 * 3**8 * 5**2)')
#    0.00 segundos
#    >>> tiempo('sumaDivisores6(2**9 * 3**8 * 5**2)')
#    0.00 segundos
#
#    >>> tiempo('sumaDivisores2(2**9 * 3**8 * 5**7 * 7**4)')
#    0.00 segundos
#    >>> tiempo('sumaDivisores4(2**9 * 3**8 * 5**7 * 7**4)')
#    0.00 segundos
#    >>> tiempo('sumaDivisores5(2**9 * 3**8 * 5**7 * 7**4)')
#    3.24 segundos
#    >>> tiempo('sumaDivisores6(2**9 * 3**8 * 5**7 * 7**4)')
#    0.00 segundos
#
#    >>> tiempo('sumaDivisores2(251888923423315469521109880000000)')
#    1.13 segundos
#    >>> tiempo('sumaDivisores4(251888923423315469521109880000000)')
#    0.00 segundos
#    >>> tiempo('sumaDivisores6(251888923423315469521109880000000)')
#    0.00 segundos
#
#    >>> tiempo('sumaDivisores4(reduce(mul, list(range(1, 30000))))')
#    1.89 segundos
#    >>> tiempo('sumaDivisores6(reduce(mul, list(range(1, 30000))))')
#    1.88 segundos
