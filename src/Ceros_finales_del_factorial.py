# Ceros_finales_del_factorial.py
# Ceros finales del factorial.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-enero-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    cerosDelFactorial : (int) -> int
# tal que cerosDelFactorial(n) es el número de ceros en que termina el
# factorial de n. Por ejemplo,
#    cerosDelFactorial(24)                  == 4
#    cerosDelFactorial(25)                  == 6
#    len(str(cerosDelFactorial(10**70000))) == 70000
# ---------------------------------------------------------------------

from itertools import takewhile
from math import factorial
from sys import set_int_max_str_digits
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

set_int_max_str_digits(10**6)

# 1ª solución
# ===========

# ceros(n) es el número de ceros en los que termina el número n. Por
# ejemplo,
#    ceros(320000)  ==  4
def ceros(n: int) -> int:
    r = 0
    while n % 10 == 0 and n != 0:
        r += 1
        n //= 10
    return r

def cerosDelFactorial1(n: int) -> int:
    return ceros(factorial(n))

# 2ª solución
# ===========

def ceros2(n: int) -> int:
    return len(list(takewhile(lambda x: x == '0', reversed(str(n)))))

def cerosDelFactorial2(n: int) -> int:
    return ceros2(factorial(n))

# 3ª solución
# =============

def cerosDelFactorial3(n: int) -> int:
    r = 0
    while n >= 5:
        n = n // 5
        r += n
    return r

# Verificación
# ============

def test_cerosDelFactorial() -> None:
    for cerosDelFactorial in [cerosDelFactorial1,
                              cerosDelFactorial2,
                              cerosDelFactorial3]:
        assert cerosDelFactorial(24) == 4
        assert cerosDelFactorial(25) == 6
    print("Verificado")

# La verificación es
#    >>> test_cerosDelFactorial()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.integers(min_value=0, max_value=1000))
def test_cerosDelFactorial_equiv(n: int) -> None:
    r = cerosDelFactorial1(n)
    assert cerosDelFactorial2(n) == r
    assert cerosDelFactorial3(n) == r

# La comprobación es
#    >>> test_cerosDelFactorial_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('cerosDelFactorial1(6*10**4)')
#    2.47 segundos
#    >>> tiempo('cerosDelFactorial2(6*10**4)')
#    0.77 segundos
#    >>> tiempo('cerosDelFactorial3(6*10**4)')
#    0.00 segundos

# Comprobación de todas las propiedades
# =====================================

# La comprobación es
#    src> poetry run pytest -v Ceros_finales_del_factorial.py
#       test_cerosDelFactorial PASSED
#       test_cerosDelFactorial_equiv PASSED
