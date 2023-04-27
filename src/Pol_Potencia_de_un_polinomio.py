# Pol_Potencia_de_un_polinomio.py
# TAD de los polinomios: Potencia de un polinomio.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 4-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu),
# definir la función
#    potencia : (Polinomio[A], int) -> Polinomio[A]
# tal que potencia(p, n) es la potencia n-ésima del polinomio p. Por
# ejemplo,
#    >>> ejPol = consPol(1, 2, consPol(0, 3, polCero()))
#    >>> ejPol
#    2*x + 3
#    >>> potencia(ejPol, 2)
#    4*x^2 + 12*x + 9
#    >>> potencia(ejPol, 3)
#    8*x^3 + 36*x^2 + 54*x + 27
# ---------------------------------------------------------------------

from sys import setrecursionlimit
from timeit import Timer, default_timer
from typing import TypeVar

from hypothesis import given
from hypothesis import strategies as st

from src.Pol_Producto_polinomios import multPol
from src.TAD.Polinomio import Polinomio, consPol, polCero, polinomioAleatorio

setrecursionlimit(10**6)

A = TypeVar('A', int, float, complex)

# 1ª solución
# ===========

def potencia(p: Polinomio[A], n: int) -> Polinomio[A]:
    if n == 0:
        return consPol(0, 1, polCero())
    return multPol(p, potencia(p, n - 1))

# 2ª solución
# ===========

def potencia2(p: Polinomio[A], n: int) -> Polinomio[A]:
    if n == 0:
        return consPol(0, 1, polCero())
    if n % 2 == 0:
        return potencia2(multPol(p, p), n // 2)
    return multPol(p, potencia2(multPol(p, p), (n - 1) // 2))

# 3ª solución
# ===========

def potencia3(p: Polinomio[A], n: int) -> Polinomio[A]:
    r: Polinomio[A] = consPol(0, 1, polCero())
    for _ in range(0, n):
        r = multPol(p, r)
    return r

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(p=polinomioAleatorio(),
       n=st.integers(min_value=1, max_value=10))
def test_potencia(p: Polinomio[int], n: int) -> None:
    r = potencia(p, n)
    assert potencia2(p, n) == r
    assert potencia3(p, n) == r

# La comprobación es
#    src> poetry run pytest -q Pol_Potencia_de_un_polinomio.py
#    1 passed in 0.89s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> from src.TAD.Polinomio import grado
#    >>> ejPol = consPol(1, 2, consPol(0, 3, polCero()))
#    >>> tiempo('grado(potencia(ejPol, 1000))')
#    8.58 segundos
#    >>> tiempo('grado(potencia2(ejPol, 1000))')
#    8.75 segundos
