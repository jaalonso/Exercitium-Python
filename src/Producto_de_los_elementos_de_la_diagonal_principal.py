# Producto_de_los_elementos_de_la_diagonal_principal.py
# Producto de los elementos de la diagonal principal.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 9-marzo-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Las matrices se pueden representar como lista de listas de la misma
# longitud, donde cada uno de sus elementos representa una fila de la
# matriz.
#
# Definir la función
#    productoDiagonalPrincipal :: Num a => [[a]] -> a
# tal que (productoDiagonalPrincipal xss) es el producto de los
# elementos de la diagonal principal de la matriz cuadrada xss. Por
# ejemplo,
#    productoDiagonal([[3,5,2],[4,7,1],[6,9,8]])  ==  168
#    productoDiagonal([[1, 2, 3, 4, 5]]*5)        ==  120
#    len(str(productoDiagonal([range(1, 30001)]*30000)))  ==  121288
# ---------------------------------------------------------------------

from functools import reduce
from operator import mul
from sys import set_int_max_str_digits, setrecursionlimit
from timeit import Timer, default_timer

set_int_max_str_digits(10**6)
setrecursionlimit(10**6)

# 1ª solución
# ===========

# diagonal1(xss) es la diagonal de la matriz xss. Por ejemplo,
#    diagonal1([[3,5,2],[4,7,1],[6,9,0]])  ==  [3,7,0]
#    diagonal1([[3,5],[4,7],[6,9]])        ==  [3,7]
#    diagonal1([[3,5,2],[4,7,1]])          ==  [3,7]
def diagonal1(xss: list[list[int]]) -> list[int]:
    if not xss:
        return []
    if not xss[0]:
        return []
    return [xss[0][0]] + diagonal1(list(map((lambda ys : ys[1:]), xss[1:])))

def producto(xs: list[int]) -> int:
    return reduce(mul, xs)

def productoDiagonal1(xss: list[list[int]]) -> int:
    return producto(diagonal1(xss))

# 2ª solución
# ===========

def diagonal2(xss: list[list[int]]) -> list[int]:
    n = min(len(xss), len(xss[0]))
    return [xss[k][k] for k in range(n)]

def productoDiagonal2(xss: list[list[int]]) -> int:
    return producto(diagonal2(xss))

# 3ª solución
# ===========

def productoDiagonal3(xss: list[list[int]]) -> int:
    if not xss:
        return 1
    if not xss[0]:
        return 1
    return xss[0][0] * productoDiagonal3(list(map((lambda ys : ys[1:]), xss[1:])))

# Verificación
# ============

def test_productoDiagonal() -> None:
    for productoDiagonal in [productoDiagonal1, productoDiagonal2,
                             productoDiagonal3]:
        assert productoDiagonal([[3,5,2],[4,7,1],[6,9,8]]) == 168
        assert productoDiagonal([[1, 2, 3, 4, 5]]*5) == 120
    print("Verificado")

# La verificación es
#    >>> test_productoDiagonal()
#    Verificado

# Comparación de eficiencia
# =========================

# ejemplo(n) es la matriz con n filas formadas por los números de 1 a
# n. Por ejemplo,
#    >>> ejemplo(3)
#    [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
def ejemplo(n: int) -> list[list[int]]:
    return [list(range(1, n+1))]*n

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('productoDiagonal1(ejemplo(1200))')
#    1.97 segundos
#    >>> tiempo('productoDiagonal2(ejemplo(1200))')
#    0.00 segundos
#    >>> tiempo('productoDiagonal3(ejemplo(1200))')
#    1.56 segundos
