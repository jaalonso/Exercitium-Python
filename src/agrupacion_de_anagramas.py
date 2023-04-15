# Agrupacion_de_anagramas.py
# Agrupación de anagramas
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 09-agosto-2022
# ======================================================================

# ----------------------------------------------------------------------
# Una palabra es [anagrama](https://bit.ly/3cRLDNw) de otra si se puede
# obtener permutando sus letras. Por ejemplo, "mora" y "roma" son
# anagramas de "amor".
#
# Definir la función
#    anagramas : list[str]) -> list[list[str]]
# tal que anagramas(cs) es la lista de las listas de anagramas de cs. Por
# ejemplo,
#    >>> anagramas(['mora', 'pirata', 'roma', 'ana', 'patria', 'ramo'])
#    [['mora', 'roma', 'ramo'], ['pirata', 'patria'], ['ana']]
# ----------------------------------------------------------------------

# ordenada(c) es la cadena obtenida ordenando los caracteres de la cadena
# cs. Por ejemplo,
#    >>> ordenada('sevilla')
#    'aeillsv'
def ordenada(c: str) -> str:
    return "".join(sorted(c))

def anagramas(cs: list[str]) -> list[list[str]]:
    d: dict[str, list[str]] = {}
    for c in cs:
        co = ordenada(c)
        if co in d:
            d[co].append(c)
        else:
            d[co] = [c]
    return list(d.values())

# Referencias
# ===========

# + FavTutor, [Group anagrams (with Java, C++ and Python
#   solution)](https://bit.ly/3SckPYo).
# + GeeksForGeeks, [Given a sequence of words, print all anagrams
#   together (Set 1)](https://bit.ly/3oMEwIB).
# + GeeksForGeeks, [Print anagrams together](https://bit.ly/3JeQC6Y).
# + LeetCode, [Group anagrams](https://bit.ly/3JjkMWt).
