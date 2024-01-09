# La_serie_de_Thue_Morse.py
# La serie de Thue-Morse.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 9-enero-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# La [serie de Thue-Morse](http://bit.ly/1KvZONW) comienza con el
# término [0] y sus siguientes términos se construyen añadiéndole al
# anterior su complementario (es decir, la lista obtenida cambiando el
# 0 por 1 y el 1 por 0). Los primeros términos de la serie son
#    [0]
#    [0,1]
#    [0,1,1,0]
#    [0,1,1,0,1,0,0,1]
#    [0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0]
#
# Definir la función
#    serieThueMorse : () -> Iterator[list[list[int]]]
# tal que sus elementos son los términos de la serie de Thue-Morse. Por
# ejemplo,
#    >>> list(islice(serieThueMorse(), 4))
#    [[0], [0, 1], [0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1]]
# ---------------------------------------------------------------------

from itertools import count, islice
from typing import Iterator

# Solución
# ========

# complementaria(xs) es la complementaria de la lista xs (formada por
# ceros y unos); es decir, la lista obtenida cambiando el 0 por 1 y el
# 1 por 0. Por ejemplo,
#    complementaria([1,0,0,1,1,0,1])  ==  [0,1,1,0,0,1,0]
def complementaria(xs: list[int]) -> list[int]:
    return [1 - x for x in xs]

# termSerieThueMorse(n) es el término n-ésimo de la serie de
# Thue-Morse. Por ejemplo,
#    termSerieThueMorse(1)  ==  [0,1]
#    termSerieThueMorse(2)  ==  [0,1,1,0]
#    termSerieThueMorse(3)  ==  [0,1,1,0,1,0,0,1]
#    termSerieThueMorse(4)  ==  [0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0]
def termSerieThueMorse(n: int) -> list[int]:
    if n == 0:
        return [0]
    xs = termSerieThueMorse(n-1)
    return xs + complementaria(xs)

def serieThueMorse() -> Iterator[list[int]]:
    return (termSerieThueMorse(n) for n in count())

# Verificación
# ============

def test_serieThueMorse() -> None:
    assert list(islice(serieThueMorse(), 4)) == \
        [[0], [0, 1], [0, 1, 1, 0], [0, 1, 1, 0, 1, 0, 0, 1]]
    print("Verificado")

# La verificación es
#    >>> test_serieThueMorse()
#    Verificado

# ---------------------------------------------------------------------
# § Referencias                                                      --
# ---------------------------------------------------------------------

# + N.J.A. Sloane "Sucesión A010060" en OEIS http://oeis.org/A010060
# + Programming Praxis "Thue-Morse sequence" http://bit.ly/1n2PdFk
# + Wikipedia "Thue–Morse sequence" http://bit.ly/1KvZONW
