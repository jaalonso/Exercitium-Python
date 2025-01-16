# Sucesion_de_numeros_amigos.py
# Sucesión de números amigos
# José A. Alonso Jiménez
# Sevilla, 15-enero-2025
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Dos [números amigos](https://tinyurl.com/2y2ktgb9) son dos números
# enteros  positivos distintos tales que la suma de los divisores
# propios de cada uno es igual al otro. Los divisores propios de un
# número incluyen la unidad pero no al propio número. Por ejemplo, los
# divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y
# 110. La suma de estos números equivale a 284. A su vez, los divisores
# propios de 284 son 1, 2, 4, 71 y 142. Su suma equivale a 220. Por
# tanto, 220 y 284 son amigos.
#
# Definir la función
#    sucesionAmigos1() -> Iterator[list[tuple[int, int]]]
# cuyos elementos son los pares de números amigos con la primera
# componente menor que la segunda. Por ejemplo,
#    >>> list(islice(sucesionAmigos1(), 4))
#    [(220, 284), (1184, 1210), (2620, 2924), (5020, 5564)]
# ---------------------------------------------------------------------

from functools import reduce
from itertools import count, islice
from operator import mul
from timeit import Timer, default_timer
from typing import Iterator

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

def sucesionAmigos1() -> Iterator[tuple[int, int]]:
    return ((x,y) for x in count(1)
            if (y := sumaDivisoresPropios1(x)) > x and sumaDivisoresPropios1(y) == x)

# 2ª solución
# ===========

def divisoresPropios2(x: int) -> list[int]:
    return proper_divisors(x)

def sumaDivisoresPropios2(x: int) -> int:
    return sum(divisoresPropios2(x))

def sucesionAmigos2() -> Iterator[tuple[int, int]]:
    return ((x,y) for x in count(1)
            if (y := sumaDivisoresPropios2(x)) > x and sumaDivisoresPropios2(y) == x)

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

# Verificación
# ============

def test_sucesionAmigos() -> None:
    for sucesionAmigos in [sucesionAmigos1, sucesionAmigos2,
                           sucesionAmigos3, sucesionAmigos4]:
        assert list(islice(sucesionAmigos(), 4)) ==\
            [(220, 284), (1184, 1210), (2620, 2924), (5020, 5564)]
    print("Verificado")

# La verificación es
#    >>> test_sucesionAmigos()
#    Verificado

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('list(islice(sucesionAmigos1(), 6))')
#    3.73 segundos
#    >>> tiempo('list(islice(sucesionAmigos2(), 6))')
#    0.14 segundos
#    >>> tiempo('list(islice(sucesionAmigos3(), 6))')
#    0.08 segundos
#    >>> tiempo('list(islice(sucesionAmigos4(), 6))')
#    0.79 segundos
#
#    >>> tiempo('list(islice(sucesionAmigos2(), 14))')
#    1.59 segundos
#    >>> tiempo('list(islice(sucesionAmigos3(), 14))')
#    0.96 segundos
