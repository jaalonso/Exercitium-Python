# rango_de_una_lista.py
# Rango de una lista.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 18-agosto-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    rango : (List[int]) -> List[int]
# tal que rango(xs) es la lista formada por el menor y mayor elemento
# de xs.
#    rango([3, 2, 7, 5]) == [2, 7]
# ---------------------------------------------------------------------

from typing import List

def rango(xs):
    # type: (List[int]) -> List[int]
    return [min(xs), max(xs)]
