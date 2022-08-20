# primeros_y_ultimos_elementos.py
# Primeros y últimos elementos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 25-agosto-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    extremos : (int, list[A]) -> list[A]
# tal que extremos(n, xs) es la lista formada por los n primeros
# elementos de xs y los n finales elementos de xs. Por ejemplo,
#    extremos(3, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3])  ==  [2, 6, 7, 9, 2, 3]
# ---------------------------------------------------------------------

from typing import TypeVar

A = TypeVar('A')

def extremos(n: int, xs: list[A]) -> list[A]:
    return xs[:n] + xs[-n:]
