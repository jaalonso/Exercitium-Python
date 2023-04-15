# maximo_de_tres_numeros.py
# Máximo de tres números.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 15-agosto-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    maxTres : (int, int, int) -> int
# tal que maxTres(x, y, z) es el máximo de x, y y z. Por ejemplo,
#    maxTres(6, 2, 4)  ==  6
#    maxTres(6, 7, 4)  ==  7
#    maxTres(6, 7, 9)  ==  9
# ---------------------------------------------------------------------

def maxTres(x: int, y: int, z: int) -> int:
    return max(x, y, z)
