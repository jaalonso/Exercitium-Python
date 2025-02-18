# Maximos_locales.py
# Máximos locales.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 19-febrero-2025
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Un máximo local de una lista es un elemento de la lista que es mayor
# que su predecesor y que su sucesor en la lista. Por ejemplo, 5 es un
# máximo local de [3,2,5,3,7,7,1,6,2] ya que es mayor que 2 (su
# predecesor) y que 3 (su sucesor).
#
# Definir la función
#    maximosLocales : (xs: list[int]) -> list[int]
# tal que maximosLocales(xs) es la lista de los máximos locales de la
# lista xs. Por ejemplo,
#    maximosLocales([3,2,5,3,7,7,1,6,2]) == [5,6]
#    maximosLocales(list(range(0, 100))) == []
# ---------------------------------------------------------------------

from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

def maximosLocales1(xs: list[int]) -> list[int]:
    if len(xs) < 3:
        return []
    x, y, z, *ys = xs
    if y > x and y > z:
        return [y] + maximosLocales1([z] + ys)
    return maximosLocales1([y, z] + ys)

# 2ª solución
# ===========

def maximosLocales2(xs: list[int]) -> list[int]:
    ys: list[int] = []
    if len(xs) < 3:
        return ys
    for i in range(1, len(xs) - 1):
        if xs[i] > xs[i - 1] and xs[i] > xs[i + 1]:
            ys.append(xs[i])
    return ys

# 3ª solución
# ===========

def maximosLocales3(xs: list[int]) -> list[int]:
    return [y for x, y, z in zip(xs, xs[1:], xs[2:]) if y > x and y > z]

# Verificación
# ============

def test_maximosLocales() -> None:
    for maximosLocales in [maximosLocales1,
                           maximosLocales2,
                           maximosLocales3]:
        assert maximosLocales([3,2,5,3,7,7,1,6,2]) == [5,6]
        assert maximosLocales(list(range(0, 100))) == []
    print("Verificado")

# La verificación es
#    >>> test_maximosLocales()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
@given(st.lists(st.integers()))
def test_maximosLocales_equiv(xs: list[int]) -> None:
    r = maximosLocales1(xs)
    assert maximosLocales2(xs) == r
    assert maximosLocales3(xs) == r

# La comprobación es
#    >>> test_maximosLocales_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('maximosLocales1([1,2,3]*(10**4))')
#    3.19 segundos
#    >>> tiempo('maximosLocales2([1,2,3]*(10**4))')
#    0.01 segundos
#    >>> tiempo('maximosLocales3([1,2,3]*(10**4))')
#    0.01 segundos
#
#    >>> tiempo('maximosLocales2([1,2,3]*(10**7))')
#    3.95 segundos
#    >>> tiempo('maximosLocales3([1,2,3]*(10**7))')
#    1.85 segundos
