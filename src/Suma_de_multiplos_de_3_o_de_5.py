# Suma_de_multiplos_de_3_o_de_5.py
# Suma de múltiplos de 3 o de 5.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 10-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    sumaMultiplos : (int) -> int
# tal que sumaMultiplos(n) es la suma de todos los múltiplos de 3 ó 5 menores
# que n. Por ejemplo,
#    sumaMultiplos(10)     == 23
#    sumaMultiplos(10**2)  == 2318
#    sumaMultiplos(10**3)  == 233168
#    sumaMultiplos(10**4)  == 23331668
#    sumaMultiplos(10**5)  == 2333316668
#    sumaMultiplos(10**10) == 23333333331666666668
#    sumaMultiplos(10**20) == 2333333333333333333316666666666666666668
#
# Nota: Este ejercicio está basado en el problema 1 del Proyecto Euler
# https://projecteuler.net/problem=1
# ---------------------------------------------------------------------

from math import gcd
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

# 1ª solución
# ===========

# multiplo(x, y) se verifica si x es un múltiplo de y. Por ejemplo.
#    multiplo(12, 3)  ==  True
#    multiplo(14, 3)  ==  False
def multiplo(x: int, y: int) -> int:
    return x % y == 0

def sumaMultiplos1(n: int) -> int:
    return sum(x for x in range(1, n)
               if (multiplo(x, 3) or multiplo(x, 5)))

# 2ª solución                                                        --
# ===========

def sumaMultiplos2(n: int) -> int:
    return sum(x for x in range(1, n)
               if gcd(x, 15) > 1)

# 3ª solución                                                        --
# ===========

def sumaMultiplos3(n: int) -> int:
    return sum(range(3, n, 3)) + \
           sum(range(5, n, 5)) - \
           sum(range(15, n, 15))

# 4ª solución                                                        --
# ===========

def sumaMultiplos4(n: int) -> int:
    return sum(set(list(range(3, n, 3)) + list(range(5, n, 5))))

# 5ª solución                                                        --
# ===========

def sumaMultiplos5(n: int) -> int:
    return sum(set(list(range(3, n, 3))) | set(list(range(5, n, 5))))

# 6ª solución                                                        --
# ===========

# suma(d, x) es la suma de los múltiplos de d menores que x. Por
# ejemplo,
#    suma(3, 20)  ==  63
def suma(d: int, x: int) -> int:
    a = d
    b = d * ((x - 1) // d)
    n = 1 + (b - a) // d
    return (a + b) * n // 2

def sumaMultiplos6(n: int) -> int:
    return suma(3, n) + suma(5, n) - suma(15, n)

# Verificación
# ============

def test_sumaMultiplos() -> None:
    for sumaMultiplos in [sumaMultiplos1, sumaMultiplos2,
                          sumaMultiplos3, sumaMultiplos4,
                          sumaMultiplos5, sumaMultiplos6]:
        assert sumaMultiplos(10) == 23
        assert sumaMultiplos(10**2) == 2318
    print("Verificado")

# La verificación es
#    >>> test_sumaMultiplos()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_sumaMultiplos_equiv(n: int) -> None:
    r = sumaMultiplos1(n)
    assert sumaMultiplos2(n) == r
    assert sumaMultiplos3(n) == r
    assert sumaMultiplos4(n) == r
    assert sumaMultiplos5(n) == r
    assert sumaMultiplos6(n) == r

# La comprobación es
#    src> poetry run pytest -q Suma_de_multiplos_de_3_o_de_5.py
#    1 passed in 0.16s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('sumaMultiplosa(10**7)')
#    1.49 segundos
#    >>> tiempo('sumaMultiplosb(10**7)')
#    0.93 segundos
#    >>> tiempo('sumaMultiplosc(10**7)')
#    0.07 segundos
#    >>> tiempo('sumaMultiplosd(10**7)')
#    0.42 segundos
#    >>> tiempo('sumaMultiplose(10**7)')
#    0.69 segundos
#    >>> tiempo('sumaMultiplosf(10**7)')
#    0.00 segundos
#
#    >>> tiempo('sumaMultiplosc(10**8)')
#    0.72 segundos
#    >>> tiempo('sumaMultiplosf(10**8)')
#    0.00 segundos
