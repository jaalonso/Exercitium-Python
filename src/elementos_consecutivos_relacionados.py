# elementos_consecutivos_relacionados.py
# Elementos consecutivos relacionados.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 16-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    relacionados : (Callable[[A, A], bool], list[A]) -> bool
# tal que relacionados(r, xs) se verifica si para todo par (x,y) de
# elementos consecutivos de xs se cumple la relación r. Por ejemplo,
#    >>> relacionados(lambda x, y: x < y, [2, 3, 7, 9])
#    True
#    >>> relacionados(lambda x, y: x < y, [2, 3, 1, 9])
#    False
# ---------------------------------------------------------------------

from typing import Callable, TypeVar

A = TypeVar('A')

# 1ª solución
# ===========

def relacionados1(r: Callable[[A, A], bool], xs: list[A]) -> bool:
    return all((r(x, y) for (x, y) in zip(xs, xs[1:])))

# 2ª solución
# ===========

def relacionados2(r: Callable[[A, A], bool], xs: list[A]) -> bool:
    if len(xs) >= 2:
        return r(xs[0], xs[1]) and relacionados1(r, xs[1:])
    return True
