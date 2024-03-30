# algoritmo_de_Euclides_del_mcd.py
# Algoritmo de Euclides del mcd.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 26-octubre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Dados dos números naturales, a y b, es posible calcular su máximo
# común divisor mediante el Algoritmo de Euclides. Este algoritmo se
# puede resumir en la siguiente fórmula:
#    mcd(a,b) = a,                   si b = 0
#             = mcd (b, a módulo b), si b > 0
#
# Definir la función
#    mcd : (int, nt) -> int
# tal que mcd(a, b) es el máximo común divisor de a y b calculado
# mediante el algoritmo de Euclides. Por ejemplo,
#    mcd(30, 45)  ==  15
#    mcd(45, 30)  ==  15
#
# Comprobar con Hypothesis que el máximo común divisor de dos números a
# y b (ambos mayores que 0) es siempre mayor o igual que 1 y además es
# menor o igual que el menor de los números a  y b.
# ---------------------------------------------------------------------

from hypothesis import given
from hypothesis import strategies as st


def mcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return mcd(b, a % b)

# La propiedad es
@given(st.integers(min_value=1, max_value=1000),
       st.integers(min_value=1, max_value=1000))
def test_mcd(a: int, b: int) -> None:
    assert 1 <= mcd(a, b) <= min(a, b)

# La comprobación es
#    src> poetry run pytest -q algoritmo_de_Euclides_del_mcd.py
#    1 passed in 0.22s
