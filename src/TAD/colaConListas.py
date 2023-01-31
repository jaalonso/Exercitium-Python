# colaConListas.py
# Implementación de las colas mediante listas.
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
#    >>> c
#    -
#    >>> c.inserta(5)
#    >>> c.inserta(2)
#    >>> c.inserta(3)
#    >>> c.inserta(4)
#    >>> c
#    5 | 2 | 3 | 4
#    >>> c.primero()
#    5
#    >>> c.resto()
#    >>> c
#    2 | 3 | 4
#    >>> c.esVacia()
#    False
#    >>> c = Cola()
#    >>> c.esVacia()
#    True
#
# Además se definen las correspondientes funciones. Por ejemplo,
#    >>> vacia()
#    -
#    >>> inserta(4, inserta(3, inserta(2, inserta(5, vacia()))))
#    5 | 2 | 3 | 4
#    >>> inserta(4, inserta(3, inserta(2, inserta(5, vacia()))))
#    5
#    >>> resto(inserta(4, inserta(3, inserta(2, inserta(5, vacia())))))
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
    _elementos: list[A] = field(default_factory=list)

    def __repr__(self) -> str:
        """
        Devuelve una cadena con los elementos de la cola separados por " | ".
        Si la cola está vacía, devuelve "-".
        """
        if not self._elementos:
            return '-'
        return ' | '.join(str(x) for x in self._elementos)

    def inserta(self, x: A) -> None:
        """
        Inserta el elemento x al final de la cola.
        """
        self._elementos.append(x)

    def esVacia(self) -> bool:
        """
        Comprueba si la cola está vacía.

        Devuelve True si la cola está vacía, False en caso contrario.
        """
        return not self._elementos

    def primero(self) -> A:
        """
        Devuelve el primer elemento de la cola.
        """
        return self._elementos[0]

    def resto(self) -> None:
        """
        Elimina el primer elemento de la cola
        """
        self._elementos.pop(0)

# Funciones del tipo de las listas
# ================================

def vacia() -> Cola[A]:
    """
    Crea y devuelve una cola vacía de tipo A.
    """
    c: Cola[A] = Cola()
    return c

def inserta(x: A, c: Cola[A]) -> Cola[A]:
    """
    Inserta un elemento x en la cola c y devuelve una nueva cola con
    el elemento insertado.
    """
    _aux = deepcopy(c)
    _aux.inserta(x)
    return _aux

def esVacia(c: Cola[A]) -> bool:
    """
    Devuelve True si la cola está vacía, False si no lo está.
    """
    return c.esVacia()

def primero(c: Cola[A]) -> A:
    """
    Devuelve el primer elemento de la cola c.
    """
    return c.primero()

def resto(c: Cola[A]) -> Cola[A]:
    """
    Elimina el primer elemento de la cola c y devuelve una copia de la
    cola resultante.
    """
    _aux = deepcopy(c)
    _aux.resto()
    return _aux

# Generador de colas
# ==================

def colaAleatoria() -> st.SearchStrategy[Cola[int]]:
    """
    Genera una estrategia de búsqueda para generar colas de enteros de
    forma aleatoria.

    Utiliza la librería Hypothesis para generar una lista de enteros y
    luego se convierte en una instancia de la clase cola.
    """
    return st.lists(st.integers()).map(Cola)

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
#    1 passed in 0.24s
