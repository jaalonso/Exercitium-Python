# suma_de_un_arbol.py
# Suma de un árbol.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 23-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de los árboles binarios con valores en los nodos]
# (https://bit.ly/40Pplzj), definir la función
#    sumaArbol : (Arbol) -> int
# tal sumaArbol(x) es la suma de los valores que hay en el árbol x.
# Por ejemplo,
#    >>> sumaArbol(N(2, N(5, N(3, H(), H()), N(7, H(), H())), N(4, H(), H())))
#    21
# ---------------------------------------------------------------------

from src.arbol_binario_valores_en_nodos import Arbol, H, N


def sumaArbol(a: Arbol[int]) -> int:
    match a:
        case H():
            return 0
        case N(x, i, d):
            return x + sumaArbol(i) + sumaArbol(d)
    assert False
