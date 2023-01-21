# colaConDosListas.py
# Implementación de las colas mediante dos listas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 2-enero-2023
# ======================================================================

# Se define la clase Cola con los siguientes métodos:
#    + inserta(x) añade x al final de la cola.
#    + primero() es el primero de la cola.
#    + resto() elimina el primero de la cola.
#    + esVacia() se verifica si la cola es vacía.
# Por ejemplo,
#    >>> c = Cola()
#    >>> print(c)
#    -
#    >>> c.inserta(5)
#    >>> c.inserta(2)
#    >>> c.inserta(3)
#    >>> c.inserta(4)
#    >>> print(c)
#    5 | 2 | 3 | 4
#    >>> c.primero()
#    5
#    >>> c.resto()
#    >>> print(c)
#    2 | 3 | 4
#    >>> c.esVacia()
#    False
#    >>> c = Cola()
#    >>> c.esVacia()
#    True
#
# Además se definen las correspondientes funciones. Por ejemplo,
#    >>> print(vacia())
#    -
#    >>> print(inserta(4, inserta(3, inserta(2, inserta(5, vacia())))))
#    5 | 2 | 3 | 4
#    >>> primero(inserta(4, inserta(3, inserta(2, inserta(5, vacia())))))
#    5
#    >>> print(resto(inserta(4, inserta(3, inserta(2, inserta(5, vacia()))))))
#    2 | 3 | 4
#    >>> esVacia(inserta(4, inserta(3, inserta(2, inserta(5, vacia())))))
#    False
#    >>> esVacia(vacia())
#    True
#
# Finalmente, se define un generador aleatorio de colas y se comprueba
# que las colas cumplen las propiedades de su especificación.

__all__ = [
    'Cola',
    'vacia',
    'inserta',
    'primero',
    'resto',
    'esVacia',
    'colaAleatoria'
]

from copy import deepcopy
from dataclasses import dataclass, field
from typing import Generic, TypeVar

from hypothesis import assume, given
from hypothesis import strategies as st

A = TypeVar('A')

# Clase de las colas mediante listas
# ==================================

@dataclass
class Cola(Generic[A]):
    _primera: list[A] = field(default_factory=list)
    _segunda: list[A] = field(default_factory=list)

    def _elementos(self) -> list[A]:
        xs = self._primera
        ys = self._segunda
        return xs + list(reversed(ys))

    def __str__(self) -> str:
        def aux(xs: list[A]) -> str:
            if len(xs) == 0:
                return '-'
            cadena = ''
            for x in xs[:-1]:
                cadena = cadena + str(x) + ' | '
            return cadena + str(xs[-1])

        return aux(self._elementos())

    def __eq__(self, c) -> bool:
        return self._elementos() == c._elementos()

    def inserta(self, y: A) -> None:
        xs = self._primera
        ys = self._segunda
        if not xs:
            ys.insert(0, y)
            xs.extend(ys[::-1])
            self._segunda = []
        if xs:
            ys.insert(0, y)

    def esVacia(self) -> bool:
        return len(self._primera) == 0

    def primero(self) -> A:
        return self._primera[0]

    def resto(self) -> None:
        xs = self._primera
        ys = self._segunda
        del xs[0]
        if not xs:
            xs.extend(ys[::-1])
            self._segunda = []

# Funciones del tipo de las listas
# ================================

def vacia() -> Cola[A]:
    c: Cola[A] = Cola()
    return c

def inserta(x: A, c: Cola[A]) -> Cola[A]:
    _aux = deepcopy(c)
    _aux.inserta(x)
    return _aux

def esVacia(c: Cola[A]) -> bool:
    return c.esVacia()

def primero(c: Cola[A]) -> A:
    return c.primero()

def resto(c: Cola[A]) -> Cola[A]:
    _aux = deepcopy(c)
    _aux.resto()
    return _aux

# Generador de colas
# ==================

def colaAleatoria() -> st.SearchStrategy[Cola[int]]:
    def _build_cola(elementos: list[int]) -> Cola[int]:
        cola: Cola[int] = vacia()
        for x in elementos:
            cola = inserta(x, cola)
        return cola
    return st.builds(_build_cola, st.lists(st.integers()))

# Comprobación de las propiedades de las colas
# ============================================

# Las propiedades son
@given(c=colaAleatoria(), x=st.integers())
def test_cola1(c: Cola[int], x: int) -> None:
    assert primero(inserta(x, vacia())) == x
    assert resto(inserta(x, vacia())) == vacia()
    assert esVacia(vacia())
    assert not esVacia(inserta(x, c))

@given(c=colaAleatoria(), x=st.integers())
def test_cola2(c: Cola[int], x: int) -> None:
    assume(not esVacia(c))
    assert primero(inserta(x, c)) == primero(c)
    assert resto(inserta(x, c)) == inserta(x, resto(c))

# La comprobación es
#    > poetry run pytest -q colaConListas.py
#    2 passed in 0.40s
