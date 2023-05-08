# Pol_Division_de_Ruffini_con_representacion_densa.py
# TAD de los polinomios: Regla de Ruffini con representación densa.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 16-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu)
# definir la función
#    ruffiniDensa : (int, list[int]) -> list[int]
# tal que ruffiniDensa(r, cs) es la lista de los coeficientes del
# cociente junto con el rsto que resulta de aplicar la regla de Ruffini
# para dividir el polinomio cuya representación densa es cs entre
# x-r. Por ejemplo,
#    ruffiniDensa(2, [1, 2, -1, -2]) == [1, 4, 7, 12]
#    ruffiniDensa(1, [1, 2, -1, -2]) == [1, 3, 2, 0]
# ya que
#      | 1  2  -1  -2           | 1  2  -1  -2
#    2 |    2   8  14         1 |    1   3   2
#    --+--------------        --+-------------
#      | 1  4   7  12           | 1  3   2   0
# ---------------------------------------------------------------------

def ruffiniDensa(r: int, p: list[int]) -> list[int]:
    if not p:
        return []
    res = [p[0]]
    for x in p[1:]:
        res.append(x + r * res[-1])
    return res
