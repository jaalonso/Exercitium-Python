# Mayor_numero_con_dos_digitos_dados.py
# Mayor número con dos dígitos dados.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 8-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    numeroMayor :: Int -> Int -> Int
# tal que (numeroMayor x y) es el mayor número de dos cifras que puede
# construirse con los dígitos x e y. Por ejemplo,
#    numeroMayor 2 5 ==  52
#    numeroMayor 5 2 ==  52
# ---------------------------------------------------------------------

# 1ª definición
def numeroMayor1(x, y):
    return 10 * max(x, y) + min(x, y)

# 2ª definición
def numeroMayor2(x, y):
    if x > y:
        return 10*x+y
    return 10*y+x

# La propiedad de equivalencia de las definiciones es
def test_equiv_numeroMayor():
    return all(numeroMayor1(x, y) == numeroMayor2(x, y)
               for x in range(10) for y in range(10))

# La comprobación es
#    >>> test_equiv_numeroMayor()
#    True
