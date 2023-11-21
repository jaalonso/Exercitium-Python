# Integracion_por_rectangulos.hs
# Integración por el método de los rectángulos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-noviembre-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# La integral definida de una función f entre los límites a y b puede
# calcularse mediante la regla del rectángulo (ver en
# http://bit.ly/1FDhZ1z) usando la fórmula
#    h * (f(a+h/2) + f(a+h+h/2) + f(a+2h+h/2) + ... + f(a+n*h+h/2))
# con a+n*h+h/2 <= b < a+(n+1)*h+h/2 y usando valores pequeños para h.
#
# Definir la función
#    integral : (float, float, Callable[[float], float], float) -> float
# tal que integral(a, b, f, h) es el valor de dicha expresión. Por
# ejemplo, el cálculo de la integral de f(x) = x^3 entre 0 y 1, con
# paso 0.01, es
#    integral(0, 1, lambda x : x**3, 0.01) == 0.24998750000000042
# Otros ejemplos son
#    integral(0, 1, lambda x : x**4, 0.01) == 0.19998333362500054
#    integral(0, 1, lambda x : 3*x**2 + 4*x**3, 0.01) == 1.9999250000000026
#    log(2) - integral(1, 2, lambda x : 1/x, 0.01) == 3.124931644782336e-6
#    pi - 4 * integral(0, 1, lambda x : 1/(x**2+1), 0.01) == -8.333333331389525e-6
# ---------------------------------------------------------------------

from math import log, pi
from typing import Callable

# 1ª solución
# ===========

# sucesion(x, y, s) es la lista
#    [a, s(a), s(s(a), ..., s(...(s(a))...)]
# hasta que s(s(...(s(a))...)) > b. Por ejemplo,
#    sucesion(3, 20, lambda x : x+2)  ==  [3,5,7,9,11,13,15,17,19]
def sucesion(a: float, b: float, s: Callable[[float], float]) -> list[float]:
    xs = []
    while a <= b:
        xs.append(a)
        a = s(a)
    return xs

# suma(a, b, s, f) es el valor de
#    f(a) + f(s(a)) + f(s(s(a)) + ... + f(s(...(s(a))...))
# hasta que s(s(...(s(a))...)) > b. Por ejemplo,
#    suma(2, 5, lambda x: x+1, lambda x: x**3)  ==  224
def suma(a: float,
         b: float,
         s: Callable[[float], float],
         f: Callable[[float], float]) -> float:
    return sum(f(x) for x in sucesion(a, b, s))

def integral(a: float,
             b: float,
             f: Callable[[float], float],
             h: float) -> float:
    return h * suma(a+h/2, b, lambda x: x+h, f)

# 2ª solución
# ===========

def integral2(a: float,
              b: float,
              f: Callable[[float], float],
              h: float) -> float:
    if a+h/2 > b:
        return 0
    return h * f(a+h/2) + integral2(a+h, b, f, h)

# 3ª solución
# ===========

def integral3(a: float,
              b: float,
              f: Callable[[float], float],
              h: float) -> float:
    def aux(x: float) -> float:
        if x+h/2 > b:
            return 0
        return h * f(x+h/2) + aux(x+h)
    return aux(a)

# Verificación
# ============

def test_integral() -> None:
    def aproximado(a: float, b: float) -> bool:
        return abs(a - b) < 0.00001
    assert integral(0, 1, lambda x : x**3, 0.01) == 0.24998750000000042
    assert integral(0, 1, lambda x : x**4, 0.01) == 0.19998333362500054
    assert integral(0, 1, lambda x : 3*x**2 + 4*x**3, 0.01) == 1.9999250000000026
    assert log(2) - integral(1, 2, lambda x : 1/x, 0.01) == 3.124931644782336e-6
    assert pi - 4 * integral(0, 1, lambda x : 1/(x**2+1), 0.01) == -8.333333331389525e-6
    assert aproximado(integral2(0, 1, lambda x : x**3, 0.01),
                      0.24998750000000042)
    assert aproximado(integral2(0, 1, lambda x : x**4, 0.01),
                      0.19998333362500054)
    assert aproximado(integral2(0, 1, lambda x : 3*x**2 + 4*x**3, 0.01),
                      1.9999250000000026)
    assert aproximado(log(2) - integral2(1, 2, lambda x : 1/x, 0.01),
                      3.124931644782336e-6)
    assert aproximado(pi - 4 * integral2(0, 1, lambda x : 1/(x**2+1), 0.01),
                      -8.333333331389525e-6)
    assert aproximado(integral3(0, 1, lambda x : x**3, 0.01),
                      0.24998750000000042)
    assert aproximado(integral3(0, 1, lambda x : x**4, 0.01),
                      0.19998333362500054)
    assert aproximado(integral3(0, 1, lambda x : 3*x**2 + 4*x**3, 0.01),
                      1.9999250000000026)
    assert aproximado(log(2) - integral3(1, 2, lambda x : 1/x, 0.01),
                      3.124931644782336e-6)
    assert aproximado(pi - 4 * integral3(0, 1, lambda x : 1/(x**2+1), 0.01),
                      -8.333333331389525e-6)
    print("Verificado")

# La verificación es
#    >>> test_integral()
#    Verificado
