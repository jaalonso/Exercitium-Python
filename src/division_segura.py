# division_segura.py
# División segura.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 31-agosto-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    divisionSegura : (float, float) -> float
# tal que divisionSegura(x, y) es x/y si y no es cero y 9999 en caso
# contrario. Por ejemplo,
#    divisionSegura(7, 2)  ==  3.5
#    divisionSegura(7, 0)  ==  9999.0
# ---------------------------------------------------------------------

# 1ª definición
def divisionSegura1(x, y):
    if y == 0:
        return 9999.0
    return x/y


# 2ª definición
def divisionSegura2(x, y):
    match y:
        case 0:
            return 9999.0
        case _:
            return x/y
