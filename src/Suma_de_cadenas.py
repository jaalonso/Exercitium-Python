# Suma_de_cadenas.py
# Suma de cadenas.
# José A. Alonso Jiménez
# Sevilla, 14-febrero-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    sumaCadenas :: String -> String -> String
# tal que (sumaCadenas xs ys) es la cadena formada por el número entero
# que es la suma de los números enteros cuyas cadenas que lo
# representan son xs e ys; además, se supone que la cadena vacía
# representa al cero. Por ejemplo,
#    sumaCadenas("2",   "6")  == "8"
#    sumaCadenas("14",  "2")  == "16"
#    sumaCadenas("14",  "-5") == "9"
#    sumaCadenas("-14", "-5") == "-19"
#    sumaCadenas("5",   "-5") == "0"
#    sumaCadenas("",    "5")  == "5"
#    sumaCadenas("6",   "")   == "6"
#    sumaCadenas("",    "")   == "0"
# ---------------------------------------------------------------------

from functools import reduce

# 1ª solución
# ===========

def sumaCadenas1(xs: str, ys: str) -> str:
    return str(sum(map(int, filter(lambda x: x != '', [xs, ys]))))

# 2ª solución
# ===========

def sumaCadenas2(xs: str, ys: str) -> str:
    if xs == "" and ys == "":
        return "0"
    if xs == "":
        return ys
    if ys == "":
        return xs
    return str(int(xs) + int(ys))

# 3ª solución
# ===========

# numero(xs) es el número entero representado por la cadena xs
# suponiendo que la cadena vacía representa al cero.. Por ejemplo,
#    numero "12"   ==  12
#    numero "-12"  ==  -12
#    numero "0"    ==  0
#    numero ""     ==  0
def numero(s: str) -> int:
    if not s:
        return 0
    return int(s)

def sumaCadenas3(xs: str, ys: str) -> str:
    return str(numero(xs) + numero(ys))

# 4ª solución
# ===========

def sumaCadenas4(xs: str, ys: str) -> str:
    x = int(xs or "0")
    y = int(ys or "0")
    return str(x + y)

# Verificación
# ============

def test_sumaCadenas() -> None:
    for sumaCadenas in [sumaCadenas1, sumaCadenas2, sumaCadenas3,
                        sumaCadenas4]:
        assert sumaCadenas("2",   "6")  == "8"
        assert sumaCadenas("14",  "2")  == "16"
        assert sumaCadenas("14",  "-5") == "9"
        assert sumaCadenas("-14", "-5") == "-19"
        assert sumaCadenas("5",   "-5") == "0"
        assert sumaCadenas("",    "5")  == "5"
        assert sumaCadenas("6",   "")   == "6"
        assert sumaCadenas("",    "")   == "0"
    print("Verificado")

# La verificación es
#    >>> test_sumaCadenas()
#    Verificado
