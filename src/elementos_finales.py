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


from typing import List, TypeVar

A = TypeVar('A')


# 1ª definición
def finales1(n, xs):
    # type: (int, List[A]) -> List[A]
    return xs[len(xs) - n:]


# 2ª definición
def finales2(n, xs):
    # type: (int, List[A]) -> List[A]
    return xs[-n:]


# 3ª definición
def finales3(n, xs):
    # type: (int, List[A]) -> List[A]
    ys = list(reversed(xs))
    return list(reversed(ys[:n]))
