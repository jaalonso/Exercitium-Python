# Mayor_orbita_de_la_sucesion_de_Collatz.py
# Mayor órbita de la sucesión de Collatz.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 3-enero-2025
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Se considera la siguiente operación, aplicable a cualquier número
# entero positivo:
#    * Si el número es par, se divide entre 2.
#    * Si el número es impar, se multiplica por 3 y se suma 1.
#
# Dado un número cualquiera, podemos calcular su órbita; es decir,
# las imágenes sucesivas al iterar la función. Por ejemplo, la órbita
# de 13 es
#    13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 4, 2, 1,...
#
# Si observamos este ejemplo, la órbita de 13 es periódica, es decir,
# se repite indefinidamente a partir de un momento dado). La conjetura
# de Collatz dice que siempre alcanzaremos el 1 para cualquier número
# con el que comencemos. Ejemplos:
#    * Empezando en n = 6 se obtiene 6, 3, 10, 5, 16, 8, 4, 2, 1.
#    * Empezando en n = 11 se obtiene: 11, 34, 17, 52, 26, 13, 40, 20,
#      10, 5, 16, 8, 4, 2, 1.
#    * Empezando en n = 27, la sucesión tiene 112 pasos, llegando hasta
#      9232 antes de descender a 1:  27, 82, 41, 124, 62, 31, 94, 47,
#      142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274,
#      137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263,
#      790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502,
#      251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958,
#      479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644,
#      1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308,
#      1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122,
#      61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5,
#      16, 8, 4, 2, 1.
#
# Definir la función
#    mayoresGeneradores :: Integer -> [Integer]
# tal que (mayoresGeneradores n) es la lista de los números menores o
# iguales que n cuyas órbitas de Collatz son las de mayor longitud. Por
# ejemplo,
#    mayoresGeneradores(20)    ==  [18,19]
#    mayoresGeneradores(10^6)  ==  [837799]
# ---------------------------------------------------------------------

from functools import lru_cache
from itertools import count, islice
from timeit import Timer, default_timer
from typing import Iterator

from hypothesis import given
from hypothesis import strategies as st

# 1ª solución
# ===========

# siguiente(n) es el siguiente de n en la sucesión de Collatz. Por
# ejemplo,
#    siguiente(13)  ==  40
#    siguiente(40)  ==  20
def siguiente (n: int) -> int:
    if n % 2 == 0:
        return n // 2
    return 3*n+1

# collatz1(n) es la órbita de Collatz de n hasta alcanzar el
# 1. Por ejemplo,
#    collatz1(13)  ==  [13,40,20,10,5,16,8,4,2,1]
def collatz1(n: int) -> list[int]:
    if n == 1:
        return [1]
    return [n]+ collatz1(siguiente(n))

# longitudesOrbita() es la lista de los números junto a las longitudes de
# las órbitas de Collatz que generan. Por ejemplo,
#    >>> list(islice(longitudesOrbitas(), 10))
#    [(1,1),(2,2),(3,8),(4,3),(5,6),(6,9),(7,17),(8,4),(9,20),(10,7)]
def longitudesOrbitas() -> Iterator[tuple[int, int]]:
    return ((n, len(collatz1(n))) for n in count(1))

def mayoresGeneradores1(n: int) -> list[int]:
    ps = list(islice(longitudesOrbitas(), n))
    m = max((y for (_, y) in ps))
    return [x for (x,y) in ps if y == m]

# 2ª solución
# ===========

def collatz2(n: int) -> list[int]:
    r = [n]
    while n != 1:
        n = siguiente(n)
        r.append(n)
    return r

def longitudesOrbitas2() -> Iterator[tuple[int, int]]:
    return ((n, len(collatz2(n))) for n in count(1))

def mayoresGeneradores2(n: int) -> list[int]:
    ps = list(islice(longitudesOrbitas2(), n))
    m = max((y for (_, y) in ps))
    return [x for (x,y) in ps if y == m]

# 3ª solución
# ===========

# longitudOrbita(x) es la longitud de la órbita de x. Por ejemplo,
#    longitudOrbita(13)  ==  10
def longitudOrbita(x: int) -> int:
    if x == 1:
        return 1
    return 1 + longitudOrbita(siguiente(x))

def mayoresGeneradores3(n: int) -> list[int]:
    ps = [(x, longitudOrbita(x)) for x in range(1, n+1)]
    m = max((y for (_, y) in ps))
    return [x for (x,y) in ps if y == m]

# 4ª solución
# ===========

# longitudOrbita2(x) es la longitud de la órbita de x. Por ejemplo,
#    longitudOrbita2(13)  ==  10
def longitudOrbita2(x: int) -> int:
    r = 0
    while x != 1:
        x = siguiente(x)
        r += 1
    return r + 1

def mayoresGeneradores4(n: int) -> list[int]:
    ps = [(x, longitudOrbita2(x)) for x in range(1, n+1)]
    m = max((y for (_, y) in ps))
    return [x for (x,y) in ps if y == m]

# 5ª solución
# ===========

@lru_cache(maxsize=None)
def longitudOrbita3(x: int) -> int:
    if x == 1:
        return 1
    return 1 + longitudOrbita3(siguiente(x))

def mayoresGeneradores5(n: int) -> list[int]:
    ps = [(x, longitudOrbita3(x)) for x in range(1, n+1)]
    m = max((y for (_, y) in ps))
    return [x for (x,y) in ps if y == m]

# Verificación
# ============

def test_mayoresGeneradores() -> None:
    for mayoresGeneradores in [mayoresGeneradores1,
                               mayoresGeneradores2,
                               mayoresGeneradores3,
                               mayoresGeneradores4,
                               mayoresGeneradores5]:
        assert mayoresGeneradores(20) == [18,19]
    print("Verificado")

# La verificación es
#    >>> test_mayoresGeneradores()
#    Verificado

# Equivalencia de definiciones
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_mayoresGeneradores_equiv(n: int) -> None:
    r = mayoresGeneradores1(n)
    assert mayoresGeneradores2(n) == r
    assert mayoresGeneradores3(n) == r

# La comprobación es
#    >>> test_mayoresGeneradores_equiv()
#    >>>

# Comprobación de eficiencia
# ==========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comprobación es
#    >>> tiempo('mayoresGeneradores1(10**5)')
#    4.24 segundos
#    >>> tiempo('mayoresGeneradores2(10**5)')
#    1.81 segundos
#    >>> tiempo('mayoresGeneradores3(10**5)')
#    2.06 segundos
#    >>> tiempo('mayoresGeneradores4(10**5)')
#    1.59 segundos
#    >>> tiempo('mayoresGeneradores5(10**5)')
#    0.12 segundos
