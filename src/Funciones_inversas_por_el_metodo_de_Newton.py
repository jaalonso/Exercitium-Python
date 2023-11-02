# Funciones_inversas_por_el_metodo_de_Newton.hs
# Funciones inversas por el método de Newton.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 9-noviembre-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir, usando puntoCero, la función
#    inversa : (Callable[[float],float], float) -> float
# tal que inversa(g, x) es el valor de la inversa de g en x. Por
# ejemplo,
#    inversa(lambda x: x**2, 9)  ==  3.000000002941184
#
# Definir, usando inversa, las funciones raizCuadrada, raizCubica,
# arcoseno y arcocoseno que calculen la raíz cuadrada, la raíz cúbica,
# el arco seno y el arco coseno, respectivamente. Por ejemplo,
#    raizCuadrada(9)  ==  3.000000002941184
#    raizCubica(27)   ==  3.0000000000196048
#    arcoseno(1)      ==  1.5665489428306574
#    arcocoseno(0)    ==  1.5707963267949576
# ---------------------------------------------------------------------

from math import cos, sin
from typing import Callable

from src.Metodo_de_Newton_para_calcular_raices import puntoCero


def inversa(g: Callable[[float],float], a: float) -> float:
    def f(x: float) -> float:
        return g(x) - a
    return puntoCero(f)

def raizCuadrada(x: float) -> float:
    return inversa(lambda y: y**2, x)

def raizCubica(x: float) -> float:
    return inversa(lambda y: y**3, x)

def arcoseno(x: float) -> float:
    return inversa(sin, x)

def arcocoseno(x: float) -> float:
    return inversa(cos, x)

# Verificación
# ============

def test_inversa() -> None:
    assert inversa(lambda x: x**2, 9) == 3.000000002941184
    assert raizCuadrada(9) == 3.000000002941184
    assert raizCubica(27) == 3.0000000000196048
    assert arcoseno(1) == 1.5665489428306574
    assert arcocoseno(0) == 1.5707963267949576
    print("Verificado")

# La comprobación es
#    >>> test_inversa()
#    Verificado
