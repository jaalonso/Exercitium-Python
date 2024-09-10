# Sumas_de_dos_abundantes.py
# Sucesión de sumas de dos números abundantes.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 4-septiembre-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Un número n es [abundante](http://bit.ly/1vySpf2) si la suma de los
# divisores propios de n es mayor que n. El primer número abundante es
# el 12 (cuyos divisores propios son 1, 2, 3, 4 y 6 cuya suma es
# 16). Por tanto, el menor número que es la suma de dos números
# abundantes es el 24.
#
# Definir la sucesión
#    sumasDeDosAbundantes() -> Iterator[int]
# cuyos elementos son los números que se pueden escribir como suma de
# dos números abundantes. Por ejemplo,
#    >>> list(islice(sumasDeDosAbundantes(), 10))
#    [24, 30, 32, 36, 38, 40, 42, 44, 48, 50]
# ---------------------------------------------------------------------

from functools import reduce
from itertools import count, islice, takewhile
from operator import mul
from timeit import Timer, default_timer
from typing import Iterator

from sympy import divisor_sigma, factorint

# 1ª solución
# ===========

# divisores(n) es la lista de los divisores propios de n. Por ejemplo,
#    divisores(12)  ==  [1,2,3,4,6]
def divisores(n: int) -> list[int]:
    return [x for x in range(1, 1 + n // 2) if n % x == 0]

# abundante(n) se verifica si n es abundante. Por ejemplo,
#    abundante(12)  ==  True
#    abundante(11)  ==  False
def abundante(n: int) -> bool:
    return sum(divisores(n)) > n

# abundantes es la lista de los números abundantes. Por ejemplo,
#    >>> list(islice(abundantes(), 10))
#    [12, 18, 20, 24, 30, 36, 40, 42, 48, 54]
def abundantes() -> Iterator[int]:
    return (n for n in count(2) if abundante(n))

# esSumaDeDosAbundantes(n) se verifica si n es suma de dos números
# abundantes. Por ejemplo,
#    esSumaDeDosAbundantes(24)                           ==  True
#    any(esSumaDeDosAbundantes(n) for n in range(1, 23)) == False
def esSumaDeDosAbundantes(n: int) -> bool:
    xs = list(takewhile(lambda x: x <= n, abundantes()))
    return any(n - x in xs for x in xs)

def sumasDeDosAbundantes1() -> Iterator[int]:
    return (n for n in count(1) if esSumaDeDosAbundantes(n))

# 2ª solución
# ===========

# Si la descomposición de x en factores primos es
#    x = p(1)^e(1) . p(2)^e(2) . .... . p(n)^e(n)
# entonces la suma de los divisores de x es
#    p(1)^(e(1)+1) - 1     p(2)^(e(2)+1) - 1       p(n)^(e(2)+1) - 1
#   ------------------- . ------------------- ... -------------------
#        p(1)-1                p(2)-1                  p(n)-1
# Ver la demostración en http://bit.ly/2zUXZPc

# sumaDivisores(n) es la suma de los divisores propios de n. Por
# ejemplo,
#    sumaDivisores(12)  ==  16
def sumaDivisores(n: int) -> int:
    return reduce(mul, [(p ** (e + 1) - 1) // (p - 1)
                        for (p, e) in factorint(n).items()]) - n

def abundante2(n: int) -> bool:
    return sumaDivisores(n) > n

def abundantes2() -> Iterator[int]:
    return (n for n in count(2) if abundante2(n))

def esSumaDeDosAbundantes2(n: int) -> bool:
    xs = list(takewhile(lambda x: x <= n, abundantes2()))
    return any(n - x in xs for x in xs)

def sumasDeDosAbundantes2() -> Iterator[int]:
    return (n for n in count(1) if esSumaDeDosAbundantes2(n))

# 3ª solución
# ===========

def sumaDivisores2(n: int) -> int:
    return divisor_sigma(n, 1) - n

def abundante3(n: int) -> bool:
    return sumaDivisores2(n) > n

def abundantes3() -> Iterator[int]:
    return (n for n in count(2) if abundante3(n))

def esSumaDeDosAbundantes3(n: int) -> bool:
    xs = list(takewhile(lambda x: x <= n, abundantes3()))
    return any(n - x in xs for x in xs)

def sumasDeDosAbundantes3() -> Iterator[int]:
    return (n for n in count(1) if esSumaDeDosAbundantes3(n))

# Verificación
# ============

def test_sumasDeDosAbundantes() -> None:
    for sumasDeDosAbundantes in [sumasDeDosAbundantes1,
                                 sumasDeDosAbundantes2,
                                 sumasDeDosAbundantes3]:
        assert list(islice(sumasDeDosAbundantes(), 10)) ==\
            [24, 30, 32, 36, 38, 40, 42, 44, 48, 50]
    print("Verificado")

# La verificación es
#    >>> test_sumasDeDosAbundantes()
#    Verificado

# Comprobación de equivalencia
# ============================

# nth(i, n) es el n-ésimo elemento del iterador i. Por ejemplo,
#    nth(sumasDeDosAbundantes1(), 4) == 38
def nth(i: Iterator[int], n: int) -> int:
    return list(islice(i, n, n+1))[0]

# La propiedad es
def test_sumasDeDosAbundantes_equiv(n: int) -> bool:
    return list(islice(sumasDeDosAbundantes1(), n)) ==\
           list(islice(sumasDeDosAbundantes2(), n)) ==\
           list(islice(sumasDeDosAbundantes3(), n))

# La comprobación es
#    >>> test_sumasDeDosAbundantes_equiv(400)
#    True

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('nth(sumasDeDosAbundantes1(), 500)')
#    3.83 segundos
#    >>> tiempo('nth(sumasDeDosAbundantes2(), 500)')
#    2.30 segundos
#    >>> tiempo('nth(sumasDeDosAbundantes3(), 500)')
#    1.92 segundos

# ---------------------------------------------------------------------
# § Referencias                                                      --
# ---------------------------------------------------------------------

# + A048260: The sum of 2 (not necessarily distinct) abundant numbers.
#   https://oeis.org/A048260
#
# + E23: Non-abundant sums. Euler Project http://bit.ly/1A1vScr
