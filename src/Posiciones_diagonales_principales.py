# Posiciones_diagonales_principales.py
# Posiciones de las diagonales principales
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 4-mayo-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Las posiciones de una matriz con 3 filas y 4 columnas son
#    (1,1) (1,2) (1,3) (1,4)
#    (2,1) (2,2) (2,3) (2,4)
#    (3,1) (3,2) (3,3) (3,4)
# La posiciones de sus 6 diagonales principales son
#   [(3,1)]
#   [(2,1),(3,2)]
#   [(1,1),(2,2),(3,3)]
#   [(1,2),(2,3),(3,4)]
#   [(1,3),(2,4)]
#   [(1,4)]
#
# Definir la función
#    posicionesDiagonalesPrincipales : (int, int) -> list[list[tuple[int, int]]]
# tal que posicionesdiagonalesprincipales(m, n) es la lista de las
# posiciones de las diagonales principales de una matriz con m filas y
# n columnas. Por ejemplo,
#    >>> posicionesDiagonalesPrincipales1(3, 4)
#    [[(3, 1)],
#     [(2, 1), (3, 2)],
#     [(1, 1), (2, 2), (3, 3)],
#     [(1, 2), (2, 3), (3, 4)],
#     [(1, 3), (2, 4)],
#     [(1, 4)]]
#    >>> posicionesDiagonalesPrincipales1(4, 4)
#    [[(4, 1)],
#     [(3, 1), (4, 2)],
#     [(2, 1), (3, 2), (4, 3)],
#     [(1, 1), (2, 2), (3, 3), (4, 4)],
#     [(1, 2), (2, 3), (3, 4)],
#     [(1, 3), (2, 4)],
#     [(1, 4)]]
#    >>> posicionesDiagonalesPrincipales1(4, 3)
#    [[(4, 1)],
#     [(3, 1), (4, 2)],
#     [(2, 1), (3, 2), (4, 3)],
#     [(1, 1), (2, 2), (3, 3)],
#     [(1, 2), (2, 3)],
#     [(1, 3)]]
# ---------------------------------------------------------------------

from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

# 1ª solución
# ===========

def posicionesDiagonalesPrincipales1(m: int, n: int) -> list[list[tuple[int, int]]]:
    def iniciales() -> list[tuple[int, int]]:
        return [(i,1) for i in range(m,1,-1)] + [(1,j) for j in range(1, n+1)]
    def extension(p: tuple[int, int]) -> list[tuple[int, int]]:
        (i,j) = p
        return [(i+k,j+k) for k in range(0, 1+min(m-i, n-j))]
    return [extension(ij) for ij in iniciales()]

# 2ª solución
# ===========

def posicionesDiagonalesPrincipales2(m: int, n: int) -> list[list[tuple[int, int]]]:
    return [list(zip(range(i,m+1), range(1,n+1))) for i in range(m,0,-1)] + \
           [list(zip(range(1,m+1), range(j,n+1))) for j in range(2,n+1)]

# Verificación
# ============

def test_posicionesDiagonalesPrincipales() -> None:
    for posicionesDiagonalesPrincipales in [posicionesDiagonalesPrincipales1,
                                            posicionesDiagonalesPrincipales2]:
        assert posicionesDiagonalesPrincipales(3, 4) == \
            [[(3,1)],
             [(2,1),(3,2)],
             [(1,1),(2,2),(3,3)],
             [(1,2),(2,3),(3,4)],
             [(1,3),(2,4)],
             [(1,4)]]
        assert posicionesDiagonalesPrincipales(4, 4) == \
            [[(4,1)],
             [(3,1),(4,2)],
             [(2,1),(3,2),(4,3)],
             [(1,1),(2,2),(3,3),(4,4)],
             [(1,2),(2,3),(3,4)],
             [(1,3),(2,4)],
             [(1,4)]]
        assert posicionesDiagonalesPrincipales(4, 3) == \
            [[(4,1)],
             [(3,1),(4,2)],
             [(2,1),(3,2),(4,3)],
             [(1,1),(2,2),(3,3)],
             [(1,2),(2,3)],
             [(1,3)]]
    print("Verificado")

# La verificación es
#    >>> test_posicionesDiagonalesPrincipales()
#    Verificado

# Equivalencia de las definiciones
# ================================

# La propiedad es
@given(st.integers(min_value=1, max_value=100),
       st.integers(min_value=1, max_value=100))
def test_posicionesDiagonalesPrincipales_equiv(m: int, n: int) -> None:
    assert posicionesDiagonalesPrincipales1(m, n) == \
           posicionesDiagonalesPrincipales2(m, n)

# La comprobación es
#    >>> test_posicionesDiagonalesPrincipales_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('posicionesDiagonalesPrincipales1(10**4, 2*10**3)')
#    3.32 segundos
#    >>> tiempo('posicionesDiagonalesPrincipales2(10**4, 2*10**3)')
#    2.16 segundos
