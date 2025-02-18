# Matriz_Toeplitz.py
# Matrices de Toepliz
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 18-febrero-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Una [matriz de Toeplitz](https://tinyurl.com/zqzokbm) es una matriz
# cuadrada que es constante a lo largo de las diagonales paralelas a la
# diagonal principal. Por ejemplo,
#    |2 5 1 6|       |2 5 1 6|
#    |4 2 5 1|       |4 2 6 1|
#    |7 4 2 5|       |7 4 2 5|
#    |9 7 4 2|       |9 7 4 2|
# la primera es una matriz de Toeplitz y la segunda no lo es.
#
# Las anteriores matrices se pueden definir por
#    ej1 = [[2,5,1,6],[4,2,5,1],[7,4,2,5],[9,7,4,2]]
#    ej2 = [[2,5,1,6],[4,2,6,1],[7,4,2,5],[9,7,4,2]]
#
# Definir la función
#    esToeplitz : (list[list[A]]) -> bool
# tal que esToeplitz(p) se verifica si la matriz p es de Toeplitz. Por
# ejemplo,
#    esToeplitz(ej1)  ==  True
#    esToeplitz(ej2)  ==  False
# ---------------------------------------------------------------------

from timeit import Timer, default_timer
from typing import TypeVar

from src.Diagonales_principales import diagonalesPrincipales1

A = TypeVar('A')

# 1ª solución
# ===========

ej1: list[list[int]] = [[2,5,1,6],[4,2,5,1],[7,4,2,5],[9,7,4,2]]
ej2: list[list[int]] = [[2,5,1,6],[4,2,6,1],[7,4,2,5],[9,7,4,2]]

#  esCuadrada(p) se verifica si la matriz p es cuadrada. Por ejemplo,
#    >>> esCuadrada([[1,2],[3,4]])       == True
#    >>> esCuadrada([[1,2],[3,4],[5,6]]) == False
#    >>> esCuadrada([[1,2,3],[4,5,6]])   == False
def esCuadrada(p : list[list[A]]) -> bool:
    return all(len(elemento) == len(p) for elemento in p)

# todosIguales(xs) se verifica si todos los elementos de xs son
# iguales. Por ejemplo,
#    todosIguales([5,5,5])  ==  True
#    todosIguales([5,4,5])  ==  False
def todosIguales(xs: list[A]) -> bool:
    return all(x == xs[0] for x in xs)

def esToeplitz1(p: list[list[A]]) -> bool:
    return esCuadrada(p) and all(todosIguales(xs) for xs in diagonalesPrincipales1(p))

# 2ª solución
# ===========

def esToeplitz2(p: list[list[A]]) -> bool:
    n = len(p)
    return all(len(xs) == n for xs in p) and \
           all(p[i][j] == p[i+1][j+1] for i in range(0,n-1)
                                      for j in range(0,n-1))

# Verificación
# ============

def test_esToeplitz() -> None:
    for esToeplitz in [esToeplitz1, esToeplitz2]:
        assert esToeplitz(ej1)
        assert not esToeplitz(ej2)
    print("Verificado")

# La verificación es
#    >>> test_esToeplitz()
#    Verificado

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('esToeplitz1([[1]*2*10**3]*2*10**3)')
#    1.52 segundos
#    >>> tiempo('esToeplitz2([[1]*2*10**3]*2*10**3)')
#    0.51 segundos
