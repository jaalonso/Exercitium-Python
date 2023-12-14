# ListaVector.oy
# Transformación de listas a vectores.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 9-diciembre-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El tipo de los vectores, usando la librería Data.Array, se pueden
# definir por
#    from typing import TypeVar
#    import numpy as np
#    import numpy.typing as npt
#    A = TypeVar('A')
#    Vector = npt.NDArray[A]
#
# Definir la función
#    listaVector : (list[A]) -> Vector
# tal que listaVector(xs) es el vector correspondiente a la lista
# xs. Por ejemplo,
#    >>> listaVector([4,7,5])
#    array([4, 7, 5])
# ---------------------------------------------------------------------

from typing import TypeVar
import numpy as np
import numpy.typing as npt

A = TypeVar('A')

Vector = npt.NDArray[A]

# 1ª solución
# ===========

def listaVector(xs: list[A]) -> Vector:
    return np.array(xs)

# Verificación
# ============

def test_listaVector() -> None:
    assert listaVector([4,7,5]).all() == np.array([4, 7, 5]).all()
    print("Verificado")

# La verificación es
#    >>> test_listaVector()
#    Verificado
