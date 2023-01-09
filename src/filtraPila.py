# filtraPila.py
# Filtrar pilas según una propiedad.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 24-enero-2023
# ======================================================================

# ---------------------------------------------------------------------
# Ejercicio 1: Definir la función
#    filtraPila :: (a -> Bool) -> Pila a -> Pila a
# tal que (filtraPila p q) es la pila obtenida con los elementos de
# pila q que verifican el predicado p, en el mismo orden. Por ejemplo,
#    λ> ejP1
#    1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|-
#    λ> filtraPila even ejP1
#    2|4|6|8|10|12|14|16|18|20|-
# ---------------------------------------------------------------------

from typing import Callable, TypeVar

from src.TAD.pilaConListas import Pila, apila, cima, desapila, esVacia, vacia

T = TypeVar('T')

# 1ª solución
# ===========

def filtraPila(p: Callable[[T], bool], q: Pila[T]) -> Pila[T]:
    if q.esVacia():
        return q
    cq = cima(q)
    q.desapila()
    r = filtraPila(p, q)
    if p(cq):
        r.apila(cq)
    return r

# 2ª solución
# ===========

#    >>> ejP1 = lista2Pila(list(range(10)))
#    >>> print(ejP1)
#    9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0
#    >>> print(filtraPila2(lambda x: x % 2 == 0, ejP1))
#    8 | 6 | 4 | 2 | 0
def filtraPila2(p: Callable[[T], bool], q: Pila[T]) -> Pila[T]:
    if esVacia(q):
        return q
    cq = cima(q)
    dq = desapila(q)
    r = filtraPila2(p, dq)
    if p(cq):
        return apila(cq, r)
    return r
