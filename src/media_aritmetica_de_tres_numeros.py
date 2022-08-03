# media_aritmetica_de_tres_numeros.py
# Media aritmética de tres números.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 8-agosto-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    media3 : (float, float, float) -> float
# tal que (media3 x y z) es la media aritmética de los números x, y y
# z. Por ejemplo,
#    media3(1, 3, 8)   ==  4.0
#    media3(-1, 0, 7)  ==  2.0
#    media3(-3, 0, 3)  ==  0.0
# ---------------------------------------------------------------------

# 1ª solución
# ===========

def media3a(x, y, z):
    # type: (float, float, float) -> float
    return (x + y + z)/3


# 2ª solución
# ===========

def media3b(x, y, z):
    # type: (float, float, float) -> float
    return sum([x, y, z]) / 3
