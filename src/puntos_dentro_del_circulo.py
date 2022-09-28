# puntos_dentro_del_circulo.py
# Puntos dentro del círculo.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 11-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    circulo : (int) -> int
# tal que circulo(n) es el la cantidad de pares de números naturales
# (x,y) que se encuentran dentro del círculo de radio n. Por ejemplo,
#    circulo(3)  ==  9
#    circulo(4)  ==  15
#    circulo(5)  ==  22
#    circulo(100)  ==  7949
# ---------------------------------------------------------------------

from math import sqrt
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

# 1ª solución
# ===========

def circulo1(n: int) -> int:
    return len([(x, y) for x in range(0, n) for y in range(0, n)
                if x * x + y * y < n * n])

# 2ª solución
# ===========

# raizCuadradaEntera(n) es la parte entera de la raíz cuadrada de
# n. Por ejemplo,
#    raizCuadradaEntera 17  ==  4
def raizCuadradaEntera(n: int) -> int:
    return int(sqrt(n))

def circulo2(n: int) -> int:
    return len([(x, y)
                for x in range(0, n)
                for y in range(0, raizCuadradaEntera(n * n - x * x) + 1)
                if x * x + y * y < n * n])

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=1, max_value=100))
def test_circulo(n: int) -> None:
    assert circulo1(n) == circulo2(n)

# La comprobación es
#    src> poetry run pytest -q puntos_dentro_del_circulo.py
#    1 passed in 0.34s

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('circulo1(2000)')
#    0.71 segundos
#    >>> tiempo('circulo2(2000)')
#    0.76 segundos
