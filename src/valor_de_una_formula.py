# valor_de_una_formula.py
# El tipo de las fórmulas proposicionales: Valor de una fórmula
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 01-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Una interpretación de una fórmula es una función de sus variables en
# los booleanos. Por ejemplo, la interpretación que a la variable A le
# asigna verdadero y a la B falso se puede representar por
#    [('A', True), ('B', False)]
#
# El tipo de las intepretaciones de puede definir por
#    Interpretacion = list[tuple[str, bool]]
#
# El valor de una fórmula en una interpretación se calcula usando las
# funciones de verdad de las conectivas que se muestran a continuación
#    |---+----|   |---+---+-------+-------|
#    | p | ¬p |   | p | q | p ∧ q | p → q |
#    |---+----|   |---+---+-------+-------|
#    | T | F  |   | T | T | T     | T     |
#    | F | T  |   | T | F | F     | F     |
#    |---+----|   | F | T | F     | T     |
#                 | F | F | F     | T     |
#                 |---+---+-------+-------|
#
# Usando el [tipo de las fórmulas proposicionales](https://bit.ly/3L3G2SX),
# definir la función
#    valor: (Interpretacion, FProp) -> bool:
# tal que valor(i, p) es el valor de la fórmula p en la interpretación
# i. Por ejemplo,
#    >>> p = Impl(Var('A'), Conj(Var('A'), Var('B')))
#    >>> valor([('A',False),('B',False)], p)
#    True
#    >>> valor([('A',True),('B',False)], p)
#    False
# ---------------------------------------------------------------------

from src.tipo_de_formulas import Conj, Const, FProp, Impl, Neg, Var

Interpretacion = list[tuple[str, bool]]

# busca(c, t) es el valor del primer elemento de la lista de asociación
# t cuya clave es c. Por ejemplo,
#    >>> busca('B', [('A', True), ('B', False), ('C', True)])
#    False
def busca(c: str, i: Interpretacion) -> bool:
    return [v for (d, v) in i if d == c][0]

def valor(i: Interpretacion, f: FProp) -> bool:
    match f:
        case Const(b):
            return b
        case Var(x):
            return busca(x, i)
        case Neg(p):
            return not valor(i, p)
        case Conj(p, q):
            return valor(i, p) and valor(i, q)
        case Impl(p, q):
            return valor(i, p) <= valor(i, q)
    assert False
