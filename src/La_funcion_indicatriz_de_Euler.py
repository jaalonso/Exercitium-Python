# La_funcion_indicatriz_de_Euler.py
# La función indicatriz de Euler.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 24-enero-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# La [indicatriz de Euler](https://bit.ly/3yQbzA6) (también llamada
# función φ de Euler) es una función importante en teoría de
# números. Si n es un entero positivo, entonces φ(n) se define como el
# número de enteros positivos menores o iguales a n y coprimos con
# n. Por ejemplo, φ(36) = 12 ya que los números menores o iguales a 36
# y coprimos con 36 son doce: 1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31,
# y 35.
#
# Definir la función
#    phi : (int) -> int
# tal que phi(n) es igual a φ(n). Por ejemplo,
#    phi(36)                         ==  12
#    list(map(phi, range(10, 21)))   ==  [4,10,4,12,6,8,8,16,6,18,8]
#    phi(3**10**5) % (10**9)         ==  681333334
#    len(str(phi2(10**(10**5))))     == 100000
#
# Comprobar con Hypothesis que, para todo n > 0, φ(10^n) tiene n
# dígitos.
# ---------------------------------------------------------------------

from functools import reduce
from math import gcd
from operator import mul
from sys import set_int_max_str_digits
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st
from sympy import factorint, totient

set_int_max_str_digits(10**6)

# 1ª solución
# ===========

def phi1(n: int) -> int:
    return len([x for x in range(1, n+1) if gcd(x, n) == 1])

# 2ª solución
# ===========

def producto(xs: list[int]) -> int:
    return reduce(mul, xs, 1)

def phi2(n: int) -> int:
    factores = factorint(n)
    return producto([(p-1)*p**(e-1) for p, e in factores.items()])

# 3ª solución
# =============

def phi3(n: int) -> int:
    return totient(n)

# Verificación
# ============

def test_phi() -> None:
    for phi in [phi1, phi2, phi3]:
        assert phi(36) == 12
        assert list(map(phi, range(10, 21))) == [4,10,4,12,6,8,8,16,6,18,8]
    print("Verificado")

# La verificación es
#    >>> test_phi()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_phi_equiv(n: int) -> None:
    r = phi1(n)
    assert phi2(n) == r
    assert phi3(n) == r

# La comprobación es
#    >>> test_phi_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('phi1(9*10**6)')
#    2.09 segundos
#    >>> tiempo('phi2(9*10**6)')
#    0.00 segundos
#    >>> tiempo('phi3(9*10**6)')
#    0.00 segundos
#
#    >>> tiempo('phi2(10**1000000)')
#    3.55 segundos
#    >>> tiempo('phi3(10**1000000)')
#    3.37 segundos

# Verificación de la propiedad
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_phi_prop(n: int) -> None:
    assert len(str(phi2(10**n))) == n

# La comprobación es
#    >>> test_phi_prop()
#    >>>

# Comprobación de todas las propiedades
# =====================================

# La comprobación es
#    src> poetry run pytest -v La_funcion_indicatriz_de_Euler.py
#    ===== test session starts =====
#       test_phi PASSED
#       test_phi_equiv PASSED
#       test_phi_prop PASSED
#    ===== passed in 0.55s =====
