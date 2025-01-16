# Suma_de_numeros_amigos_menores_que_n.py
# Suma de los números amigos menores que n
# José A. Alonso Jiménez
# Sevilla, 16-enero-2025
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Dos [números amigos](https://tinyurl.com/2y2ktgb9) son dos números
# enteros positivos distintos tales que la suma de los divisores
# propios de cada uno es igual al otro. Los divisores propios de un
# número incluyen la unidad pero no al propio número. Por ejemplo, los
# divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y
# 110. La suma de estos números equivale a 284. A su vez, los divisores
# propios de 284 son 1, 2, 4, 71 y 142. Su suma equivale a 220. Por
# tanto, 220 y 284 son amigos.
#
# Definir la función
#    sumaAmigosMenores1 : (int) -> int
# tal que (sumaAmigosMenores n) es la suma de los números amigos
# menores que n. Por ejemplo,
#    sumaAmigosMenores(2000)  == 2898
#    sumaAmigosMenores(10**5) == 852810
# ---------------------------------------------------------------------

from functools import reduce
from itertools import count, islice, takewhile
from operator import mul
from timeit import Timer, default_timer
from typing import Iterator

from hypothesis import given
from hypothesis import strategies as st
from sympy import divisor_sigma, factorint, proper_divisors

# 1ª solución
# ===========

# divisoresPropios1(x) es la lista de los divisores propios de x. Por
# ejemplo,
#    divisoresPropios1(220)  ==  [1,2,4,5,10,11,20,22,44,55,110]
#    divisoresPropios1(284)  ==  [1,2,4,71,142]
def divisoresPropios1(x: int) -> list[int]:
    return [n for n in range(1, x) if x % n == 0]

# sumaDivisoresPropios1(x) es la suma de los divisores propios de
# x. Por ejemplo,
#    sumaDivisoresPropios1(220)  ==  284
#    sumaDivisoresPropios1(284)  ==  220
def sumaDivisoresPropios1(x: int) -> int:
    return sum(divisoresPropios1(x))

# sucesionAmigos1() genera los pares de números amigos con la primera
# componente menor que la segunda. Por ejemplo,
#    >>> list(islice(sucesionAmigos1(), 4))
#    [(220, 284), (1184, 1210), (2620, 2924), (5020, 5564)]
def sucesionAmigos1() -> Iterator[tuple[int, int]]:
    return ((x,y) for x in count(1)
            if (y := sumaDivisoresPropios1(x)) > x and sumaDivisoresPropios1(y) == x)

# amigosMenores1(n) es la lista de los pares de números amigos (con la
# primera componente menor que la segunda) que son menores que n. Por
# ejemplo,
#    amigosMenores1(2000)  ==  [(220,284),(1184,1210)]
def amigosMenores1(n: int) -> list[tuple[int, int]]:
    return list(takewhile(lambda par: par[1] < n, sucesionAmigos1()))

def sumaAmigosMenores1(n: int) -> int:
    return sum(x + y for x, y in amigosMenores1(n))

# 2ª solución
# ===========

def divisoresPropios2(x: int) -> list[int]:
    return proper_divisors(x)

def sumaDivisoresPropios2(x: int) -> int:
    return sum(divisoresPropios2(x))

def sucesionAmigos2() -> Iterator[tuple[int, int]]:
    return ((x,y) for x in count(1)
            if (y := sumaDivisoresPropios2(x)) > x and sumaDivisoresPropios2(y) == x)

def amigosMenores2(n: int) -> list[tuple[int, int]]:
    return list(takewhile(lambda par: par[1] < n, sucesionAmigos2()))

def sumaAmigosMenores2(n: int) -> int:
    return sum(x + y for x, y in amigosMenores2(n))

# 3ª solución
# ===========

# Si la descomposición de x en factores primos es
#    x = p(1)^e(1) . p(2)^e(2) . .... . p(n)^e(n)
# entonces la suma de los divisores de x es
#    p(1)^(e(1)+1) - 1     p(2)^(e(2)+1) - 1       p(n)^(e(2)+1) - 1
#   ------------------- . ------------------- ... -------------------
#        p(1)-1                p(2)-1                  p(n)-1
# Ver la demostración en http://bit.ly/2zUXZPc

# producto(xs) es el producto de los elementos de xs. Por ejemplo,
#    producto([2, 3, 5]) == 30
def producto(xs: list[int]) -> int:
    return reduce(mul, xs)

# sumaDivisoresPropios3(x) es la suma de los divisores propios de
# x. Por ejemplo,
#    sumaDivisoresPropios3(220)  ==  284
#    sumaDivisoresPropios3(284)  ==  220
def sumaDivisoresPropios3(x: int) -> int:
    return producto([(p**(e+1)-1) // (p-1)
                     for (p,e) in factorint(x).items()]) - x

def sucesionAmigos3() -> Iterator[tuple[int, int]]:
    return ((x,y) for x in count(2)
            if (y := sumaDivisoresPropios3(x)) > x and sumaDivisoresPropios3(y) == x)

def amigosMenores3(n: int) -> list[tuple[int, int]]:
    return list(takewhile(lambda par: par[1] < n, sucesionAmigos3()))

def sumaAmigosMenores3(n: int) -> int:
    return sum(x + y for x, y in amigosMenores3(n))

# 4ª solución
# ===========

# sumaDivisoresPropios4(x) es la suma de los divisores propios de
# x. Por ejemplo,
#    sumaDivisoresPropios4(220)  ==  284
#    sumaDivisoresPropios4(284)  ==  220
def sumaDivisoresPropios4(x: int) -> int:
    return divisor_sigma(x, 1) - x

def sucesionAmigos4() -> Iterator[tuple[int, int]]:
    return ((x,y) for x in count(2)
            if (y := sumaDivisoresPropios4(x)) > x and sumaDivisoresPropios4(y) == x)

def amigosMenores4(n: int) -> list[tuple[int, int]]:
    return list(takewhile(lambda par: par[1] < n, sucesionAmigos4()))

def sumaAmigosMenores4(n: int) -> int:
    return sum(x + y for x, y in amigosMenores4(n))

# Verificación
# ============

def test_sumaAmigosMenores() -> None:
    for sumaAmigosMenores in [sumaAmigosMenores1, sumaAmigosMenores2,
                           sumaAmigosMenores3, sumaAmigosMenores4]:
        assert sumaAmigosMenores(2000)  == 2898
    print("Verificado")

# La verificación es
#    >>> test_sumaAmigosMenores()
#    Verificado

# Comprobación de la equivalencia de las definiciones
# ===================================================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_sumaAmigosMenores_equiv(n: int) -> None:
    r = sumaAmigosMenores1(n)
    assert sumaAmigosMenores2(n) == r
    assert sumaAmigosMenores3(n) == r
    assert sumaAmigosMenores4(n) == r

# La comprobación es
#    >>> test_sumaAmigosMenores_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('sumaAmigosMenores1(6000)')
#    1.25 segundos
#    >>> tiempo('sumaAmigosMenores1(7000)')
#    3.82 segundos
#    >>> tiempo('sumaAmigosMenores2(7000)')
#    0.16 segundos
#    >>> tiempo('sumaAmigosMenores3(7000)')
#    0.08 segundos
#    >>> tiempo('sumaAmigosMenores4(7000)')
#    0.80 segundos
#
#    >>> tiempo('sumaAmigosMenores2(90000)')
#    1.61 segundos
#    >>> tiempo('sumaAmigosMenores3(90000)')
#    0.93 segundos
