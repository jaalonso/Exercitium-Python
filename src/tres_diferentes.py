# tres_diferentes.py
# Tres diferentes
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 30-agosto-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    tresDiferentes : (int, int, int) -> bool
# tal que tresDiferentes(x, y, z) se verifica si los elementos x, y y z
# son distintos. Por ejemplo,
#    tresDiferentes(3, 5, 2)  ==  True
#    tresDiferentes(3, 5, 3)  ==  False
# ---------------------------------------------------------------------


def tresDiferentes(x, y, z):
    # type: (int, int, int) -> bool
    return x != y and x != z and y != z
