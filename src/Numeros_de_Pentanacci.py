# Numeros_de_Pentanacci.py
# Números de Pentanacci.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 05-agosto-2022 (versión 14-dic-23)
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Los números de Fibonacci se definen mediante las ecuaciones
#    F(0) = 0
#    F(1) = 1
#    F(n) = F(n-1) + F(n-2), si n > 1
# Los primeros números de Fibonacci son
#    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, ...
#
# Una generalización de los anteriores son los números de Pentanacci
# definidos por las siguientes ecuaciones
#    P(0) = 0
#    P(1) = 1
#    P(2) = 1
#    P(3) = 2
#    P(4) = 4
#    P(n) = P(n-1) + P(n-2) + P(n-3) + P(n-4) + P(n-5), si n > 4
# Los primeros números de Pentanacci son
#   0, 1, 1, 2, 4, 8, 16, 31, 61, 120, 236, 464, 912, 1793, 3525, ...
#
# Definir las funciones
#    pentanacci  : (int) -> int
#    pentanaccis : () -> Iterator[int]
# tales que
# + pentanacci(n) es el n-ésimo número de Pentanacci. Por ejemplo,
#      >>> pentanacci(14)
#      3525
#      >>> pentanacci2(10**5) % 10**30
#      482929150584077921552549215816
#      >>> len(str(pentanacci2(10**5)))
#      29357
# + pentanaccis() genera los números de Pentanacci. Por ejemplo,
#      >>> list(islice(pentanaccis(), 15))
#      [0, 1, 1, 2, 4, 8, 16, 31, 61, 120, 236, 464, 912, 1793, 3525]
# ---------------------------------------------------------------------

from itertools import count, islice
from sys import set_int_max_str_digits
from timeit import Timer, default_timer
from typing import Iterator

set_int_max_str_digits(30000)

# 1ª solución
# ===========

def pentanacci1(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4
    return sum((pentanacci1(n-k) for k in range(1, 6)))

def pentanaccis1() -> Iterator[int]:
    return (pentanacci1(n) for n in count())

# 2ª solución
# ===========

def pentanaccis2() -> Iterator[int]:
    seq = [0, 1, 1, 2, 4]
    while True:
        yield seq[0]
        seq.append(sum(seq))
        seq.pop(0)

def nth(i: Iterator[int], n: int) -> int:
    return list(islice(i, n, n+1))[0]

def pentanacci2(n: int) -> int:
    return nth(pentanaccis2(), n)

# Verificación
# ============

def test_pentanacci() -> None:
    assert pentanacci1(14) == 3525
    assert list(islice(pentanaccis1(), 15)) == \
        [0, 1, 1, 2, 4, 8, 16, 31, 61, 120, 236, 464, 912, 1793, 3525]
    assert pentanacci2(14) == 3525
    assert list(islice(pentanaccis2(), 15)) == \
        [0, 1, 1, 2, 4, 8, 16, 31, 61, 120, 236, 464, 912, 1793, 3525]
    print("Verificado")

# La verificación es
#    >>> test_pentanacci()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
def test_pentanacci_equiv() -> bool:
    return list(islice(pentanaccis1(), 25)) == list(islice(pentanaccis2(), 25))

# La comprobación es
#    >>> test_pentanacci_equiv()
#    True

# Comparación de eficiencia
# =========================

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('pentanacci1(28)')
#    8.24 segundos
#    >>> tiempo('pentanacci2(28)')
#    0.00 segundos

# Referencias
# ===========

# + Tito III Piezas y Eric Weisstein, [Pentanacci number](https://bit.ly/3cPJGkF).
# + N. J. A. Sloane, [Sucesión A001591 de la OEIS](https://oeis.org/A001591).
