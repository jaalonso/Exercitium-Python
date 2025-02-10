# Anagramas.py
# Anagramas.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 7-febrero-2025
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Una palabra es una anagrama de otra si se puede obtener permutando
# sus letras. Por ejemplo, "mora" y "roma" son anagramas de "amor".
#
# Definir la función
#    anagramas : (str, list[str]) -> list[str]
# tal que anagramas(x, ys) es la lista de los elementos de ys que son
# anagramas de x. Por ejemplo,
#    >>> anagramas("amor", ["Roma","mola","loma","moRa", "rama"])
#    ['Roma', 'moRa']
#    >>> anagramas("rama", ["aMar","amaRa","roMa","marr","aRma"])
#    ['aMar', 'aRma']
# ---------------------------------------------------------------------

from collections import Counter
from itertools import cycle, islice, permutations
from timeit import Timer, default_timer

# 1ª solución
# ===========

def anagramas1(x: str, ys: list[str]) -> list[str]:
    return [y for y in ys if son_anagramas(x, y)]

# (son_anagramas(xs, ys)) se verifica si xs e ys son anagramas. Por
# ejemplo,
#    son_anagramas("amor", "Roma")  ==  True
#    son_anagramas("amor", "mola")  ==  False
def son_anagramas(xs: str, ys: str) -> bool:
    return sorted(xs.lower()) == sorted(ys.lower())

# 2ª solución
# =============

def anagramas2(x: str, ys: list[str]) -> list[str]:
    return list(filter(lambda y: son_anagramas(x, y), ys))

# 3ª solución
# ===========

def anagramas3(x: str, ys: list[str]) -> list[str]:
    counter_x = Counter(x.lower())
    return list(filter(lambda y: counter_x == Counter(y.lower()), ys))

# 4ª solución
# ===========

def anagramas4(x: str, ys: list[str]) -> list[str]:
    return [y for y in ys if frecuencias(x.lower()) == frecuencias(y.lower())]

def frecuencias(s: str) -> dict[str, int]:
    dic : dict[str, int] = {}
    for c in s:
        dic[c] = dic.get(c, 0) + 1
    return dic

# Verificación
# ============

def test_anagramas() -> None:
    for anagramas in [anagramas1, anagramas2, anagramas3, anagramas4]:
        assert anagramas("amor", ["Roma","mola","loma","moRa", "rama"]) == \
            ['Roma', 'moRa']
        assert anagramas("rama", ["aMar","amaRa","roMa","marr","aRma"]) ==\
            ['aMar', 'aRma']
        print(f"Verificado {anagramas.__name__}")

# La verificación es
#    >>> test_anagramas()
#    Verificado anagramas1
#    Verificado anagramas2
#    Verificado anagramas3
#    Verificado anagramas4

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# ejemplo(n) es la lista de la n primeras permutaciones de
# "1234567890". Por ejemplo,
#    >>> ejemplo(3)
#    ['1234567890', '1234567809', '1234567980']
def ejemplo(n: int) -> list[str]:
    return [''.join(p) for p in islice(permutations("1234567890"), n)]

# La comparación es
#    >>> ej = ejemplo(10**6)
#    >>> tiempo('len(anagramas1("1234567890", ej))')
#    0.85 segundos
#    >>> tiempo('len(anagramas2("1234567890", ej))')
#    0.88 segundos
#    >>> tiempo('len(anagramas3("1234567890", ej))')
#    3.97 segundos
#    >>> tiempo('len(anagramas4("1234567890", ej))')
#    2.38 segundos

# cadena(n) es la cadena de los 10 primeros caracteres de la cadena
# infinita abcabcabc... Por ejemplo,
#    >>> cadena(10)
#    'abcabcabca'
def cadena(n: int) -> str:
    return ''.join(islice(cycle("abc"), n))

# (cadenas m n) es la lista otenida repitiendo m veces (adena n). Por
# ejemplo,
#    >>> cadenas(3, 10)
#    ['abcabcabca', 'abcabcabca', 'abcabcabca']
def cadenas(m: int, n: int) -> list[str]:
    return [cadena(n) for _ in range(m)]

# La comparación es
#    >>> tiempo('len(anagramas1(cadena(10**5), cadenas(100, 10**5)))')
#    0.99 segundos
#    >>> tiempo('len(anagramas2(cadena(10**5), cadenas(100, 10**5)))')
#    1.00 segundos
#    >>> tiempo('len(anagramas3(cadena(10**5), cadenas(100, 10**5)))')
#    0.57 segundos
#    >>> tiempo('len(anagramas4(cadena(10**5), cadenas(100, 10**5)))')
#    2.01 segundos
