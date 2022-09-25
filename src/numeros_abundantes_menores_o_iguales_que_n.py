# numeros_abundantes_menores_o_iguales_que_n.py
# Números abundantes menores o iguales que n.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 5-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Un número natural n se denomina [abundante](https://bit.ly/3Uk4XUE)
# si es menor que la suma de sus divisores propios. Por ejemplo, 12 es
# abundante ya que la suma de sus divisores propios es 16
# (= 1 + 2 + 3 + 4 + 6), pero 5 y 28 no lo son.
#
# Definir la función
#    numerosAbundantesMenores : (int) -> list[Int]
# tal que numerosAbundantesMenores(n) es la lista de números
# abundantes menores o iguales que n. Por ejemplo,
#    numerosAbundantesMenores(50)  ==  [12,18,20,24,30,36,40,42,48]
#    numerosAbundantesMenores(48)  ==  [12,18,20,24,30,36,40,42,48]
#    leng(numerosAbundantesMenores(10**6)) ==  247545
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

# numeroAbundante(n) se verifica si n es un número abundante. Por
# ejemplo,
#    numeroAbundante(5)  == False
#    numeroAbundante(12) == True
#    numeroAbundante(28) == False
#    numeroAbundante(30) == True
def numeroAbundante1(x: int) -> bool:
    return x < sumaDivisores1(x) - x

def numerosAbundantesMenores1(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if numeroAbundante1(x)]

# 2ª solución
# ===========

# Sustituyendo la definición de numeroAbundante de la solución anterior por
# cada una de las del ejercicio [Números abundantes](https://bit.ly/3xSlWDU)
# se obtiene una nueva definición de numerosAbundantesMenores. La usada en la
# definición anterior es la menos eficiente y la que se usa en la
# siguiente definición es la más eficiente.

def sumaDivisores2(n: int) -> int:
    return divisor_sigma(n, 1)

def numeroAbundante2(x: int) -> bool:
    return x < sumaDivisores2(x) - x

def numerosAbundantesMenores2(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if numeroAbundante2(x)]

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=2, max_value=1000))
def test_numerosAbundantesMenores(n: int) -> None:
    assert numerosAbundantesMenores1(n) == numerosAbundantesMenores2(n)

# La comprobación es
#    src> poetry run pytest -q numeros_abundantes_menores_o_iguales_que_n.py
#    1 passed in 1.54s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('len(numerosAbundantesMenores1(10**4))')
#    2.21 segundos
#    >>> tiempo('len(numerosAbundantesMenores2(10**4))')
#    0.55 segundos
#
#    >>> tiempo('len(numerosAbundantesMenores2(10**5))')
#    5.96 segundos
