# Reconocimiento_de_potencias_de_4.py
# Reconocimiento de potencias de 4.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 14-marzo-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    esPotenciaDe4 : (int) -> bool
# tal que esPotenciaDe4(n) se verifica si n es una potencia de 4. Por
# ejemplo,
#    esPotenciaDe4(16)                ==  True
#    esPotenciaDe4(17)                ==  False
#    esPotenciaDe4(4**(4*10**5))      ==  True
#    esPotenciaDe4(1 + 4**(4*10**5))  ==  False
# ---------------------------------------------------------------------

from itertools import count, dropwhile, islice
from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import Callable, Iterator

setrecursionlimit(10**6)

# 1ª solución
# ===========

def esPotenciaDe4_1(n: int) -> bool:
    if n == 0:
        return False
    if n == 1:
        return True
    return n % 4 == 0 and esPotenciaDe4_1(n // 4)

# 2ª solución
# ===========

# potenciassDe4() es la lista de las potencias de 4. Por ejemplo,
#    >>> list(islice(potenciasDe4(), 5))
#    [1, 4, 16, 64, 256]
def potenciasDe4() -> Iterator[int]:
    return (4 ** n for n in count())

# pertenece(x, ys) se verifica si x pertenece a la lista ordenada
# (posiblemente infinita xs). Por ejemplo,
#    >>> pertenece(8, count(2, 2))
#    True
#    >>> pertenece(9, count(2, 2))
#    False
def pertenece(x: int, ys: Iterator[int]) -> bool:
    return next(dropwhile(lambda y: y < x, ys), None) == x

def esPotenciaDe4_2(n: int) -> bool:
    return pertenece(n, potenciasDe4())

# 3ª solución
# ===========

# iterate(f, x) es el iterador obtenido aplicando f a x y continuando
# aplicando f al resultado anterior. Por ejemplo,
#    >>> list(islice(iterate(lambda x : 4 * x, 1), 5))
#    [1, 4, 16, 64, 256]
def iterate(f: Callable[[int], int], x: int) -> Iterator[int]:
    r = x
    while True:
        yield r
        r = f(r)

def potenciasDe4_2() -> Iterator[int]:
    return iterate(lambda x : 4 * x, 1)

def esPotenciaDe4_3(n: int) -> bool:
    return pertenece(n, potenciasDe4_2())

# 4ª solución
# ===========

def esPotenciaDe4_4(n: int) -> bool:
    return next(dropwhile(lambda y: y < n,
                          iterate(lambda x : 4 * x, 1)),
                          None) == n

# 5ª solución
# ===========

def esPotenciaDe4_5(n: int) -> bool:
    r = 1
    while r < n:
        r = 4 * r
    return r == n

# Verificación
# ============

def test_esPotenciaDe4() -> None:
    for esPotenciaDe4 in [esPotenciaDe4_1, esPotenciaDe4_2,
                          esPotenciaDe4_3, esPotenciaDe4_4,
                          esPotenciaDe4_5]:
        assert esPotenciaDe4(16)
        assert not esPotenciaDe4(17)
    assert list(islice(potenciasDe4(), 5)) == [1, 4, 16, 64, 256]
    print("Verificado")

# La verificación es
#    >>> test_esPotenciaDe4()
#    Verificado

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('esPotenciaDe4_1(4**(2*10**4))')
#    0.33 segundos
#    >>> tiempo('esPotenciaDe4_2(4**(2*10**4))')
#    0.63 segundos
#    >>> tiempo('esPotenciaDe4_3(4**(2*10**4))')
#    0.04 segundos
#    >>> tiempo('esPotenciaDe4_4(4**(2*10**4))')
#    0.05 segundos
#    >>> tiempo('esPotenciaDe4_5(4**(2*10**4))')
#    0.04 segundos
#
#    >>> tiempo('esPotenciaDe4_3(4**(3*10**5))')
#    2.29 segundos
#    >>> tiempo('esPotenciaDe4_4(4**(3*10**5))')
#    2.28 segundos
#    >>> tiempo('esPotenciaDe4_5(4**(3*10**5))')
#    2.31 segundos
