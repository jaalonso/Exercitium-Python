# Limites_de_sucesiones.py
# Límites de sucesiones.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 14-noviembre-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    limite :: (Double -> Double) -> Double -> Double
# tal que limite(f, a) es el valor de f en el primer término x tal que,
# para todo y entre x+1 y x+100, el valor absoluto de la diferencia
# entre f(y) y f(x) es menor que a. Por ejemplo,
#    limite(lambda n :  (2*n+1)/(n+5), 0.001) ==  1.9900110987791344
#    limite(lambda n : (1+1/n)**n, 0.001)     ==  2.714072874546881
# ---------------------------------------------------------------------

from itertools import count
from typing import Callable

# 1ª solución
# ===========

def limite(f: Callable[[float], float], a: float) -> float:
    x = 1
    while True:
        maximum_diff = max(abs(f(y) - f(x)) for y in range(x+1, x+101))
        if maximum_diff < a:
            return f(x)
        x += 1

# 2ª solución
# ===========

def limite2(f: Callable[[float], float], a: float) -> float:
    x = 1
    while True:
        y = f(x)
        if max(abs(y - f(x + i)) for i in range(1, 101)) < a:
            break
        x += 1
    return y

# 3ª solución
# ===========

def limite3(f: Callable[[float], float], a: float) -> float:
    for x in count(1):
        if max(abs(f(y) - f(x)) for y in range(x + 1, x + 101)) < a:
            r = f(x)
            break
    return r

# Verificación
# ============

def test_limite() -> None:
    assert limite(lambda n :  (2*n+1)/(n+5), 0.001) ==  1.9900110987791344
    assert limite(lambda n : (1+1/n)**n, 0.001)     ==  2.714072874546881
    assert limite2(lambda n :  (2*n+1)/(n+5), 0.001) ==  1.9900110987791344
    assert limite2(lambda n : (1+1/n)**n, 0.001)     ==  2.714072874546881
    assert limite3(lambda n :  (2*n+1)/(n+5), 0.001) ==  1.9900110987791344
    assert limite3(lambda n : (1+1/n)**n, 0.001)     ==  2.714072874546881
    print("Verificado")

# La comprobación es
#    >>> test_limite()
#    Verificado
