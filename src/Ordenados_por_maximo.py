# Ordenados_por_maximo.py
# Ordenación por el máximo.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-enero-2025
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    ordenadosPorMaximo : (list[list[int]]) -> list[list[int]]
# tal que ordenadosPorMaximo(xss) es la lista de los elementos de xss
# ordenada por sus máximos (se supone que los elementos de xss son
# listas no vacía) y cuando tiene el mismo máximo se conserva el orden
# original. Por ejemplo,
#    >>> ordenadosPorMaximo([[0,8],[9],[8,1],[6,3],[8,2],[6,1],[6,2]])
#    [[6, 3], [6, 1], [6, 2], [0, 8], [8, 1], [8, 2], [9]]
# ---------------------------------------------------------------------

from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

# 1ª solución
# ===========

def ordenadosPorMaximo1(xss: list[list[int]]) -> list[list[int]]:
    return [xs for _, _, xs in sorted(((max(xs), k, xs) for k, xs in enumerate(xss)))]

# 2ª solución
# ===========

def ordenadosPorMaximo2(xss: list[list[int]]) -> list[list[int]]:
    return sorted(xss, key=max)

# Verificación
# ============

def test_ordenadosPorMaximo() -> None:
    for ordenadosPorMaximo in [ordenadosPorMaximo1, ordenadosPorMaximo2]:
        assert ordenadosPorMaximo([[0,8],[9],[8,1],[6,3],[8,2],[6,1],[6,2]]) ==\
            [[6,3],[6,1],[6,2],[0,8],[8,1],[8,2],[9]]
        print(f"Verificado {ordenadosPorMaximo.__name__}")

# La verificación es
#    >>> test_ordenadosPorMaximo()
#    Verificado ordenadosPorMaximo1
#    Verificado ordenadosPorMaximo2

# Equivalencia de las definiciones
# ================================

# La propiedad es
@given(st.lists(st.lists(st.integers(), min_size=1)))
def test_ordenadosPorMaximo_equiv(xss: list[list[int]]) -> None:
    assert ordenadosPorMaximo1(xss) == ordenadosPorMaximo2(xss)

# La comprobación es
#    >>> test_ordenadosPorMaximo_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('ordenadosPorMaximo1([[i for i in range(k)] for k in range(1, 10**4)])')
#    2.87 segundos
#    >>> tiempo('ordenadosPorMaximo2([[i for i in range(k)] for k in range(1, 10**4)])')
#    2.86 segundos
