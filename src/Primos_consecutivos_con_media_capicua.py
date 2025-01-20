# Primos_consecutivos_con_media_capicua.py
# Primos consecutivos con media capicúa.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 19-enero-2025
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la lista
#    primosConsecutivosConMediaCapicua :: [(Int,Int,Int)]
# formada por las ternas (x,y,z) tales que x e y son primos
# consecutivos cuya media, z, es capicúa. Por ejemplo,
#    >>> list(islice(primosConsecutivosConMediaCapicua1(), 5))
#    [(3, 5, 4), (5, 7, 6), (7, 11, 9), (97, 101, 99), (109, 113, 111)]
#    λ> primosConsecutivosConMediaCapicua !! 500
#    (5687863,5687867,5687865)
# ---------------------------------------------------------------------

from itertools import count, islice
from timeit import Timer, default_timer
from typing import Iterator

from sympy import isprime

# 1ª solución
# ===========

# primo(x) se verifica si x es primo. Por ejemplo,
#    primo(7)  ==  True
#    primo(8)  ==  False
def primo(x: int) -> bool:
    return [y for y in range(1, x + 1) if x % y == 0] == [1, x]

# primosImpares() genera la lista de los números primos impares. Por
# ejemplo,
#    >>> list(islice(primosImpares(), 10))
#    [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
def primosImpares() -> Iterator[int]:
    return (x for x in count(3, 2) if primo(x))

# capicua(x) se verifica si x es capicúa. Por ejemplo,
#    capicua(232) == True
#    capicua(223) == False
def capicua(x: int) -> bool:
    ys = str(x)
    return ys == ys[::-1]

def primosConsecutivosConMediaCapicua1() -> Iterator[tuple[int, int, int]]:
    return (
        (x, y, z)
        for x, y in zip(primosImpares(), islice(primosImpares(), 1, None))
        if (z := (x + y) // 2) and capicua(z)
    )

# 2ª solución
# ===========

# Generador de números primos usando la criba de Eratóstenes.
def primos2() -> Iterator[int]:
    no_primos = {}
    for n in count(2):
        if n not in no_primos:
            yield n
            no_primos[n * n] = [n]
        else:
            for p in no_primos[n]:
                no_primos.setdefault(p + n, []).append(p)
            del no_primos[n]

def primosImpares2() -> Iterator[int]:
    return islice(primos2(), 1, None)

def primosConsecutivosConMediaCapicua2() -> Iterator[tuple[int, int, int]]:
    return (
        (x, y, z)
        for x, y in zip(primosImpares2(), islice(primosImpares2(), 1, None))
        if (z := (x + y) // 2) and capicua(z)
    )

# 3ª solución
# ===========

def primosImpares3() -> Iterator[int]:
    return (n for n in count(3, 2) if isprime(n))

def primosConsecutivosConMediaCapicua3() -> Iterator[tuple[int, int, int]]:
    return (
        (x, y, z)
        for x, y in zip(primosImpares3(), islice(primosImpares3(), 1, None))
        if (z := (x + y) // 2) and capicua(z)
    )

# Verificación
# ============

def test_primosConsecutivosConMediaCapicua() -> None:
    for primosConsecutivosConMediaCapicua \
        in[primosConsecutivosConMediaCapicua1,
           primosConsecutivosConMediaCapicua2,
           primosConsecutivosConMediaCapicua3]:
        assert list(islice(primosConsecutivosConMediaCapicua(), 5)) == \
            [(3, 5, 4), (5, 7, 6), (7, 11, 9), (97, 101, 99), (109, 113, 111)]
        print(f"Verificado {primosConsecutivosConMediaCapicua.__name__}")

# La verificación es
#    >>> test_primosConsecutivosConMediaCapicua()
#    Verificado primosConsecutivosConMediaCapicua1
#    Verificado primosConsecutivosConMediaCapicua2
#    Verificado primosConsecutivosConMediaCapicua3

# Equivalencia de definiciones
# ============================

# nth(i, n) es el n-ésimo elemento del iterador i. Por ejemplo,
#    nth(primos2(), 4) == 11
def nth(i: Iterator[int], n: int) -> int:
    return list(islice(i, n, n+1))[0]

# La propiedad es
def test_primosConsecutivosConMediaCapicua_equiv() -> None:
    assert list(islice(primosConsecutivosConMediaCapicua1(), 30)) == \
        list(islice(primosConsecutivosConMediaCapicua2(), 30))
    assert list(islice(primosConsecutivosConMediaCapicua2(), 100)) == \
        list(islice(primosConsecutivosConMediaCapicua3(), 100))
    print("Verificado")

# La comprobación es
#    >>> test_primosConsecutivosConMediaCapicua_equiv()
#    Verificado

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('nth(primosConsecutivosConMediaCapicua1(), 30)')
#    4.17 segundos
#    >>> tiempo('nth(primosConsecutivosConMediaCapicua2(), 30)')
#    0.02 segundos
#    >>> tiempo('nth(primosConsecutivosConMediaCapicua3(), 30)')
#    0.04 segundos
#
#    >>> tiempo('nth(primosConsecutivosConMediaCapicua2(), 200)')
#    1.54 segundos
#    >>> tiempo('nth(primosConsecutivosConMediaCapicua3(), 200)')
#    3.33 segundos
