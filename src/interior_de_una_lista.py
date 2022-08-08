# interior_de_una_lista.py
# Interior de una lista
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 22-agosto-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    interior : (List[A]) -> List[A]
# tal que interior(xs) es la lista obtenida eliminando los extremos de
# la lista xs. Por ejemplo,
#    interior([2, 5, 3, 7, 3])  ==  [5, 3, 7]
# ---------------------------------------------------------------------

# 1ª solución
def interior1(xs):
    return xs[1][:-1]


# 2ª solución
def interior2(xs):
    return xs[1:-1]
