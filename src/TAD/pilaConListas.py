# pilaConListas.py
# Implementación de las pilas mediante listas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 2-enero-2023
# ======================================================================

# Se define la clase Pila con los siguientes métodos:
#    + apila(x) añade x al principio de la pila.
#    + cima() devuelve la cima de la pila.
#    + desapila() elimina la cima de la pila.
#    + esVacia() se verifica si la pila es vacía.
# Por ejemplo,
#    >>> p = Pila()
#    >>> print(p)
#    -
#    >>> p.apila(5)
#    >>> p.apila(2)
#    >>> p.apila(3)
#    >>> p.apila(4)
#    >>> print(p)
#    4 | 3 | 2 | 5
#    >>> p.cima()
#    4
#    >>> p.desapila()
#    >>> print(p)
#    3 | 2 | 5
#    >>> p.esVacia()
#    False
#    >>> p = Pila()
#    >>> p.esVacia()
#    True
#
# Además se definen las correspondientes funciones. Por ejemplo,
#    >>> print(vacia())
#    -
#    >>> print(apila(4, apila(3, apila(2, apila(5, vacia())))))
#    4 | 3 | 2 | 5
#    >>> print(cima(apila(4, apila(3, apila(2, apila(5, vacia()))))))
#    4
#    >>> print(desapila(apila(4, apila(3, apila(2, apila(5, vacia()))))))
#    3 | 2 | 5
#    >>> print(esVacia(apila(4, apila(3, apila(2, apila(5, vacia()))))))
#    False
#    >>> print(esVacia(vacia()))
#    True
#
# Finalmente, se define un generador aleatorio de pilas y se comprueba
# que las pilas cumplen las propiedades de su especificación.

__all__ = [
    'Pila',
    'vacia',
    'apila',
    'esVacia',
    'cima',
    'desapila',
    'pilaAleatoria'
]

from copy import deepcopy
from dataclasses import dataclass, field
from typing import Generic, TypeVar

from hypothesis import given
from hypothesis import strategies as st

A = TypeVar('A')

# Clase de las pilas mediante Listas
# ==================================

@dataclass
class Pila(Generic[A]):
    _elementos: list[A] = field(default_factory=list)

    def __str__(self) -> str:
        if len(self._elementos) == 0:
            return '-'
        return " | ".join(str(x) for x in self._elementos)

    def apila(self, x: A) -> None:
        self._elementos.insert(0, x)

    def esVacia(self) -> bool:
        return not self._elementos

    def cima(self) -> A:
        return self._elementos[0]

    def desapila(self) -> None:
        self._elementos.pop(0)

# Funciones del tipo de las listas
# ================================

def vacia() -> Pila[A]:
    p: Pila[A] = Pila()
    return p

def apila(x: A, p: Pila[A]) -> Pila[A]:
    aux = deepcopy(p)
    aux.apila(x)
    return aux

def esVacia(p: Pila[A]) -> bool:
    return p.esVacia()

def cima(p: Pila[A]) -> A:
    return p.cima()

def desapila(p: Pila[A]) -> Pila[A]:
    aux = deepcopy(p)
    aux.desapila()
    return aux

# Generador de pilas
# ==================

def pilaAleatoria() -> st.SearchStrategy[Pila[int]]:
    return st.lists(st.integers()).map(Pila)

# Comprobación de las propiedades de las pilas
# ============================================

# Las propiedades son
@given(p=pilaAleatoria(), x=st.integers())
def test_pila(p: Pila[int], x: int) -> None:
    assert cima(apila(x, p)) == x
    assert desapila(apila(x, p)) == p
    assert esVacia(vacia())
    assert not esVacia(apila(x, p))

# La comprobación es
#    > poetry run pytest -q pilaConListas.py
#    1 passed in 0.25s
