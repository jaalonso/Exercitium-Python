# numeros_abundantes_impares.py
# Números abundantes impares.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 7-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#   abundantesImpares : (int) -> list[int]
# tal que abundantesImpares(n) son los números abundantes impares
# menores que n. Por ejemplo,
#    >>> abundantesImpares1(10000)[:12]
#    [945, 1575, 2205, 2835, 3465, 4095, 4725, 5355, 5775, 5985, 6435, 6615]
# ---------------------------------------------------------------------

from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st
from sympy import divisor_sigma

# 1ª solución
# ===========

def abundantesImpares1(n: int) -> list[int]:
    return [x for x in range(1, n, 2) if numeroAbundante1(x)]

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

# 2ª solución
# ===========

def abundantesImpares2(n: int) -> list[int]:
    return list(filter(numeroAbundante1, range(1, n, 2)))

# 3ª solución
# ===========
#
# Sustituyendo la definición de numeroAbundante1 de las soluciones
# anteriores por cada una de las del ejercicio "Números abundantes"
# https://bit.ly/3xSlWDU se obtiene una nueva definición de abundantes
# impares. La usada en las definiciones anteriores es la menos
# eficiente y la que se usa en la siguiente definición es la más eficiente.

def abundantesImpares3(n: int) -> list[int]:
    return list(filter(numeroAbundante3, range(1, n, 2)))

def sumaDivisores3(n: int) -> int:
    return divisor_sigma(n, 1)

def numeroAbundante3(x: int) -> bool:
    return x < sumaDivisores3(x) - x

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_abundantesImpares(n: int) -> None:
    r = abundantesImpares1(n)
    assert abundantesImpares2(n) == r
    assert abundantesImpares3(n) == r

# La comprobación es
#    src> poetry run pytest -q numeros_abundantes_impares.py
#    1 passed in 1.42s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('abundantesImpares1(10000)[5]')
#    1.25 segundos
#    >>> tiempo('abundantesImpares2(10000)[5]')
#    1.22 segundos
#    >>> tiempo('abundantesImpares3(10000)[5]')
#    0.33 segundos
