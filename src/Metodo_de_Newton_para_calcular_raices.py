# Metodo_de_Newton_para_calcular_raices.py
# Método de Newton para calcular raíces.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 4-noviembre-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Los ceros de una función pueden calcularse mediante el método de
# Newton basándose en las siguientes propiedades:
# + Si b es una aproximación para el punto cero de f, entonces
#   b-f(b)/f'(b) es una mejor aproximación.
# + el límite de la sucesión x_n definida por
#      x_0     = 1
#      x_{n+1} = x_n-f(x_n)/f'(x_n)
#   es un cero de f.
#
# Definir la función
#    puntoCero : (Callable[[float], float]) -> float
# tal que puntoCero(f) es un cero de la función f calculado usando la
# propiedad anterior. Por ejemplo,
#    puntoCero(cos)  ==  1.5707963267949576
# ---------------------------------------------------------------------

from typing import Callable
from math import sin, cos, pi

# 1ª solución
# ===========

# derivada(f, x) es el valor de la derivada de la función f en el punto
# x con aproximación 0.0001. Por ejemplo,
#    derivada(sin, pi) == -0.9999999983354435
#    derivada(cos, pi) == 4.999999969612645e-5
def derivada(f: Callable[[float], float], x: float) -> float:
    a = 0.0001
    return (f(x+a) - f(x)) / a

def puntoCero(f: Callable[[float], float]) -> float:
    def aceptable(b: float) -> bool:
        return abs(f(b)) < 0.00001
    def mejora(b: float) -> float:
        return b - f(b) / derivada(f, b)
    def aux(g: Callable[[float], float], x: float) -> float:
        if aceptable(x):
            return x
        return aux(g, mejora(x))
    return aux(f, 1)

# 2ª solución
# ===========

def puntoCero2(f: Callable[[float], float]) -> float:
    def aceptable(b: float) -> bool:
        return abs(f(b)) < 0.00001
    def mejora(b: float) -> float:
        return b - f(b) / derivada(f, b)
    y = 1.0
    while not aceptable(y):
        y = mejora(y)
    return y

# Verificación
# ============

def test_puntoCero () -> None:
    assert puntoCero(cos) == 1.5707963267949576
    assert puntoCero(cos) - pi/2 == 6.106226635438361e-14
    assert puntoCero(sin) == -5.8094940533562345e-15
    assert puntoCero2(cos) == 1.5707963267949576
    assert puntoCero2(cos) - pi/2 == 6.106226635438361e-14
    assert puntoCero2(sin) == -5.8094940533562345e-15
    print("Verificado")

# La comprobación es
#    >>> test_puntoCero()
#    Verificado
