# Caminos_en_un_triangulo.py
# Caminos en un triángulo.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 4-enero-2025
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Los triángulos se pueden representar mediante listas de listas. Por
# ejemplo, el triángulo
#       3
#      7 4
#     2 4 6
#    8 5 9 3
# se representa por
#    [[3],[7,4],[2,4,6],[8,5,9,3]]
#
# Definir la función
#    caminos : (list[list[A]]) -> list[list[A]]
# tal que caminos(xss) es la lista de los caminos en el triángulo xss
# donde los caminos comienzan en el elemento de la primera fila, en cada
# paso se mueve a uno de  sus dos elementos adyacentes en la fila
# siguiente y terminan en la última fila. Por ejemplo,
#    >>> caminos([[3],[7,4]])
#    [[3,7],[3,4]]
#    >>> caminos([[3],[7,4],[2,4,6]])
#    [[3,7,2],[3,7,4],[3,4,4],[3,4,6]]
#    >>> caminos([[3],[7,4],[2,4,6],[8,5,9,3]])
#    [[3,7,2,8],[3,7,2,5],[3,7,4,5],[3,7,4,9],[3,4,4,5],[3,4,4,9],[3,4,6,9],[3,4,6,3]]
# ---------------------------------------------------------------------

from typing import TypeVar

A = TypeVar('A')

def caminos(xss: list[list[A]]) -> list[list[A]]:
    if not xss:
        return [[]]
    if len(xss) == 1:
        return xss
    x = xss[0][0]
    y1 = xss[1][0]
    y2 = xss[1][1]
    zss = xss[2:]
    return [[x, y1] + us for _, *us in caminos([[y1]] + [zs[:-1] for zs in zss])] + \
           [[x, y2] + us for _, *us in caminos([[y2]] + [zs[1:] for zs in zss])]

# Verificación
# ============

def test_caminos() -> None:
    assert caminos([[3],[7,4]]) == \
        [[3,7],[3,4]]
    assert caminos([[3],[7,4],[2,4,6]]) == \
        [[3,7,2],[3,7,4],[3,4,4],[3,4,6]]
    assert caminos([[3],[7,4],[2,4,6],[8,5,9,3]]) == \
        [[3,7,2,8],[3,7,2,5],[3,7,4,5],[3,7,4,9],[3,4,4,5],[3,4,4,9],[3,4,6,9],[3,4,6,3]]
    print("Verificado")

# La verificación es
#    >>> test_caminos()
#    Verificado
