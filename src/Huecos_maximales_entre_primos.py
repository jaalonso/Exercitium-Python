# Huecos_maximales_entre_primos.py
# Huecos maximales entre primos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 19-enero-24
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El **hueco de un número primo** p es la distancia entre p y primo
# siguiente de p. Por ejemplo, el hueco de 7 es 4 porque el primo
# siguiente de 7 es 11 y 4 = 11-7. Los huecos de los primeros números son
#    Primo Hueco
#     2    1
#     3    2
#     7    4
#    11    2
#
# El hueco de un número primo p es **maximal** si es mayor que los
# huecos de todos los números menores que p. Por ejemplo, 4 es un hueco
# maximal de 7 ya que los huecos de los primos menores que 7 son 1 y 2
# y ambos son menores que 4. La tabla de los primeros huecos maximales es
#    Primo Hueco
#      2    1
#      3    2
#      7    4
#     23    6
#     89    8
#    113   14
#    523   18
#    887   20
#
# Definir la sucesión
#    primosYhuecosMaximales : () -> Iterator[tuple[int, int]]
# cuyos elementos son los números primos con huecos maximales junto son
# sus huecos. Por ejemplo,
#    >>> list(islice(primosYhuecosMaximales1(), 8))
#    [(2,1),(3,2),(7,4),(23,6),(89,8),(113,14),(523,18),(887,20)]
# ---------------------------------------------------------------------

from itertools import count, islice, pairwise, takewhile
from timeit import Timer, default_timer
from typing import Iterator

from sympy import isprime, nextprime

# 1ª solución
# ===========

# primos() genera la lista de los primos. Por ejemplo,
#    >>> list(islice(primos(), 10))
#    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
def primos() -> Iterator[int]:
    return (n for n in count() if isprime(n))

# huecoPrimo(p) es la distancia del primo p hasta el siguiente
# primo. Por ejemplo,
#    huecoPrimo(7)  ==  4
def huecoPrimo(p: int) -> int:
    return nextprime(p) - p

# esMaximalHuecoPrimo(p) se verifica si el hueco primo de p es
# maximal. Por ejemplo,
#    esMaximalHuecoPrimo(7)   ==  True
#    esMaximalHuecoPrimo(11)  ==  False
def esMaximalHuecoPrimo(p: int) -> bool:
    h = huecoPrimo(p)
    return all(huecoPrimo(n) < h for n in takewhile(lambda x: x < p, primos()))

def primosYhuecosMaximales1() -> Iterator[tuple[int, int]] :
    return ((p,huecoPrimo(p)) for p in primos() if esMaximalHuecoPrimo(p))

# 2ª solución
# ===========

# primosYhuecos es la lista de los números primos junto son sus
# huecos. Por ejemplo,
#    >>> list(islice(primosYhuecos(), 10))
#    [(2,1),(3,2),(5,2),(7,4),(11,2),(13,4),(17,2),(19,4),(23,6),(29,2)]
def primosYhuecos() -> Iterator[tuple[int, int]]:
    return ((x,y-x) for (x,y) in pairwise(primos()))

def primosYhuecosMaximales2() -> Iterator[tuple[int, int]]:
    n = 0
    for (x,y) in primosYhuecos():
        if y > n:
            yield (x,y)
            n = y

# Verificación
# ============

def test_primosYhuecosMaximales() -> None:
    r = [(2,1),(3,2),(7,4),(23,6),(89,8),(113,14),(523,18),(887,20)]
    assert list(islice(primosYhuecosMaximales1(), 8)) == r
    assert list(islice(primosYhuecosMaximales2(), 8)) == r
    print("Verificado")

# La verificación es
#    >>> test_primosYhuecosMaximales()
#    Verificado


# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('list(islice(primosYhuecosMaximales1(), 15))')
#    8.08 segundos
#    >>> tiempo('list(islice(primosYhuecosMaximales2(), 15))')
#    0.17 segundos

# ---------------------------------------------------------------------
# § Referencias                                                      --
# ---------------------------------------------------------------------

# Basado en el ejercicio "Maximal prime gaps" http://bit.ly/22UfDJN de
# Programming Praxis http://programmingpraxis.com

# Otras referencias
# + C. Caldwell, "The gaps between primes" http://bit.ly/1Znusp5
# + J.K. Andersen, "Maximal prime gaps" http://bit.ly/1ZntwRi
# + N.J.A. Sloane "Sequence A002386" en OEIS http://oeis.org/A002386
# + N.J.A. Sloane "Sequence A005250" en OEIS http://oeis.org/A005250
# + E.W. Weisstein, "Prime gaps" en MathWorld http://bit.ly/1ZnubCq
