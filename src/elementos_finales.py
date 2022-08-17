# elementos_finales.py
# Elementos finales.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 23-agosto-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    finales : (int, List[A]) -> List[A]
# tal que finales(n, xs) es la lista formada por los n finales
# elementos de xs. Por ejemplo,
#    finales(3, [2, 5, 4, 7, 9, 6])  ==  [7, 9, 6]
# ---------------------------------------------------------------------

from hypothesis import given, strategies as st

# 1ª definición
def finales1(n, xs):
    if len(xs) <= n:
        return xs
    return xs[len(xs) - n:]

# 2ª definición
def finales2(n, xs):
    if n == 0:
        return []
    return xs[-n:]

# 3ª definición
def finales3(n, xs):
    ys = list(reversed(xs))
    return list(reversed(ys[:n]))

# La propiedad es
@given(st.integers(min_value=0), st.lists(st.integers()))
def test_equiv_finales(n, xs):
    assert finales1(n, xs) == finales2(n, xs) == finales3(n, xs)

# La comprobación es
#    src> poetry run pytest -q elementos_finales.py
#    1 passed in 0.18s
