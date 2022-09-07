# numeros_libres_de_cuadrados.py
# Números libres de cuadrados.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 26-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Un número es libre de cuadrados si no es divisible por el cuadrado de
# ningún entero mayor que 1. Por ejemplo, 70 es libre de cuadrado
# porque sólo es divisible por 1, 2, 5, 7 y 70; en cambio, 40 no es
# libre de cuadrados porque es divisible por 2^2.
#
# Definir la función
#    libreDeCuadrados : (int) -> bool
# tal que (ibreDeCuadrados(x) se verifica si x es libre de cuadrados.
# Por ejemplo,
#    libreDeCuadrados(70)  ==  True
#    libreDeCuadrados(40)  ==  False
#    libreDeCuadrados (product (take 30000 primes))  ==  True
# ---------------------------------------------------------------------

from timeit import Timer, default_timer
from sys import setrecursionlimit
from sympy import primefactors, primerange
from hypothesis import given, strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

def libreDeCuadrados1(n: int) -> bool:
    return [x for x in range(2, n + 2) if n % (x**2) == 0] == []

# 2ª solución
# ===========

# divisores(n) es la lista de los divisores del número n. Por ejemplo,
#    divisores(30)  ==  [1,2,3,5,6,10,15,30]
def divisores1(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if n % x == 0]

# primo(n) se verifica si n es primo. Por ejemplo,
#    primo(30)  == False
#    primo(31)  == True
def primo1(n: int) -> bool:
    return divisores1(n) == [1, n]

# divisoresPrimos(x) es la lista de los divisores primos de x. Por
# ejemplo,
#    divisoresPrimos(40) == [2, 5]
#    divisoresPrimos(70) == [2, 5, 7]
def divisoresPrimos1(x: int) -> list[int]:
    return [n for n in divisores1(x) if primo1(n)]

# producto(xs) es el producto de los elementos de xs. Por ejemplo,
#    producto([3, 2, 5])  ==  30
def producto(xs):
    if xs:
        return xs[0] * producto(xs[1:])
    return 1

def libreDeCuadrados2(x):
    return x == producto(divisoresPrimos1(x))

# 3ª solución
# ===========

def libreDeCuadrados3(n: int) -> bool:
    if n % 2 == 0:
        return n % 4 != 0 and libreDeCuadrados3(n // 2)

    def aux(m, xs):
        if m == 1:
            return True
        if xs == []:
            return True
        if m % xs[0] == 0:
            return m % (xs[0]**2) != 0 and aux(m // xs[0], xs[1:])
        return aux(m, xs[1:])
    return aux(n, range(3, n + 1, 2))

# 4ª solución
# ===========

def libreDeCuadrados4(x):
    return x == producto(primefactors(x))

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=2, max_value=1000))
def test_libreDeCuadrados(n):
    assert libreDeCuadrados1(n) ==\
           libreDeCuadrados2(n) ==\
           libreDeCuadrados3(n) ==\
           libreDeCuadrados4(n)

# La comprobación es
#    src> poetry run pytest -q numeros_libres_de_cuadrados.py
#    1 passed in 0.59s

# Comparación de eficiencia
# =========================

def tiempo(e):
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('libreDeCuadrados1(9699690)')
#    2.66 segundos
#    >>> tiempo('libreDeCuadrados2(9699690)')
#    2.58 segundos
#    >>> tiempo('libreDeCuadrados3(9699690)')
#    0.00 segundos
#    >>> tiempo('libreDeCuadrados4(9699690)')
#    0.00 segundos
#
#    >>> n = producto(list(primerange(1, 25000)))
#    >>> tiempo('libreDeCuadrados3(n)')
#    0.42 segundos
#    >>> tiempo('libreDeCuadrados4(n)')
#    0.14 segundos
