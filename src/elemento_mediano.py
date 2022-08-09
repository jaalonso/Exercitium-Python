# elemento_mediano.py
# Elemento mediano.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 26-agosto-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    mediano : (int, int, int) -> int
# tal que mediano(x, y, z) es el número mediano de los tres números x, y
# y z. Por ejemplo,
#    mediano(3, 2, 5) == 3
#    mediano(2, 4, 5) == 4
#    mediano(2, 6, 5) == 5
#    mediano(2, 6, 6) == 6
# ---------------------------------------------------------------------


def mediano(x, y, z):
    return x + y + z - min([x, y, z]) - max([x, y, z])
