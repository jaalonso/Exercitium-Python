# Numeros_amigos.py
# Números amigos
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 14-abril-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Dos [números amigos](https://bit.ly/36gSRHt) son dos números enteros
# positivos distintos tales que la suma de los divisores propios de
# cada uno es igual al otro. Los divisores propios de un número
# incluyen la unidad pero no al propio número. Por ejemplo, los
# divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y
# 110. La suma de estos números equivale a 284. A su vez, los divisores
# propios de 284 son 1, 2, 4, 71 y 142. Su suma equivale a 220. Por
# tanto, 220 y 284 son amigos.
#
# Definir la función
#    amigos : (int, int) -> bool
# tal que amigos(x, y) se verifica si los números x e y son amigos. Por
# ejemplo,
#    amigos(220, 284) == True
#    amigos(220, 23)  == False
#    amigos(42262694537514864075544955198125, 42405817271188606697466971841875) == True
# ---------------------------------------------------------------------

from functools import reduce
from operator import mul
from timeit import Timer, default_timer

from sympy import divisor_sigma, factorint, is_amicable, proper_divisors

# 1ª solución
# ===========

# divisoresPropios1(x) es la lista de los divisores propios de x. Por
# ejemplo,
#    divisoresPropios1(220)  ==  [1,2,4,5,10,11,20,22,44,55,110]
#    divisoresPropios1(284)  ==  [1,2,4,71,142]
def divisoresPropios1(x: int) -> list[int]:
    return [n for n in range(1, x) if x % n == 0]

# sumaDivisoresPropios1(x) es la suma de los divisores propios de
# x. Por ejemplo,
#    sumaDivisoresPropios1(220)  ==  284
#    sumaDivisoresPropios1(284)  ==  220
def sumaDivisoresPropios1(x: int) -> int:
    return sum(divisoresPropios1(x))

def amigos1(x: int, y: int) -> bool:
    return sumaDivisoresPropios1(x)== y and \
           sumaDivisoresPropios1(y)== x

# 2ª solución
# ===========

def divisoresPropios2(x: int) -> list[int]:
    return proper_divisors(x)

def sumaDivisoresPropios2(x: int) -> int:
    return sum(divisoresPropios2(x))

def amigos2(x: int, y: int) -> bool:
    return sumaDivisoresPropios2(x)== y and \
           sumaDivisoresPropios2(y)== x

# 3ª solución
# ===========

# Si la descomposición de x en factores primos es
#    x = p(1)^e(1) . p(2)^e(2) . .... . p(n)^e(n)
# entonces la suma de los divisores de x es
#    p(1)^(e(1)+1) - 1     p(2)^(e(2)+1) - 1       p(n)^(e(2)+1) - 1
#   ------------------- . ------------------- ... -------------------
#        p(1)-1                p(2)-1                  p(n)-1
# Ver la demostración en http://bit.ly/2zUXZPc

# producto(xs) es el producto de los elementos de xs. Por ejemplo,
#    producto([2, 3, 5]) == 30
def producto(xs: list[int]) -> int:
    return reduce(mul, xs)

# sumaDivisoresPropios3(x) es la suma de los divisores propios de
# x. Por ejemplo,
#    sumaDivisoresPropios3(220)  ==  284
#    sumaDivisoresPropios3(284)  ==  220
def sumaDivisoresPropios3(x: int) -> int:
    return producto([(p**(e+1)-1) // (p-1)
                     for (p,e) in factorint(x).items()]) - x

def amigos3(x: int, y: int) -> bool:
    return sumaDivisoresPropios3(x)== y and \
           sumaDivisoresPropios3(y)== x

# 4ª solución
# ===========

def amigos4(x: int, y: int) -> bool:
    return divisor_sigma(x, 1) == divisor_sigma(y, 1)

# 5ª solución
# ===========

def amigos5(x: int, y: int) -> bool:
    return is_amicable(x, y)

# Verificación
# ============

def test_amigos() -> None:
    for amigos in [amigos1, amigos2, amigos3, amigos4, amigos5]:
        assert amigos(220, 284)
        assert not amigos(220, 23)
    print("Verificado")

# La verificación es
#    >>> test_amigos()
#    Verificado

# Comparación de eficiencia
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('amigos1(5864660, 7489324)')
#    0.65 segundos
#    >>> tiempo('amigos2(5864660, 7489324)')
#    0.00 segundos
#    >>> tiempo('amigos3(5864660, 7489324)')
#    0.00 segundos
#    >>> tiempo('amigos4(5864660, 7489324)')
#    0.00 segundos
#    >>> tiempo('amigos5(5864660, 7489324)')
#    0.00 segundos
#
#    >>> x = 42262694537514864075544955198125
#    >>> y = 42405817271188606697466971841875
#    >>> tiempo('amigos2(x, y)')
#    0.10 segundos
#    >>> tiempo('amigos3(x, y)')
#    0.00 segundos
#    >>> tiempo('amigos4(x, y)')
#    0.00 segundos
#    >>> tiempo('amigos5(x, y)')
#    0.00 segundos
