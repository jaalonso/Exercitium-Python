# triangulo_aritmetico.py
# Triángulo aritmético
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 30-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Los triángulos aritméticos se forman como sigue
#     1
#     2  3
#     4  5  6
#     7  8  9 10
#    11 12 13 14 15
#    16 17 18 19 20 21
#
# Definir las funciones
#    linea     :: Integer -> [Integer]
#    triangulo :: Integer -> [[Integer]]
# tales que
# + (linea n) es la línea n-ésima de los triángulos aritméticos. Por
#   ejemplo,
#      linea 4  ==  [7,8,9,10]
#      linea 5  ==  [11,12,13,14,15]
#      head (linea (10^20)) == 4999999999999999999950000000000000000001
# + (triangulo n) es el triángulo aritmético de altura n. Por ejemplo,
#      triangulo 3  ==  [[1],[2,3],[4,5,6]]
#      triangulo 4  ==  [[1],[2,3],[4,5,6],[7,8,9,10]]
# ---------------------------------------------------------------------

from timeit import Timer, default_timer
from hypothesis import given, strategies as st

# 1ª definición de línea
# ======================

# suma(n) es la suma de los n primeros números. Por ejemplo,
#    suma(3)  ==  6
def suma1(n: int) -> int:
    return sum(range(1, n + 1))

def linea1(n: int) -> list[int]:
    return list(range(suma1(n - 1) + 1, suma1(n) + 1))

# 2ª definición de línea
# ======================

def linea2(n: int) -> list[int]:
    s = suma1(n-1)
    return list(range(s + 1, s + n + 1))

# 3ª definición de línea
# ======================

def suma2(n: int) -> int:
    return (1 + n) * n // 2

def linea3(n: int) -> list[int]:
    s = suma2(n-1)
    return list(range(s + 1, s + n + 1))

# Comprobación de equivalencia de linea
# =====================================

@given(st.integers(min_value=1, max_value=1000))
def test_suma(n):
    r = linea1(n)
    assert linea2(n) == r
    assert linea3(n) == r

# La comprobación es
#    src> poetry run pytest -q triangulo_aritmetico.py
#    1 passed in 0.15s

# Comparación de eficiencia
# =========================

def tiempo(e):
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('linea1(10**7)')
#    0.53 segundos
#    >>> tiempo('linea2(10**7)')
#    0.40 segundos
#    >>> tiempo('linea3(10**7)')
#    0.29 segundos

# 1ª definición de triangulo
# ==========================

def triangulo1(n: int) -> list[list[int]]:
    return [linea1(m) for m in range(1, n + 1)]

# 2ª definición de triangulo
# ==========================

def triangulo2(n: int) -> list[list[int]]:
    return [linea2(m) for m in range(1, n + 1)]

# 3ª definición de triangulo
# ==========================

def triangulo3(n: int) -> list[list[int]]:
    return [linea3(m) for m in range(1, n + 1)]

# Comprobación de equivalencia de triangulo
# =========================================

@given(st.integers(min_value=1, max_value=1000))
def test_triangulo(n):
    r = triangulo1(n)
    assert triangulo2(n) == r
    assert triangulo3(n) == r

# La comprobación es
#    src> poetry run pytest -q triangulo_aritmetico.py
#    1 passed in 3.44s

# Comparación de eficiencia de triangulo
# ======================================
#
# La comparación es
#    >>> tiempo('triangulo1(10**4)')
#    2.58 segundos
#    >>> tiempo('triangulo2(10**4)')
#    1.91 segundos
#    >>> tiempo('triangulo3(10**4)')
#    1.26 segundos
