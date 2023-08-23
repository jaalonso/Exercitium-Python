# Problema_de_las_jarras.py
# Problema de las jarras.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 9-septiembre-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# En el problema de las jarras (A,B,C) se tienen dos jarras sin marcas
# de medición, una de A litros de capacidad y otra de B. También se
# dispone de una bomba que permite llenar las jarras de agua.
#
# El problema de las jarras (A,B,C) consiste en determinar cómo se
# puede lograr tener exactamente C litros de agua en la jarra de A
# litros de capacidad.
#
# Usando el [procedimiento de búsqueda en anchura](https://bit.ly/3XBlqG7),
# definir la función
#    jarras: tuple[int,int,int] -> list[list[tuple[int,int]]]
# tal jarras((a,b,c)) es la lista de las soluciones del problema de las
# jarras (a,b,c). Por ejemplo,
#    >>> jarras((4,3,2))[:3]
#    [[(0, 0), (4, 0), (1, 3), (1, 0), (0, 1), (4, 1), (2, 3)],
#     [(0, 0), (0, 3), (3, 0), (3, 3), (4, 2), (0, 2), (2, 0)],
#     [(0, 0), (4, 0), (4, 3), (0, 3), (3, 0), (3, 3), (4, 2), (0, 2), (2, 0)]]
#
# La interpretación [(0,0),(4,0),(1,3),(1,0),(0,1),(4,1),(2,3)] es:
#    (0,0) se inicia con las dos jarras vacías,
#    (4,0) se llena la jarra de 4 con el grifo,
#    (1,3) se llena la de 3 con la de 4,
#    (1,0) se vacía la de 3,
#    (0,1) se pasa el contenido de la primera a la segunda,
#    (4,1) se llena la primera con el grifo,
#    (2,3) se llena la segunda con la primera.
#
# Otros ejemplos
#    >>> len(jarras((15,10,5)))
#    8
#    >>> [len(e) for e in jarras((15,10,5))]
#    [3, 5, 5, 7, 7, 7, 8, 9]
#    >>> jarras((15,10,4))
#    []
# ---------------------------------------------------------------------

from src.BusquedaEnAnchura import buscaAnchura

# Un problema es una lista de 3 números enteros (a,b,c) tales que a es
# la capacidad de la primera jarra, b es la capacidad de la segunda
# jarra y c es el número de litros que se desea obtener en la primera
# jarra.
Problema = tuple[int, int, int]

# Una configuracion es una lista de dos números. El primero es el
# contenido de la primera jarra y el segundo el de la segunda.
Configuracion = tuple[int, int]

# Inicialmente, las dos jarras están vacías.
configuracionInicial: Configuracion = (0,0)

# esConfiguracionFinal(p, e) se verifica si e es un configuracion final
# del problema p.
def esConfiguracionFinal(p: Problema, c: Configuracion) -> bool:
    return p[2] == c[0]

# sucesorasConfiguracion(p, c) son las sucesoras de la configuración c
# del problema p. Por ejemplo,
#    sucesorasConfiguracion((4,3,2), (0,0))  ==  [(4,0),(0,3)]
#    sucesorasConfiguracion((4,3,2), (4,0))  ==  [(4,3),(0,0),(1,3)]
#    sucesorasConfiguracion((4,3,2), (4,3))  ==  [(0,3),(4,0)]
def sucesorasConfiguracion(p: Problema, c: Configuracion) -> list[Configuracion]:
    (a, b, _) = p
    (x, y) = c
    r = []
    if x < a:
        r.append((a, y))
    if y < b:
        r.append((x, b))
    if x > 0:
        r.append((0, y))
    if y > 0:
        r.append((x, 0))
    if x < a and y > 0 and x + y > a:
        r.append((a, y - (a - x)))
    if x > 0 and y < b and x + y > b:
        r.append((x - (b - y), b))
    if y > 0 and x + y <= a:
        r.append((x + y, 0))
    if x > 0 and x + y <= b:
        r.append((0, x + y))
    return r

# Los estados son listas de configuraciones [c_n,...c_2,c_1] tales que
# c_1 es la configuración inicial y, para 2 <= i <= n, c_i es una
# sucesora de c_(i-1).
Estado = list[Configuracion]

# inicial es el estado cuyo único elemento es la configuración
# inicial.
inicial: Estado = [configuracionInicial]

# esFinal(p, e) se verifica si e es un estado final; es decir, su
# primer elemento es una configuración final.
def esFinal(p: Problema, e: Estado) -> bool:
    return esConfiguracionFinal(p, e[0])

# sucesores(p, e) es la lista de los sucesores del estado e en el
# problema p. Por ejemplo,
#    λ> sucesores((4,3,2), [(0,0)])
#    [[(4,0),(0,0)],[(0,3),(0,0)]]
#    λ> sucesores((4,3,2), [(4,0),(0,0)])
#    [[(4,3),(4,0),(0,0)],[(1,3),(4,0),(0,0)]]
#    λ> sucesores((4,3,2), [(4,3),(4,0),(0,0)])
#    [[(0,3),(4,3),(4,0),(0,0)]]
def sucesores(p: Problema, e: Estado) -> list[Estado]:
    return [[c] + e
            for c in sucesorasConfiguracion(p, e[0])
            if c not in e]

def jarras(p: Problema) -> list[Estado]:
    soluciones = buscaAnchura(lambda e: sucesores(p, e),
                              lambda e: esFinal(p, e),
                              inicial)
    return [list(reversed(e)) for e in soluciones]

# Verificación
# ============

def test_jarras() -> None:
    assert jarras((4,3,2))[:3] == \
        [[(0, 0), (4, 0), (1, 3), (1, 0), (0, 1), (4, 1), (2, 3)],
         [(0, 0), (0, 3), (3, 0), (3, 3), (4, 2), (0, 2), (2, 0)],
         [(0, 0), (4, 0), (4, 3), (0, 3), (3, 0), (3, 3), (4, 2), (0, 2), (2, 0)]]
    assert len(jarras((15,10,5))) == 8
    assert [len(e) for e in jarras((15,10,5))] == [3, 5, 5, 7, 7, 7, 8, 9]
    assert jarras((15,10,4)) == []
    print("Verificado")

# La verificación es
#    >>> test_jarras()
#    Verificado
