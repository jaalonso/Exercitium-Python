# Reconocimiento_de_grandes_potencias_de_2.py
# Reconocimiento de potencias de 2.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 24-junio-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    esPotenciaDeDos : (int) -> bool
# tal que esPotenciaDeDos(n) se verifica si n es una potencia de
# dos (suponiendo que n es mayor que 0). Por ejemplo.
#    esPotenciaDeDos(1)        == True
#    esPotenciaDeDos(2)        == True
#    esPotenciaDeDos(6)        == False
#    esPotenciaDeDos(8)        == True
#    esPotenciaDeDos(1024)     == True
#    esPotenciaDeDos(1026)     == False
#    esPotenciaDeDos(2^(10^8)) == True
# ---------------------------------------------------------------------

from itertools import count, dropwhile, islice, repeat, starmap
from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import Iterator

from hypothesis import given
from hypothesis import strategies as st
from sympy import factorint

setrecursionlimit(10**6)

# 1ª solución
# ===========

def esPotenciaDeDos1(n: int) -> bool:
    return n == 1 or (n % 2 == 0 and esPotenciaDeDos1(n // 2))

# 2ª solución
# ===========

# potenciasDeDos() es la lista de las potencias de dos. Por ejemplo,
#    >>> list(islice(potenciasDeDos(), 10))
#    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
def potenciasDeDos1() -> Iterator[int]:
    n = 1
    while True:
        yield n
        n *= 2

def esPotenciaDeDos2(n: int) -> bool:
    return n == next(dropwhile(lambda x: x < n, potenciasDeDos1()))

# 3ª solución
# ===========

def potenciasDeDos2() -> Iterator[int]:
    return starmap(pow, zip(repeat(2), count()))

def esPotenciaDeDos3(n: int) -> bool:
    return n == next(dropwhile(lambda x: x < n, potenciasDeDos2()))

# 4ª solución
# ===========

def esPotenciaDeDos4(n: int) -> bool:
    return all(x == 2 for x in factorint(n))

# 5ª solución
# ===========

# Usando la función &. Dicha función calcula el número correspondiente a
# la conjunción de las representaciones binarias de sus argumentos. Por
# ejemplo,
#    6 & 3 == 2
# ya que
#    la representación binaria de 6 es     [1,1,0]
#    la representación binaria de 3 es       [1,1]
#    la conjunción es                        [1,0]
#    la representación decimal de [1,0] es   2
#
# Otros ejemplos:
#    4 & 3 ==   [1,0,0] &   [1,1] == 0
#    8 & 7 == [1,0,0,0] & [1,1,1] == 0

def esPotenciaDeDos5(n: int) -> bool:
    return n & (n - 1) == 0

# Verificación
# ============

def test_esPotenciaDeDos() -> None:
    for esPotenciaDeDos in [esPotenciaDeDos1,
                            esPotenciaDeDos2,
                            esPotenciaDeDos3,
                            esPotenciaDeDos4,
                            esPotenciaDeDos5]:
        assert list(islice(potenciasDeDos1(), 10)) ==\
            [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
        assert list(islice(potenciasDeDos2(), 10)) ==\
            [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
        assert esPotenciaDeDos(1)
        assert esPotenciaDeDos(2)
        assert not esPotenciaDeDos(6)
        assert esPotenciaDeDos(8)
        assert esPotenciaDeDos(1024)
        assert not esPotenciaDeDos(1026)
    print("Verificado")

# La verificación es
#    >>> test_esPotenciaDeDos()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_esPotenciaDeDos_equiv(n: int) -> None:
    r = esPotenciaDeDos1(n)
    assert esPotenciaDeDos2(n) == r
    assert esPotenciaDeDos3(n) == r
    assert esPotenciaDeDos4(n) == r
    assert esPotenciaDeDos5(n) == r

# La comprobación es
#    >>> test_esPotenciaDeDos_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('esPotenciaDeDos1(2**(2*10**4))')
#    0.19 segundos
#    >>> tiempo('esPotenciaDeDos2(2**(2*10**4))')
#    0.03 segundos
#    >>> tiempo('esPotenciaDeDos3(2**(2*10**4))')
#    0.25 segundos
#    >>> tiempo('esPotenciaDeDos4(2**(2*10**4))')
#    0.00 segundos
#    >>> tiempo('esPotenciaDeDos5(2**(2*10**4))')
#    0.00 segundos
#
#    >>> tiempo('esPotenciaDeDos2(2**(10**5))')
#    0.18 segundos
#    >>> tiempo('esPotenciaDeDos3(2**(10**5))')
#    8.65 segundos
#    >>> tiempo('esPotenciaDeDos4(2**(10**5))')
#    0.00 segundos
#    >>> tiempo('esPotenciaDeDos5(2**(10**5))')
#    0.00 segundos
#
#    >>> tiempo('esPotenciaDeDos2(2**(10**6))')
#    12.92 segundos
#    >>> tiempo('esPotenciaDeDos4(2**(10**6))')
#    0.01 segundos
#    >>> tiempo('esPotenciaDeDos5(2**(10**6))')
#    0.01 segundos
#
#    >>> tiempo('esPotenciaDeDos4(2**(10**9))')
#    4.51 segundos
#    >>> tiempo('esPotenciaDeDos5(2**(10**9))')
#    4.57 segundos
