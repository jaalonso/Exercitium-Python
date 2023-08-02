# Escalada_Monedas.py
# Problema de las monedas por búsqueda en escalada.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 4-agosto-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El problema del cambio de monedas consiste en determinar cómo
# conseguir una cantidad usando el menor número de monedas
# disponibles. Se supone que se posee un número ilimitado de monedas de
# 1, 2, 5, 10, 20, 50 y 100 euros. Por ejemplo, para conseguir 199 se
# necesitan como mínimo 7 monedas (129 = 2 + 2 + 5 + 20 + 20 + 50 + 100).
#
# En la representación se usarán los siguientes tipos:
# + Moneda, que es un número entero representado el valor de la moneda
# + Solucion, que es una lista de monedas cuya suma es la cantidad
#   deseada y no nay ninguna lista más corta con la misma suma.
#
# Usando la [búsqueda en escalada](https://bit.ly/3Kk4A99), definir la
# función
#    cambio : (int) -> Optional[Solucion]
# tal que (cambio n) es la solución del problema de las monedas, para
# obtener la cantidad n, por búsqueda en escalada. Por ejemplo,
#    cambio(199)  ==  [2,2,5,20,20,50,100]
# ---------------------------------------------------------------------

from typing import Optional

from src.BusquedaEnEscalada import buscaEscalada

# Las monedas son números enteros.
Moneda = int

# monedas es la lista del tipo de monedas disponibles. Se supone que
# hay un número infinito de monedas de cada tipo.
monedas: list[Moneda] = [1,2,5,10,20,50,100]

# Las soluciones son listas de monedas.
Solucion = list[Moneda]

# Los estados son pares formados por la cantidad que falta y la lista
# de monedas usadas.
Estado = tuple[int, list[Moneda]]

# inicial(n) es el estado inicial del problema de las monedas, para
# obtener la cantidad n.
def inicial(n: int) -> Estado:
    return (n, [])

# esFinal(e) se verifica si e es un estado final del problema
# de las monedas.
def esFinal(e: Estado) -> bool:
    return e[0] == 0

# sucesores(e) es la lista de los sucesores del estado e en el
# problema de las monedas. Por ejemplo,
#   λ> sucesores((199,[]))
#   [(198,[1]),(197,[2]),(194,[5]),(189,[10]),
#    (179,[20]),(149,[50]),(99,[100])]
def sucesores(e: Estado) -> list[Estado]:
    (r,p) = e
    return [(r - c, [c] + p) for c in monedas if r - c >= 0]

def cambio(n: int) -> Optional[Solucion]:
    r = buscaEscalada(sucesores, esFinal, inicial(n))
    if r is None:
        return None
    return r[1]

# Verificación
# ============

def test_monedas() -> None:
    assert cambio(199) == [2,2,5,20,20,50,100]

# La verificación es
#    src> poetry run pytest -q Escalada_Monedas.py
#    1 passed in 0.12s
