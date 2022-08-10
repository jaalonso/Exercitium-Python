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

# 1ª definición
def tresIguales(x, y, z):
    # type: (int, int, int) -> bool
    return x == y & y == z


# 2ª definición
def tresIguales2(x, y, z):
    return x == y == z
