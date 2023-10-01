# Maxima_suma_de_los_caminos_en_una_matriz.py
# Máxima suma de los caminos en una matriz.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 19-octubre-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Los caminos desde el extremo superior izquierdo (posición (1,1))
# hasta el extremo inferior derecho (posición (3,4)) en la matriz
#    (  1  6 11  2 )
#    (  7 12  3  8 )
#    (  3  8  4  9 )
# moviéndose en cada paso una casilla hacia la derecha o hacia abajo,
# son los siguientes:
#    [1,6,11,2,8,9]
#    [1,6,11,3,8,9]
#    [1,6,12,3,8,9]
#    [1,7,12,3,8,9]
#    [1,6,11,3,4,9]
#    [1,6,12,3,4,9]
#    [1,7,12,3,4,9]
#    [1,6,12,8,4,9]
#    [1,7,12,8,4,9]
#    [1,7, 3,8,4,9]
# La suma de los caminos son 37, 38, 39, 40, 34, 35, 36, 40, 41 y 32,
# respectivamente. El camino de máxima suma es el penúltimo (1, 7, 12, 8,
# 4, 9) que tiene una suma de 41.
#
# Definir la función
#    maximaSuma : (list[list[int]]) -> int
# tal que maximaSuma(m) es el máximo de las sumas de los caminos en la
# matriz m desde el extremo superior izquierdo hasta el extremo
# inferior derecho, moviéndose en cada paso una casilla hacia abajo o
# hacia la derecha. Por ejemplo,
#    >>> maximaSuma([[1,6,11,2],[7,12,3,8],[3,8,4,9]])
#    41
#    >>> maximaSuma4([list(range(800*n+1, 800*(n+1)+1)) for n in range(800)])
#    766721999
# ---------------------------------------------------------------------

from collections import defaultdict
from sys import setrecursionlimit
from timeit import Timer, default_timer

setrecursionlimit(10**6)

# 1ª definicion de maximaSuma (con caminos1)
# ==========================================

def maximaSuma1(m: list[list[int]]) -> int:
    return max((sum(xs) for xs in caminos1(m)))

def caminos1(m: list[list[int]]) -> list[list[int]]:
    nf = len(m)
    nc = len(m[0])
    return list(reversed([list(reversed(xs)) for xs in caminos1Aux(m, (nf,nc))]))

# caminos1Aux(m, p) es la lista de los caminos invertidos en la matriz m
# desde la posición (1,1) hasta la posición p. Por ejemplo,
def caminos1Aux(m: list[list[int]], p: tuple[int, int]) -> list[list[int]]:
    (i, j) = p
    if p == (1,1):
        return [[m[0][0]]]
    if i == 1:
        return [[m[0][k-1] for k in range(j, 0, -1)]]
    if j == 1:
        return [[m[k-1][0] for k in range(i, 0, -1)]]
    return [[m[i-1][j-1]] + xs
            for xs in caminos1Aux(m, (i,j-1)) + caminos1Aux(m, (i-1,j))]

# 2ª definición de maximaSuma (con caminos2)
# ==========================================

def maximaSuma2(m: list[list[int]]) -> int:
    return max((sum(xs) for xs in caminos2(m)))

def caminos2(p: list[list[int]]) -> list[list[int]]:
    m = len(p)
    n = len(p[0])
    return [list(reversed(xs)) for xs in diccionarioCaminos(p)[(m, n)]]

# diccionarioCaminos(p) es el diccionario cuyas claves son los
# puntos de la matriz p y sus valores son los caminos a dichos
# puntos. Por ejemplo,
#    >>> diccionarioCaminos([[1,6,11,2],[7,12,3,8],[3,8,4,9]])
#    defaultdict(<class 'list'>,
#                {(1, 1): [[1]],
#                 (1, 2): [[6, 1]],
#                 (1, 3): [[11, 6, 1]],
#                 (1, 4): [[2, 11, 6, 1]],
#                 (2, 1): [[7, 1]],
#                 (2, 2): [[12, 6, 1], [12, 7, 1]],
#                 (2, 3): [[3, 11, 6, 1], [3, 12, 6, 1], [3, 12, 7, 1]],
#                 (2, 4): [[8, 2, 11, 6, 1], [8, 3, 11, 6, 1],
#                          [8, 3, 12, 6, 1], [8, 3, 12, 7, 1]],
#                 (3, 1): [[3, 7, 1]],
#                 (3, 2): [[8, 12, 6, 1], [8, 12, 7, 1], [8, 3, 7, 1]],
#                 (3, 3): [[4, 3, 11, 6, 1], [4, 3, 12, 6, 1],
#                          [4, 3, 12, 7, 1], [4, 8, 12, 6, 1],
#                          [4, 8, 12, 7, 1], [4, 8, 3, 7, 1]],
#                 (3, 4): [[9, 8, 2, 11, 6, 1], [9, 8, 3, 11, 6, 1],
#                          [9, 8, 3, 12, 6, 1], [9, 8, 3, 12, 7, 1],
#                          [9, 4, 3, 11, 6, 1], [9, 4, 3, 12, 6, 1],
#                          [9, 4, 3, 12, 7, 1], [9, 4, 8, 12, 6, 1],
#                          [9, 4, 8, 12, 7, 1], [9, 4, 8, 3, 7, 1]]})
def diccionarioCaminos(p: list[list[int]]) -> dict[tuple[int, int], list[list[int]]]:
    m = len(p)
    n = len(p[0])
    q = defaultdict(list)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 1:
                q[(i, j)] = [[p[0][z-1] for z in range(j, 0, -1)]]
            elif j == 1:
                q[(i, j)] = [[p[z-1][0] for z in range(i, 0, -1)]]
            else:
                q[(i, j)] = [[p[i-1][j-1]] + cs for cs in q[(i-1, j)] + q[(i, j-1)]]
    return q

