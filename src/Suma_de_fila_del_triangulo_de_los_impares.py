# Suma_de_fila_del_triangulo_de_los_impares.hs
# Suma fila del triángulo de los impares.
# José A. Alonso Jiménez
# Sevilla, 29 de febrero 2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Se condidera el siguiente triángulo de números impares
#
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
#
# Definir la función
#    sumaFilaTrianguloImpares : (int) -> int
# tal que sumaFilaTrianguloImpares(n) es la suma de la n-ésima fila
# del triángulo de los números impares. Por ejemplo,
#    sumaFilaTrianguloImpares(1)  ==  1
#    sumaFilaTrianguloImpares(2)  ==  8
#    len(str(sumaFilaTrianguloImpares(10**500)))    ==  1501
#    len(str(sumaFilaTrianguloImpares(10**5000)))   ==  15001
#    len(str(sumaFilaTrianguloImpares(10**50000)))  ==  150001
# ---------------------------------------------------------------------

from sys import set_int_max_str_digits
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

set_int_max_str_digits(10**6)

# 1ª solución
# ===========

def sumaFilaTrianguloImpares1(n: int) -> int:
    return sum(range(n**2-n+1, n**2+n, 2))

# 2ª solución
# ===========

def sumaFilaTrianguloImpares2(n: int) -> int:
    return n**3

# Verificación
# ============

def test_sumaFilaTrianguloImpares() -> None:
    for sumaFilaTrianguloImpares in [sumaFilaTrianguloImpares1,
                                     sumaFilaTrianguloImpares2]:
        assert sumaFilaTrianguloImpares(1) == 1
        assert sumaFilaTrianguloImpares(2) == 8
    print("Verificado")

# La verificación es
#    >>> test_sumaFilaTrianguloImpares()
#    Verificado

# Equivalencia de las definiciones
# ================================

# La propiedad es
@given(st.integers(min_value=1, max_value=1000))
def test_sumaFilaTrianguloImpares_equiv(n: int) -> None:
    assert sumaFilaTrianguloImpares1(n) == sumaFilaTrianguloImpares2(n)

# La comprobación es
#    >>> test_sumaFilaTrianguloImpares_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('len(str(sumaFilaTrianguloImpares1(6*10**7)))')
#    2.04 segundos
#    >>> tiempo('len(str(sumaFilaTrianguloImpares2(6*10**7)))')
#    0.00 segundos
