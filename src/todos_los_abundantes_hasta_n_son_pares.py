# todos_los_abundantes_hasta_n_son_pares.py
# Todos los abundantes hasta n son pares.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 6-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    todosPares : (int) -> bool
# tal que todosPares(n) se verifica si todos los números abundantes
# menores o iguales que n son pares. Por ejemplo,
#    todosPares(10)    ==  True
#    todosPares(100)   ==  True
#    todosPares(1000)  ==  False
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

# numerosAbundantesMenores(n) es la lista de números abundantes menores
# o iguales que n. Por ejemplo,
#    numerosAbundantesMenores(50)  ==  [12,18,20,24,30,36,40,42,48]
#    numerosAbundantesMenores(48)  ==  [12,18,20,24,30,36,40,42,48]
def numerosAbundantesMenores1(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if numeroAbundante1(x)]

def todosPares1(n: int) -> bool:
    return False not in [x % 2 == 0 for x in numerosAbundantesMenores1(n)]

# 2ª solución
# ===========

# Sustituyendo la definición de numerosAbundantesMenores de la solución
# anterior por cada una de las del ejercicio anterior se obtiene una
# nueva definición de todosPares. La usada en la definición anterior es
# la menos eficiente y la que se usa en la siguiente definición es la
# más eficiente.

def sumaDivisores2(n: int) -> int:
    return divisor_sigma(n, 1)

def numeroAbundante2(x: int) -> bool:
    return x < sumaDivisores2(x) - x

def numerosAbundantesMenores2(n: int) -> list[int]:
    return [x for x in range(1, n + 1) if numeroAbundante2(x)]

def todosPares2(n: int) -> bool:
    return False not in [x % 2 == 0 for x in numerosAbundantesMenores2(n)]

# 3ª solución
# ===========

def todosPares3(n: int) -> bool:
    return all(x % 2 == 0 for x in numerosAbundantesMenores1(n))

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=2, max_value=1000))
def test_todosPares(n: int) -> None:
    assert todosPares1(n) == todosPares2(n) == todosPares3(n)

# La comprobación es
#    src> poetry run pytest -q todos_los_abundantes_hasta_n_son_pares.py
#    1 passed in 2.63s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('todosPares1(1000)')
#    0.03 segundos
#    >>> tiempo('todosPares2(1000)')
#    0.05 segundos
#    >>> tiempo('todosPares3(1000)')
#    0.02 segundos
#
#    >>> tiempo('todosPares1(10000)')
#    2.07 segundos
#    >>> tiempo('todosPares2(10000)')
#    0.47 segundos
#    >>> tiempo('todosPares3(10000)')
#    2.42 segundos
