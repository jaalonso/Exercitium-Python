# el_primero_al_final.py
# El primero al final.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 16-agosto-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    rota1 : (List[A]) -> List[A]
# tal que rota1(xs) es la lista obtenida poniendo el primer elemento de
# xs al final de la lista. Por ejemplo,
#    rota1([3, 2, 5, 7]) == [2, 5, 7, 3]
#    rota1(['a', 'b', 'c']) == ['b', 'c', 'a']
# ---------------------------------------------------------------------

from typing import List, TypeVar

A = TypeVar("A")


def rota1(xs):
    # type: (List[A]) -> List[A]
    return xs[1:] + [xs[0]]
