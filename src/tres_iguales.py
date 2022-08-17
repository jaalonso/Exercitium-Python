# tres_iguales.py
# Tres iguales
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-agosto-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    tresIguales : (int, int, int) -> bool
# tal que tresIguales(x, y, z) se verifica si los elementos x, y y z son
# iguales. Por ejemplo,
#    tresIguales(4, 4, 4)  ==  True
#    tresIguales(4, 3, 4)  ==  False
# ---------------------------------------------------------------------

from hypothesis import given, strategies as st

# 1ª definición
def tresIguales1(x, y, z):
    # type: (int, int, int) -> bool
    return x == y and y == z

# 2ª definición
def tresIguales2(x, y, z):
    # type: (int, int, int) -> bool
    return x == y == z

# La propiedad de equivalencia es
@given(st.integers(), st.integers(), st.integers())
def test_equiv_tresIguales(x, y, z):
    assert tresIguales1(x, y, z) == tresIguales2(x, y, z)

# La comprobación es
#    src> poetry run pytest -q tres_iguales.py
#    1 passed in 0.16s
