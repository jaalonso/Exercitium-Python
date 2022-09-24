# numeros_abundantes.py
# Números abundantes.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 4-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Un número natural n se denomina [abundante](https://bit.ly/3Uk4XUE)
# si es menor que la suma de sus divisores propios. Por ejemplo, 12 es
# abundante ya que la suma de sus divisores propios es 16
# (= 1 + 2 + 3 + 4 + 6), pero 5 y 28 no lo son.
#
# Definir la función
#    numeroAbundante :: Int -> Bool
# tal que (numeroAbundante n) se verifica si n es un número
# abundante. Por ejemplo,
#    numeroAbundante 5  == False
#    numeroAbundante 12 == True
#    numeroAbundante 28 == False
#    numeroAbundante 30 == True
#    numeroAbundante 100000000  ==  True
#    numeroAbundante 100000001  ==  False
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

def numeroAbundante1(x: int) -> bool:
    return x < sumaDivisores1(x) - x

# 2ª solución
# ===========

# Sustituyendo la definición de sumaDivisores de la solución anterior por
# cada una de las del ejercicio [Suma de divisores](https://bit.ly/3S9aonQ)
# se obtiene una nueva definición de numeroAbundante. La usada en la
# definición anterior es la menos eficiente y la que se usa en la
# siguiente definición es la más eficiente.

def sumaDivisores2(n: int) -> int:
    return divisor_sigma(n, 1)

def numeroAbundante2(x: int) -> bool:
    return x < sumaDivisores2(x) - x

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=2, max_value=1000))
def test_numeroAbundante(n):
    assert numeroAbundante1(n) == numeroAbundante2(n)

# La comprobación es
#    src> poetry run pytest -q numeros_abundantes.py
#    1 passed in 0.38s

# Comparación de eficiencia
# =========================

def tiempo(e):
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('numeroAbundante1(4 * 10**7)')
#    2.02 segundos
#    >>> tiempo('numeroAbundante2(4 * 10**7)')
#    0.00 segundos
