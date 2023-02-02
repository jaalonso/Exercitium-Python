# TAD_subconjuntoPropio.py
# TAD de los conjuntos: Reconocimiento de_subconjunto propio
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 3-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de los conjuntos](https://bit.ly/3HbB7fo)
# definir la función
#    subconjuntoPropio : (Conj[A], Conj[A]) -> bool
# tal subconjuntoPropio(c1, c2) se verifica si c1 es un subconjunto
# propio de c2. Por ejemplo,
#    >>> ej1 = inserta(5, inserta(2, vacio()))
#    >>> ej2 = inserta(3, inserta(2, inserta(5, vacio())))
#    >>> ej3 = inserta(3, inserta(4, inserta(5, vacio())))
#    >>> ej4 = inserta(2, inserta(5, vacio()))
#    >>> subconjuntoPropio(ej1, ej2)
#    True
#    >>> subconjuntoPropio(ej1, ej3)
#    False
#    >>> subconjuntoPropio(ej1, ej4)
#    False
# ---------------------------------------------------------------------

from typing import TypeVar

from src.TAD.conjunto import (Conj, conjuntoAleatorio, elimina, esVacio,
                              inserta, menor, pertenece, vacio)
from src.TAD_subconjunto import subconjunto

A = TypeVar('A', int, float, str)

def subconjuntoPropio(c1: Conj[A], c2: Conj[A]) -> bool:
    return subconjunto(c1, c2) and c1 != c2

# La función subconjunto está definida en el ejercicio
# "Reconocimiento de subconjuntos" que se encuentra en
# https://bit.ly/3wPBtU5
