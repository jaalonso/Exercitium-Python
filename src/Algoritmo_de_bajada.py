# Algoritmo_de_bajada.py
# Algoritmo de bajada para resolver un sistema triangular inferior.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 4-diciembre-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Un sistema de ecuaciones lineales Ax = b es triangular inferior si
# todos los elementos de la matriz A que están por encima de la
# diagonal principal son nulos; es decir, es de la forma
#    a(1,1)*x(1)                                               = b(1)
#    a(2,1)*x(1) + a(2,2)*x(2)                                 = b(2)
#    a(3,1)*x(1) + a(3,2)*x(2) + a(3,3)*x(3)                   = b(3)
#    ...
#    a(n,1)*x(1) + a(n,2)*x(2) + a(n,3)*x(3) +...+ a(x,x)*x(n) = b(n)
#
# El sistema es compatible si, y sólo si, el producto de los elementos
# de la diagonal principal es distinto de cero. En este caso, la
# solución se puede calcular mediante el algoritmo de bajada:
#    x(1) = b(1) / a(1,1)
#    x(2) = (b(2) - a(2,1)*x(1)) / a(2,2)
#    x(3) = (b(3) - a(3,1)*x(1) - a(3,2)*x(2)) / a(3,3)
#    ...
#    x(n) = (b(n) - a(n,1)*x(1) - a(n,2)*x(2) -...- a(n,n-1)*x(n-1)) / a(n,n)
#
# Definir la función
#    bajada : (list[list[float]], list[list[float]]) -> list[list[float]]
# tal que bajada(a, b) es la solución, mediante el algoritmo de bajada,
# del sistema compatible triangular superior ax = b. Por ejemplo,
#    >>> bajada([[2,0,0],[3,1,0],[4,2,5.0]], [[3],[6.5],[10]])
#    [[1.5], [2.0], [0.0]]
# Es decir, la solución del sistema
#    2x            = 3
#    3x + y        = 6.5
#    4x + 2y + 5 z = 10
# es x=1.5, y=2 y z=0.
# ---------------------------------------------------------------------

def bajada(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    n = len(a)
    def x(k: int) -> float:
        return (b[k][0] - sum((a[k][j] * x(j) for j in range(0, k)))) / a[k][k]
    return [[x(i)] for i in range(0, n)]

# Verificación
# ============

def test_bajada() -> None:
    assert bajada([[2,0,0],[3,1,0],[4,2,5.0]], [[3],[6.5],[10]]) == \
        [[1.5], [2.0], [0.0]]
    print("Verificado")

# La verificación es
#    >>> test_bajada()
#    Verificado
