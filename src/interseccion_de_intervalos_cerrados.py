# interseccion_de_intervalos_cerrados.py
# Intersección de intervalos cerrados.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 14-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Los intervalos cerrados se pueden representar mediante una lista de
# dos números (el primero es el extremo inferior del intervalo y el
# segundo el superior).
#
# Definir la función
#    interseccion : (list[float], list[float]) -> list[float]
# tal que interseccion(i1, i2) es la intersección de los intervalos i1 e
# i2. Por ejemplo,
#    interseccion([],     [3, 5]   ==  []
#    interseccion([3, 5], [])      ==  []
#    interseccion([2, 4], [6, 9])  ==  []
#    interseccion([2, 6], [6, 9])  ==  [6, 6]
#    interseccion([2, 6], [0, 9])  ==  [2, 6]
#    interseccion([2, 6], [0, 4])  ==  [2, 4]
#    interseccion([4, 6], [0, 4])  ==  [4, 4]
#    interseccion([5, 6], [0, 4])  ==  []
#
# Comprobar con Hypothesis que la intersección de intervalos es
# conmutativa.
# ---------------------------------------------------------------------

from hypothesis import assume, given
from hypothesis import strategies as st

Rectangulo = list[float]

def interseccion(i1: Rectangulo,
                 i2: Rectangulo) -> Rectangulo:
    if i1 and i2:
        [a1, b1] = i1
        [a2, b2] = i2
        a = max(a1, a2)
        b = min(b1, b2)
        if a <= b:
            return [a, b]
        return []
    return []

# La propiedad es
@given(st.floats(), st.floats(), st.floats(), st.floats())
def test_prop_raices(a1: float, b1: float, a2: float, b2: float) -> None:
    assume(a1 <= b1 and a2 <= b2)
    assert interseccion([a1, b1], [a2, b2]) == interseccion([a2, b2], [a1, b1])

# La comprobación es
#    src> poetry run pytest -q interseccion_de_intervalos_cerrados.py
#    1 passed in 0.64s
