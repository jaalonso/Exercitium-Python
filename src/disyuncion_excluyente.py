# disyuncion_excluyente.py
# Disyunción excluyente.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 1-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# La disyunción excluyente de dos fórmulas se verifica si una es
# verdadera y la otra es falsa. Su tabla de verdad es
#    x     | y     | xor x y
#    ------+-------+---------
#    True  | True  | False
#    True  | False | True
#    False | True  | True
#    False | False | False
#
# Definir la función
#    xor :: (bool, bool) -> bool
# tal que xor(x, y) es la disyunción excluyente de x e y. Por ejemplo,
#    xor(True, True) == False
#    xor(True, False) == True
#    xor(False, True) == True
#    xor(False, False) == False
# ---------------------------------------------------------------------

# 1ª solución
def xor1(x, y):
    match x, y:
        case True,  True: return False
        case True,  False: return True
        case False, True: return True
        case False, False: return False


# 2ª solución
def xor2(x, y):
    if x:
        return not y
    return y


# 3ª solución
def xor3(x, y):
    return (x or y) and not(x and y)


# 4ª solución
def xor4(x, y):
    return (x and not y) or (y and not x)


# 5ª solución
def xor5(x, y):
    return x != y
