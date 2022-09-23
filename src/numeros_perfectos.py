# numeros_perfectos.py
# Números perfectos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 3-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Un números entero positivo es [perfecto](https://bit.ly/3BIN0be) si
# es igual a la suma de sus divisores, excluyendo el propio número. Por
# ejemplo, 6 es un número perfecto porque sus divisores propios son 1,
# 2 y 3; y 6 = 1 + 2 + 3.
#
# Definir la función
#    perfectos (int) -> list[int]
# tal que perfectos(n) es la lista de todos los números perfectos
# menores que n. Por ejemplo,
#    perfectos(500)   ==  [6, 28, 496]
#    perfectos(10^5)  ==  [6, 28, 496, 8128]
# ---------------------------------------------------------------------

from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st
from sympy import divisor_sigma

# 1ª solución
# ===========

# divisores(n) es la lista de los divisores del número n. Por ejemplo,
#    divisores(30)  ==  [1,2,3,5,6,10,15,30]
def divisores1(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if n % x == 0]

# sumaDivisores(x) es la suma de los divisores de x. Por ejemplo,
#    sumaDivisores(12)                ==  28
#    sumaDivisores(25)                ==  31
def sumaDivisores1(n: int) -> int:
    return sum(divisores1(n))

# esPerfecto(x) se verifica si x es un número perfecto. Por ejemplo,
#    esPerfecto(6)  ==  True
#    esPerfecto(8)  ==  False
def esPerfecto1(x: int) -> bool:
    return sumaDivisores1(x) - x == x

def perfectos1(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if esPerfecto1(x)]

# 2ª solución
# ===========

# Sustituyendo la definición de sumaDivisores de la solución anterior por
# cada una de las del ejercicio [Suma de divisores](https://bit.ly/3S9aonQ)
# se obtiene una nueva definición deperfectos. La usada en la
# definición anterior es la menos eficiente y la que se usa en la
# siguiente definición es la más eficiente.

def sumaDivisores2(n: int) -> int:
    return divisor_sigma(n, 1)

def esPerfecto2(x: int) -> bool:
    return sumaDivisores2(x) - x == x

def perfectos2(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if esPerfecto2(x)]

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=2, max_value=1000))
def test_perfectos(n):
    assert perfectos1(n) == perfectos2(n)

# La comprobación es
#    src> poetry run pytest -q numeros_perfectos.py
#    1 passed in 1.43s

# Comparación de eficiencia
# =========================

def tiempo(e):
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('perfectos1(10**4)')
#    2.97 segundos
#    >>> tiempo('perfectos2(10**4)')
#    0.57 segundos
