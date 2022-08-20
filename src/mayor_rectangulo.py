# mayor_rectangulo.py
# Mayor rectángulo.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 2-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Las dimensiones de los rectángulos puede representarse por pares; por
# ejemplo, (5,3) representa a un rectángulo de base 5 y altura 3.
#
# Definir la función
#    mayorRectangulo : (tuple[float, float], tuple[float, float])
#                      -> tuple[float, float]
# tal que mayorRectangulo(r1, r2) es el rectángulo de mayor área entre
# r1 y r2. Por ejemplo,
#    mayorRectangulo((4, 6), (3, 7))  ==  (4, 6)
#    mayorRectangulo((4, 6), (3, 8))  ==  (4, 6)
#    mayorRectangulo((4, 6), (3, 9))  ==  (3, 9)
# ---------------------------------------------------------------------

def mayorRectangulo(r1: tuple[float, float],
                    r2: tuple[float, float]) -> tuple[float, float]:
    (a, b) = r1
    (c, d) = r2
    if a*b >= c*d:
        return (a, b)
    return (c, d)
