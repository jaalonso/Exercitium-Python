# el_tipo_de_las_listas.py
# El tipo de las listas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 28-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El tipo de las listas, con elementos de tipo a, se puede definir por
#    @dataclass
#    class Lista(Generic[A]):
#        pass
#
#    @dataclass
#    class Nil(Lista[A]):
#        pass
#
#    @dataclass
#    class Cons(Lista[A]):
#        x: A
#        xs: Lista[A]
# Por ejemplo, la lista [4,2,5] se representa por
# Cons(4, Cons(2, Cons(5, Nil()))).
#
# Definir la función
#    longitud :: Lista a -> Int
# tal que  (longitud xs) es la longitud de la lista xs. Por ejemplo,
#    >>> longitud(Cons(4, Cons(2, Cons(5, Nil()))))
#    3
# ---------------------------------------------------------------------

from dataclasses import dataclass
from typing import Generic, TypeVar

A = TypeVar("A")

@dataclass
class Lista(Generic[A]):
    pass

@dataclass
class Nil(Lista[A]):
    pass

@dataclass
class Cons(Lista[A]):
    x: A
    xs: Lista[A]

def longitud(xs: Lista[A]) -> int:
    match xs:
        case Nil():
            return 0
        case Cons(_, xs):
            return 1 + longitud(xs)
    assert False
