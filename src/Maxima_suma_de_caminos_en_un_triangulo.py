# Maxima_suma_de_caminos_en_un_triangulo.py
# Máxima suma de caminos en un triángulo.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 16-abril-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Los triángulos se pueden representar mediante listas de listas. Por
# ejemplo, el triángulo
#       3
#      7 4
#     2 4 6
#    8 5 9 3
# se representa por
#    [[3],[7,4],[2,4,6],[8,5,9,3]]
#
# Definir la función
#    maximaSuma : (list[list[int]]) -> int
# tal que maximaSuma(xss) es el máximo de las sumas de los elementos
# de los caminos en el triángulo xss donde los caminos comienzan en el
# elemento de la primera fila, en cada paso se mueve a uno de  sus dos
# elementos adyacentes en la fila siguiente y terminan en la última
# fila. Por ejemplo,
#    maximaSuma([[3],[7,4]])                    ==  10
#    maximaSuma([[3],[7,4],[2,4,6]])            ==  14
#    maximaSuma([[3],[7,4],[2,4,6],[8,5,9,3]])  ==  23
# ---------------------------------------------------------------------

from timeit import Timer, default_timer

# 1ª solución
# ===========

def caminos(xss: list[list[int]]) -> list[list[int]]:
    if not xss:
        return [[]]
    if len(xss) == 1:
        return xss
    x = xss[0][0]
    y1 = xss[1][0]
    y2 = xss[1][1]
    zss = xss[2:]
    return [[x, y1] + us for _, *us in caminos([[y1]] + [zs[:-1] for zs in zss])] + \
           [[x, y2] + us for _, *us in caminos([[y2]] + [zs[1:] for zs in zss])]

# maximaSuma1 :: [[Integer]] -> Integer
def maximaSuma1(xss: list[list[int]]) -> int:
    return max((sum(ys) for ys in caminos(xss)))

# 2ª solución
# ===========

def maximaSuma2(xss: list[list[int]]) -> int:
    if not xss:
        return 0
    if len(xss) == 1:
        return xss[0][0]
    x = xss[0][0]
    y1 = xss[1][0]
    y2 = xss[1][1]
    zss = xss[2:]
    return x + max(maximaSuma2([[y1]] + [us[:-1] for us in zss]),
                   maximaSuma2([[y2]] + [us[1:] for us in zss]))

# Verificación
# ============

def test_maximaSuma() -> None:
    for maximaSuma in [maximaSuma1, maximaSuma2]:
        assert maximaSuma([[3],[7,4]]) == 10
        assert maximaSuma([[3],[7,4],[2,4,6]]) == 14
        assert maximaSuma([[3],[7,4],[2,4,6],[8,5,9,3]]) == 23
    print("Verificado")

# La verificación es
#    >>> test_maximaSuma()
#    Verificado

# Comparación de eficiencia
# =========================

# Para la comparaciones se usará la siguiente función que construye un
# triángulo de la altura dada. Por ejemplo,
#    >>> triangulo(2)
#    [[0], [1, 2]]
#    >>> triangulo(3)
#    [[0], [1, 2], [2, 3, 4]]
#    >>> triangulo(4)
#    [[0], [1, 2], [2, 3, 4], [3, 4, 5, 6]]
def triangulo(n: int) -> list[list[int]]:
    return [list(range(k, k+k+1)) for k in range(n)]

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('maximaSuma1(triangulo(20))')
#    3.21 segundos
#    >>> tiempo('maximaSuma2(triangulo(20))')
#    0.59 segundos
