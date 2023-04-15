# variables_de_una_formula.py
# El tipo de las fórmulas proposicionales: Variables de una fórmula
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 30-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el tipo de las fórmulas proposicionales definido en el
# [ejercicio anterior](https://bit.ly/3L3G2SX), definir la función
#    variables : (FProp) -> list[str]:
# tal que variables(p) es la lista de las variables de la fórmula
# p. Por ejemplo,
#    >>> variables (Impl(Var('A'), Conj(Const(False), Neg (Var('B')))))
#    ['A', 'B']
#    >>> variables (Impl(Var('A'), Conj(Var('A'), Neg (Var('B')))))
#    ['A', 'A', 'B']
# ---------------------------------------------------------------------

from src.tipo_de_formulas import Conj, Const, FProp, Impl, Neg, Var


def variables(f: FProp) -> list[str]:
    match f:
        case Const(_):
            return []
        case Var(x):
            return [x]
        case Neg(p):
            return variables(p)
        case Conj(p, q):
            return variables(p) + variables(q)
        case Impl(p, q):
            return variables(p) + variables(q)
    assert False
