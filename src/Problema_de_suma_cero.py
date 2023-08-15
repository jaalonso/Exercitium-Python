# Problema_de_suma_cero.py
# Problema de suma cero.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 4-Septiembre-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El problema de suma cero consiste en, dado el conjunto de números
# enteros, encontrar sus subconjuntos no vacío cuyos elementos sumen
# cero.
#
# Usando el [procedimiento de búsqueda en profundidad](https://bit.ly/3NPI4qV),
# definir la función
#    suma0 : (list[int]) -> list[list[int]]
# tal que suma0(ns) es la lista de las soluciones del problema de suma
# cero para ns. Por ejemplo,
#    λ> suma0([-7,-3,-2,5,8])
#    [[-3,-2,5]]
#    λ> suma0([-7,-3,-2,5,8,-1])
#    [[-7,-3,-2,-1,5,8],[-7,-1,8],[-3,-2,5]]
#    λ> suma0([-7,-3,1,5,8])
#    []
# ---------------------------------------------------------------------

from src.BusquedaEnProfundidad import buscaProfundidad

# Los estados son ternas formadas por los números seleccionados, su
# suma y los restantes números.
Estado = tuple[list[int], int, list[int]]

def inicial(ns: list[int]) -> Estado:
    return ([], 0, ns)

def esFinal(e: Estado) -> bool:
    (xs,s,_) = e
    return xs != [] and s == 0

def sucesores(e: Estado) -> list[Estado]:
    (xs, s, ns) = e
    return [([n] + xs, n + s, [m for m in ns if m !=n])
            for n in ns]

def soluciones(ns: list[int]) -> list[Estado]:
    return buscaProfundidad(sucesores, esFinal, inicial(ns))

def suma0(ns: list[int]) -> list[list[int]]:
    xss = [list(sorted(s[0])) for s in soluciones(ns)]
    r = []
    for xs in xss:
        if xs not in r:
            r.append(xs)
    return r

# Verificación
# ============

def test_suma0() -> None:
    assert suma0([-7,-3,-2,5,8]) == \
        [[-3,-2,5]]
    assert suma0([-7,-3,-2,5,8,-1]) == \
        [[-7,-3,-2,-1,5,8],[-7,-1,8],[-3,-2,5]]
    assert not suma0([-7,-3,1,5,8])
    print("Verificado")

# La verificación es
#    >>> test_suma0()
#    Verificado
