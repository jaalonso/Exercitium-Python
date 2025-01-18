# Mastermind.py
# Mastermind.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 18-enero-2025
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El Mastermind es un juego que consiste en deducir un código
# numérico formado por una lista de números. Cada vez que se empieza
# una partida, el programa debe elegir un código, que será lo que el
# jugador debe adivinar en la menor cantidad de intentos posibles. Cada
# intento consiste en una propuesta de un código posible que propone el
# jugador, y una respuesta del programa. Las respuestas le darán pistas
# al jugador para que pueda deducir el código.
#
# Estas pistas indican lo cerca que estuvo el número propuesto de la
# solución a través de dos valores: la cantidad de aciertos es la
# cantidad de dígitos que propuso el jugador que también están en el
# código en la misma posición. La cantidad de coincidencias es la
# cantidad de dígitos que propuso el jugador que también están en el
# código pero en una posición distinta.
#
# Por ejemplo, si el código que eligió el programa es el [2,6,0,7] y
# el jugador propone el [1,4,0,6], el programa le debe responder un
# acierto (el 0, que está en el código original en el mismo lugar, el
# tercero), y una coincidencia (el 6, que también está en el código
# original, pero en la segunda posición, no en el cuarto como fue
# propuesto). Si el jugador hubiera propuesto el [3,5,9,1], habría
# obtenido como respuesta ningún acierto y ninguna coincidencia, ya que
# no hay números en común con el código original. Si se obtienen
# cuatro aciertos es porque el jugador adivinó el código y ganó el
# juego.
#
# Definir la función
#    mastermind : (list[int], list[int]) -> tuple[int, int]
# tal que mastermind(xs, ys) es el par formado por los números de
# aciertos y de coincidencias entre xs e ys. Por ejemplo,
#    mastermind([3,3], [3,2])          ==  (1,0)
#    mastermind([3,5,3], [3,2,5])      ==  (1,1)
#    mastermind([3,5,3,2], [3,2,5,3])  ==  (1,3)
#    mastermind([3,5,3,3], [3,2,5,3])  ==  (2,1)
# ---------------------------------------------------------------------

from sys import setrecursionlimit
from timeit import Timer, default_timer

from hypothesis import given
from hypothesis import strategies as st

setrecursionlimit(10**6)

# 1ª solución
# ===========

# aciertos(xs, ys) es la lista de las posiciones de los aciertos entre
# xs e ys. Por ejemplo,
#    aciertos([1,1,0,7], [1,0,1,7])  ==  [0,3]
def aciertos(xs: list[int], ys: list[int]) -> list[int]:
    return [n for n, (x, y) in enumerate(zip(xs, ys)) if x == y]

# coincidencia(xs, ys) es la lista de las posiciones de las
# coincidencias entre xs e ys. Por ejemplo,
#    coincidencias([1,1,0,7], [1,0,1,7])  ==  [1,2]
def coincidencias(xs: list[int], ys: list[int]) -> list[int]:
    return [n for n, y in enumerate(ys)
            if y in xs and n not in aciertos(xs, ys)]

def mastermind1(xs: list[int], ys: list[int]) -> tuple[int, int]:
    return (len(aciertos(xs, ys)), len(coincidencias(xs, ys)))

# 2ª solución
# ===========

def mastermind2(xs: list[int], ys: list[int]) -> tuple[int, int]:
    aciertos2 = [n for n, (x, y) in enumerate(zip(xs, ys)) if x == y]
    coincidencias2 = [n for n, y in enumerate(ys)
                      if y in xs and n not in aciertos(xs, ys)]
    return (len(aciertos2), len(coincidencias2))

# 3ª solución
# ===========

def mastermind3(xs: list[int], ys: list[int]) -> tuple[int, int]:
    def aux(us: list[int], vs: list[int]) -> tuple[int, int]:
        if us and vs:
            u, *us_tail = us
            v, *vs_tail = vs
            a, b = aux(us_tail, vs_tail)
            if u == v:
                return (a + 1, b)
            if v in xs:
                return (a, b + 1)
            return (a, b)
        return (0, 0)
    return aux(xs, ys)

# 4ª solución
# ===========

def mastermind4(xs: list[int], ys: list[int]) -> tuple[int, int]:
    aciertos4 = [n for n, (x, y) in enumerate(zip(xs, ys)) if x == y]
    coincidencias4 = [n for n, y in enumerate(ys)
                      if y in set(xs) and n not in aciertos4]
    return (len(aciertos4), len(coincidencias4))

# mastermind4 :: [Int] -> [Int] -> (Int, Int)
# mastermind4 xs ys =
#   (length aciertos4, length coincidencias4)
#   where
#     aciertos4, coincidencias4 :: [Int]
#     aciertos4      = [n | (n,x,y) <- zip3 [0..] xs ys, x == y]
#     xs'            = S.fromList xs
#     coincidencias4 = [n | (n,y) <- zip [0..] ys, y `S.member` xs', n `notElem` aciertos4]

# Verificación
# ============

def test_mastermind() -> None:
    for mastermind in [mastermind1, mastermind2, mastermind3,
                       mastermind4]:
        assert mastermind([3,3], [3,2])          ==  (1,0)
        assert mastermind([3,5,3], [3,2,5])      ==  (1,1)
        assert mastermind([3,5,3,2], [3,2,5,3])  ==  (1,3)
        assert mastermind([3,5,3,3], [3,2,5,3])  ==  (2,1)
        print(f"Verificado {mastermind.__name__}")

# La verificación es
#    >>> test_mastermind()
#    Verificado

# Equivalencia de las definiciones
# ================================

# La propiedad es
@given(st.lists(st.integers()), st.lists(st.integers()))
def test_mastermind_equiv(xs: list[int], ys: list[int]) -> None:
    n = min(len(xs), len(ys))
    xs1 = xs[:n]
    ys1 = ys[:n]
    r = mastermind1(xs1, ys1)
    assert mastermind2(xs1, ys1) == r
    assert mastermind3(xs1, ys1) == r
    assert mastermind4(xs1, ys1) == r

# La comprobación es
#    >>> test_minimales_equiv()
#    >>>

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('mastermind3(list(range(1,10**4+1)), list(range(2,20001,2)))')
#    1.31 segundos
#    >>> tiempo('mastermind4(list(range(1,10**4+1)), list(range(2,20001,2)))')
#    1.17 segundos
#    >>> tiempo('mastermind1(list(range(1,10**4+1)), list(range(2,20001,2)))')
#    3.45 segundos
#    >>> tiempo('mastermind2(list(range(1,10**4+1)), list(range(2,20001,2)))')
#    3.52 segundos
#    >>> tiempo('mastermind3(list(range(1,10**4+1)), list(range(2,20001,2)))')
#    1.32 segundos
#    >>> tiempo('mastermind4(list(range(1,10**4+1)), list(range(2,20001,2)))')
#    1.19 segundos
