# Sistema_factoradico_de_numeracion.py
# Sistema factorádico de numeración.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 24-abril-2025
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El [sistema factorádico](https://bit.ly/3KQZRue) es un sistema
# numérico basado en factoriales en el que el n-ésimo dígito, empezando
# desde la derecha, debe ser multiplicado por n! Por ejemplo, el número
# "341010" en el sistema factorádico es 463 en el sistema decimal ya
# que
#    3×5! + 4×4! + 1×3! + 0×2! + 1×1! + 0×0! = 463
#
# En este sistema numérico, el dígito de más a la derecha es siempre 0,
# el segundo 0 o 1, el tercero 0,1 o 2 y así sucesivamente.
#
# Con los dígitos del 0 al 9 el mayor número que podemos codificar es el
# 10!-1 = 3628799. En cambio, si lo ampliamos con las letras A a Z podemos
# codificar hasta 36!-1 = 37199332678990121746799944815083519999999910.
#
# Definir las funciones
#    factoradicoAdecimal : (str) -> int
#    decimalAfactoradico : int -> str
# tales que
# + factoradicoAdecimal(cs) es el número decimal correspondiente al
#   número factorádico cs. Por ejemplo,
#      >>> factoradicoAdecimal("341010")
#      463
#      >>> factoradicoAdecimal("2441000")
#      2022
#      >>> factoradicoAdecimal("A0000000000")
#      36288000
#      >>> list(map(factoradicoAdecimal, ["10","100","110","200","210","1000","1010","1100","1110","1200"]))
#      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#      >>> factoradicoAdecimal("3KXWVUTSRQPONMLKJIHGFEDCBA9876543210")
#      37199332678990121746799944815083519999999
# + decimalAfactoradico(n) es el número factorádico correpondiente al
#   número decimal n. Por ejemplo,
#      >>> decimalAfactoradico(463)
#      '341010'
#      >>> decimalAfactoradico(2022)
#      '2441000'
#      >>> decimalAfactoradico(36288000)
#      'A0000000000'
#      >>> list(map(decimalAfactoradico, range(1, 11)))
#      ['10', '100', '110', '200', '210', '1000', '1010', '1100', '1110', '1200']
#      >>> decimalAfactoradico(37199332678990121746799944815083519999999)
#      '3KXWVUTSRQPONMLKJIHGFEDCBA9876543210'
#
# Comprobar con Hypothesis que, para cualquier entero positivo n,
#    factoradicoAdecimal(decimalAfactoradico(n)) == n
# ---------------------------------------------------------------------

from itertools import count, takewhile
from math import factorial
from typing import Iterator

from hypothesis import given
from hypothesis import strategies as st

# 1ª definición de factoradicoAdecimal
# ====================================

# caracterAentero(c) es la posición del carácter c en la lista de
# caracteres ['0', '1',..., '9', 'A', 'B',..., 'Z']. Por ejemplo,
#    caracterAentero('0')  ==  0
#    caracterAentero('1')  ==  1
#    caracterAentero('9')  ==  9
#    caracterAentero('A')  ==  10
#    caracterAentero('B')  ==  11
#    caracterAentero('Z')  ==  35
def caracterAentero(c: str) -> int:
    if c.isdigit():
        return int(c)
    return ord(c) - ord('A') +  10

def factoradicoAdecimal1(cs: str) -> int:
    xs = map(caracterAentero, cs)
    n  = len(cs)
    ys = reversed([factorial(k) for k in range(n)])
    return sum((x * y for (x, y) in zip(xs, ys)))

# 2ª definición de factoradicoAdecimal
# ====================================

# caracteres es la cadena de los caracteres.
caracteres: str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# caracteresEnteros es el diccionario cuyas claves son los caracteres y
# los valores son los números de 0 a 35.
caracteresEnteros: dict[str, int] = {c: i for i, c in enumerate(caracteres)}

# caracterAentero2(c) es la posición del carácter c en la lista de
# caracteres ['0', '1',..., '9', 'A', 'B',..., 'Z']. Por ejemplo,
#    caracterAentero2('0')  ==  0
#    caracterAentero2('1')  ==  1
#    caracterAentero2('9')  ==  9
#    caracterAentero2('A')  ==  10
#    caracterAentero2('B')  ==  11
#    caracterAentero2('Z')  ==  35
def caracterAentero2(c: str) -> int:
    return caracteresEnteros[c]

def factoradicoAdecimal2(cs: str) -> int:
    xs = map(caracterAentero2, cs)
    n  = len(cs)
    ys = reversed([factorial(k) for k in range(n)])
    return sum((x * y for (x, y) in zip(xs, ys)))

# 3ª definición de factoradicoAdecimal
# ====================================

# caracterAentero3(c) es la posición del carácter c en la lista de
# caracteres ['0', '1',..., '9', 'A', 'B',..., 'Z']. Por ejemplo,
#    caracterAentero3('0')  ==  0
#    caracterAentero3('1')  ==  1
#    caracterAentero3('9')  ==  9
#    caracterAentero3('A')  ==  10
#    caracterAentero3('B')  ==  11
#    caracterAentero3('Z')  ==  35
def caracterAentero3(c: str) -> int:
    return len(list(takewhile(lambda x: x != c, caracteres)))

def factoradicoAdecimal3(cs: str) -> int:
    return sum(x * y for x, y in zip([factorial(k) for k in range(len(cs))],
                                     reversed(list(map(caracterAentero3, cs)))))

# 1ª definición de decimalAfactoradico
# ====================================

# enteroAcaracter(k) es el k-ésimo elemento de la lista
# ['0', '1',..., '9', 'A', 'B',..., 'Z']. . Por ejemplo,
#    enteroAcaracter(0)   ==  '0'
#    enteroAcaracter(1)   ==  '1'
#    enteroAcaracter(9)   ==  '9'
#    enteroAcaracter(10)  ==  'A'
#    enteroAcaracter(11)  ==  'B'
#    enteroAcaracter(35)  ==  'Z'
def enteroAcaracter(k: int) -> str:
    return caracteres[k]

# facts() es la lista de los factoriales. Por ejemplo,
#    >>> list(takewhile(lambda x : x < 900, facts()))
#    [1, 1, 2, 6, 24, 120, 720]
def facts() -> Iterator[int]:
    return (factorial(n) for n in count())

def decimalAfactoradico1(n: int) -> str:
    def aux(m: int, xs: list[int]) -> str:
        if m == 0:
            return "0" * len(xs)
        y, *ys = xs
        print(m, y, m // y)
        return enteroAcaracter(m // y) + aux(m % y, ys)
    return aux(n, list(reversed(list(takewhile(lambda x : x <= n, facts())))))

# 2ª definición de decimalAfactoradico
# ====================================

# enterosCaracteres es el diccionario cuyas claves son los número de 0
# a 35 y las claves son los caracteres.
enterosCaracteres: dict[int, str] = dict(enumerate(caracteres))

# enteroAcaracter2(k) es el k-ésimo elemento de la lista
# ['0', '1',..., '9', 'A', 'B',..., 'Z']. . Por ejemplo,
#    enteroAcaracter2(0)   ==  '0'
#    enteroAcaracter2(1)   ==  '1'
#    enteroAcaracter2(9)   ==  '9'
#    enteroAcaracter2(10)  ==  'A'
#    enteroAcaracter2(11)  ==  'B'
#    enteroAcaracter2(35)  ==  'Z'
def enteroAcaracter2(k: int) -> str:
    return enterosCaracteres[k]

def decimalAfactoradico2(n: int) -> str:
    def aux(m: int, xs: list[int]) -> str:
        if m == 0:
            return "0" * len(xs)
        y, *ys = xs
        return enteroAcaracter2(m // y) + aux(m % y, ys)
    return aux(n, list(reversed(list(takewhile(lambda x : x <= n, facts())))))

# 3ª definición de decimalAfactoradico
# ====================================

# enteroAcaracter3(k) es el k-ésimo elemento de la lista
# ['0', '1',..., '9', 'A', 'B',..., 'Z']. . Por ejemplo,
#    enteroAcaracter3(0)   ==  '0'
#    enteroAcaracter3(1)   ==  '1'
#    enteroAcaracter3(9)   ==  '9'
#    enteroAcaracter3(10)  ==  'A'
#    enteroAcaracter3(11)  ==  'B'
#    enteroAcaracter3(35)  ==  'Z'
def enteroAcaracter3(n: int) -> str:
    return caracteres[n]

def decimalAfactoradico3(n: int) -> str:
    def aux(m: int, xs: list[int]) -> str:
        if m == 0:
            return "0" * len(xs)
        y, *ys = xs
        return enteroAcaracter3(m // y) + aux(m % y, ys)
    return aux(n, list(reversed(list(takewhile(lambda x : x <= n, facts())))))

# Verificación
# ============

def test_factoradico() -> None:
    for factoradicoAdecimal in [factoradicoAdecimal1,
                                factoradicoAdecimal2,
                                factoradicoAdecimal3]:
        assert factoradicoAdecimal("341010") == 463
        assert factoradicoAdecimal("2441000") == 2022
        assert factoradicoAdecimal("A0000000000") == 36288000
    for decimalAfactoradico in [decimalAfactoradico1,
                                decimalAfactoradico2,
                                decimalAfactoradico3]:
        assert decimalAfactoradico(463) == "341010"
        assert decimalAfactoradico(2022) == "2441000"
        assert decimalAfactoradico(36288000) == "A0000000000"
    print("Verificado")

# La verificación es
#    >>> test_factoradico()
#    Verificado

# Propiedad de inverso
# ====================

@given(st.integers(min_value=0, max_value=1000))
def test_factoradico_equiv(n: int) -> None:
    assert factoradicoAdecimal1(decimalAfactoradico1(n)) == n
    assert factoradicoAdecimal2(decimalAfactoradico3(n)) == n
    assert factoradicoAdecimal3(decimalAfactoradico3(n)) == n

# La comprobación es
#    >>> test_factoradico_equiv()
#    >>>