# 3ª definicion de maximaSuma (por recursión)
# ===========================================

def maximaSuma3(m: list[list[int]]) -> int:
    nf = len(m)
    nc = len(m[0])
    return maximaSuma3Aux(m, (nf,nc))

# (maximaSuma3Aux m p) calcula la suma máxima de un camino hasta la
# posición p. Por ejemplo,
#    λ> maximaSuma3Aux (fromLists [[1,6,11,2],[7,12,3,8],[3,8,4,9]]) (3,4)
#    41
#    λ> maximaSuma3Aux (fromLists [[1,6,11,2],[7,12,3,8],[3,8,4,9]]) (3,3)
#    32
#    λ> maximaSuma3Aux (fromLists [[1,6,11,2],[7,12,3,8],[3,8,4,9]]) (2,4)
#    31
def maximaSuma3Aux(m: list[list[int]], p: tuple[int, int]) -> int:
    (i, j) = p
    if (i, j) == (1, 1):
        return m[0][0]
    if i == 1:
        return maximaSuma3Aux(m, (1,j-1)) + m[0][j-1]
    if j == 1:
        return maximaSuma3Aux(m, (i-1,1)) + m[i-1][0]
    return max(maximaSuma3Aux(m, (i,j-1)), maximaSuma3Aux(m, (i-1,j))) + m[i-1][j-1]

# 4ª solución (mediante programación dinámica)
# ============================================

def maximaSuma4(p: list[list[int]]) -> int:
    m = len(p)
    n = len(p[0])
    return diccionarioMaxSuma(p)[(m,n)]

# diccionarioMaxSuma(p) es el diccionario cuyas claves son los
# puntos de la matriz p y sus valores son las máximas sumas de los
# caminos a dichos puntos. Por ejemplo,
#    diccionarioMaxSuma([[1,6,11,2],[7,12,3,8],[3,8,4,9]])
#    defaultdict(<class 'int'>,
#                {(1, 0): 0,
#                 (1, 1): 1,  (1, 2): 7,  (1, 3): 18, (1, 4): 20,
#                 (2, 1): 8,  (2, 2): 20, (2, 3): 23, (2, 4): 31,
#                 (3, 1): 11, (3, 2): 28, (3, 3): 32, (3, 4): 41})
def diccionarioMaxSuma(p: list[list[int]]) -> dict[tuple[int, int], int]:
    m = len(p)
    n = len(p[0])
    q: dict[tuple[int, int], int] = defaultdict(int)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 1:
                q[(i, j)] = q[(1,j-1)] + p[0][j-1]
            elif j == 1:
                q[(i, j)] = q[(i-1,1)] + p[i-1][0]
            else:
                q[(i, j)] = max(q[(i,j-1)], q[(i-1,j)]) + p[i-1][j-1]
    return q

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('maximaSuma1([list(range(12*n+1, 12*(n+1)+1)) for n in range(12)])')
#    4.95 segundos
#    >>> tiempo('maximaSuma2([list(range(12*n+1, 12*(n+1)+1)) for n in range(12)])')
#    1.49 segundos
#    >>> tiempo('maximaSuma3([list(range(12*n+1, 12*(n+1)+1)) for n in range(12)])')
#    0.85 segundos
#    >>> tiempo('maximaSuma4([list(range(12*n+1, 12*(n+1)+1)) for n in range(12)])')
#    0.00 segundos

# Verificación
# ============

def test_maximaSuma() -> None:
    assert maximaSuma1([[1,6,11,2],[7,12,3,8],[3,8,4,9]]) == 41
    assert maximaSuma2([[1,6,11,2],[7,12,3,8],[3,8,4,9]]) == 41
    assert maximaSuma3([[1,6,11,2],[7,12,3,8],[3,8,4,9]]) == 41
    assert maximaSuma4([[1,6,11,2],[7,12,3,8],[3,8,4,9]]) == 41
    print("Verificado")

# La verificación es
#    >>> test_maximaSuma()
#    Verificado
