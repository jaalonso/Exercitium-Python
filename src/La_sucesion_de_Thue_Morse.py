# La_sucesion_de_Thue_Morse.py
# La sucesión de Thue-Morse.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 14-enero-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# La serie de Thue-Morse comienza con el término [0] y sus siguientes
# términos se construyen añadiéndole al anterior su complementario. Los
# primeros términos de la serie son
#    [0]
#    [0,1]
#    [0,1,1,0]
#    [0,1,1,0,1,0,0,1]
#    [0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0]
# De esta forma se va formando una sucesión
#    0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0,...
# que se conoce como la [sucesión de Thue-Morse](https://bit.ly/3PE9LRJ).
#
# Definir la sucesión
#    sucThueMorse : () -> Iterator[int]
# cuyos elementos son los de la sucesión de Thue-Morse. Por ejemplo,
#    >>> list(islice(sucThueMorse(), 30))
#    [0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,0,1,1,0,1,0]
#
# Comprobar con QuickCheck que si s(n) representa el término n-ésimo de
# la sucesión de Thue-Morse, entonces
#    s(2n)   = s(n)
#    s(2n+1) = 1 - s(n)
# ---------------------------------------------------------------------

from itertools import count, islice
from timeit import Timer, default_timer
from typing import Iterator, TypeVar
from math import floor, log2

from hypothesis import given
from hypothesis import strategies as st

from src.La_serie_de_Thue_Morse import serieThueMorse

A = TypeVar('A')

# 1ª solución
# ===========

# nth(i, n) es el n-ésimo elemento del iterador i.
def nth(i: Iterator[A], n: int) -> A:
    return list(islice(i, n, n+1))[0]

# termSucThueMorse(n) es el n-ésimo término de la sucesión de
# Thue-Morse. Por ejemplo,
#    termSucThueMorse(0)  ==  0
#    termSucThueMorse(1)  ==  1
#    termSucThueMorse(2)  ==  1
#    termSucThueMorse(3)  ==  0
#    termSucThueMorse(4)  ==  1
def termSucThueMorse(n: int) -> int:
    if n == 0:
        return 0
    k = 1 + floor(log2(n))
    return nth(serieThueMorse(), k)[n]

def sucThueMorse() -> Iterator[int]:
    return (termSucThueMorse(n) for n in count())

# Comprobación de la propiedad
# ============================

# La propiedad es
@given(st.integers(min_value=0, max_value=100))
def test_prop_termSucThueMorse(n: int) -> None:
    sn = nth(sucThueMorse(), n)
    assert nth(sucThueMorse(), 2*n) == sn
    assert nth(sucThueMorse(), 2*n+1) == 1 - sn

# La comprobación es
#    >>> test_prop_termSucThueMorse()
#    >>>

# 2ª solución
# ===========

# termSucThueMorse2(n) es el n-ésimo término de la sucesión de
# Thue-Morse. Por ejemplo,
#    termSucThueMorse2(0)  ==  0
#    termSucThueMorse2(1)  ==  1
#    termSucThueMorse2(2)  ==  1
#    termSucThueMorse2(3)  ==  0
#    termSucThueMorse2(4)  ==  1
def termSucThueMorse2(n: int) -> int:
    if n == 0:
        return 0
    if n % 2 == 0:
        return termSucThueMorse2(n // 2)
    return 1 - termSucThueMorse2(n // 2)

def sucThueMorse2() -> Iterator[int]:
    return (termSucThueMorse2(n) for n in count())

# Verificación
# ============

def test_sucThueMorse() -> None:
    r = [0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,0,1,1,0,1,0]
    assert list(islice(sucThueMorse(), 30)) == r
    assert list(islice(sucThueMorse2(), 30)) == r
    print("Verificado")

# La verificación es
#    >>> test_sucThueMorse()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=0, max_value=100))
def test_sucThueMorse_equiv(n: int) -> None:
    assert nth(sucThueMorse(), n) == nth(sucThueMorse2(), n)

# La comprobación es
#    >>> test_sucThueMorse_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('nth(sucThueMorse(), 6000)')
#    2.05 segundos
#    >>> tiempo('nth(sucThueMorse2(), 6000)')
#    0.01 segundos

# ---------------------------------------------------------------------
# § Referencias                                                      --
# ---------------------------------------------------------------------

# + N.J.A. Sloane "Sucesión A010060" en OEIS http://oeis.org/A010060
# + Programming Praxis "Thue-Morse sequence" http://bit.ly/1n2PdFk
# + Wikipedia "Thue–Morse sequence" http://bit.ly/1KvZONW
