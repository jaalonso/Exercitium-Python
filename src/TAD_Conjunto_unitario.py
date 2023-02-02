# TAD_Conjunto_unitario.py
# TAD de los conjuntos: Conjunto unitario.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 6-marzo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Utilizando el [tipo abstracto de datos de los conjuntos](https://bit.ly/3HbB7fo)
# definir la función
#    unitario :: Ord a => a -> Conj a
# tal que (unitario x) es el conjunto {x}. Por ejemplo,
#    unitario 5 == {5}
# ---------------------------------------------------------------------

from typing import TypeVar

from src.TAD.conjunto import (Conj, inserta, vacio)

A = TypeVar('A', int, float, str)

def unitario(x: A) -> Conj[A]:
    return inserta(x, vacio())
