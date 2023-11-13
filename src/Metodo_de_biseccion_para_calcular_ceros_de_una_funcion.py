# Metodo_de_biseccion_para_calcular_ceros_de_una_funcion.py
# Método de bisección para calcular ceros de una función.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 19-noviembre-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El método de bisección para calcular un cero de una función en el
# intervalo [a,b] se basa en el teorema de Bolzano:
#    "Si f(x) es una función continua en el intervalo [a, b], y si,
#    además, en los extremos del intervalo la función f(x) toma valores
#    de signo opuesto (f(a) * f(b) < 0), entonces existe al menos un
#    valor c en (a, b) para el que f(c) = 0".
#
# El método para calcular un cero de la función f en el intervalo [a,b]
# con un error menor que e consiste en tomar el punto medio del
# intervalo c = (a+b)/2 y considerar los siguientes casos:
# + Si |f(c)| < e, hemos encontrado una aproximación del punto que
#   anula f en el intervalo con un error aceptable.
# + Si f(c) tiene signo distinto de f(a), repetir el proceso en el
#   intervalo [a,c].
# + Si no, repetir el proceso en el intervalo [c,b].
#
# Definir la función
#    biseccion : (Callable[[float], float], float, float, float) -> float
# tal que biseccion(f, a, b, e) es una aproximación del punto del
# intervalo [a,b] en el que se anula la función f, con un error menor
# que e, calculada mediante el método de la bisección. Por ejemplo,
#    biseccion(lambda x : x**2 - 3, 0, 5, 0.01)        == 1.7333984375
#    biseccion(lambda x : x**3 - x - 2, 0, 4, 0.01)    == 1.521484375
#    biseccion(cos, 0, 2, 0.01)                        == 1.5625
#    biseccion(lambda x : log(50-x) - 4, -10, 3, 0.01) == -5.125
# ---------------------------------------------------------------------

from math import cos, log
from typing import Callable

# 1ª solución
# ===========

def biseccion(f: Callable[[float], float],
              a: float,
              b: float,
              e: float) -> float:
    c = (a+b)/2
    if abs(f(c)) < e:
        return c
    if f(a) * f(c) < 0:
        return biseccion(f, a, c, e)
    return biseccion(f, c, b, e)

# 2ª solución
# ===========

def biseccion2(f: Callable[[float], float],
               a: float,
               b: float,
               e: float) -> float:
    def aux(a1: float,  b1: float) -> float:
        c = (a1+b1)/2
        if abs(f(c)) < e:
            return c
        if f(a1) * f(c) < 0:
            return aux(a1, c)
        return aux(c, b1)
    return aux(a, b)

# Verificación
# ============

def test_biseccion() -> None:
    assert biseccion(lambda x : x**2 - 3, 0, 5, 0.01) == 1.7333984375
    assert biseccion(lambda x : x**3 - x - 2, 0, 4, 0.01) == 1.521484375
    assert biseccion(cos, 0, 2, 0.01) == 1.5625
    assert biseccion(lambda x : log(50-x) - 4, -10, 3, 0.01) == -5.125
    assert biseccion2(lambda x : x**2 - 3, 0, 5, 0.01) == 1.7333984375
    assert biseccion2(lambda x : x**3 - x - 2, 0, 4, 0.01) == 1.521484375
    assert biseccion2(cos, 0, 2, 0.01) == 1.5625
    assert biseccion2(lambda x : log(50-x) - 4, -10, 3, 0.01) == -5.125
    print("Verificado")

# La comprobación es
#    >>> test_biseccion()
#    Verificado
