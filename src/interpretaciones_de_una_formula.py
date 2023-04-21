# interpretaciones_de_una_formula.py
# El tipo de las fórmulas proposicionales: Interpretaciones de una fórmula
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 02-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las fórmulas proposicionales](https://bit.ly/3L3G2SX),
# definir la función
#    interpretaciones : (FProp) -> list[Interpretacion]
# tal que interpretaciones(p) es la lista de las interpretaciones de
# la fórmula p. Por ejemplo,
#    >>> interpretaciones(Impl(Var('A'), Conj(Var('A'), Var('B'))))
#    [[('B', False), ('A', False)],
#     [('B', False), ('A', True)],
#     [('B', True), ('A', False)],
#     [('B', True), ('A', True)]]
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from src.tipo_de_formulas import Conj, Const, FProp, Impl, Neg, Var
from src.valor_de_una_formula import Interpretacion
from src.variables_de_una_formula import variables


# interpretacionesVar(n) es la lista de las interpretaciones de n
# variables. Por ejemplo,
#    >>> interpretacionesVar 2
#    [[False, False],
#     [False, True],
#     [True, False],
#     [True, True]]
def interpretacionesVar(n: int) -> list[list[bool]]:
    if n == 0:
        return [[]]
    bss = interpretacionesVar(n-1)
    return [[False] + x for x in bss] + [[True] + x for x in bss]

def interpretaciones(f: FProp) -> list[Interpretacion]:
    vs = list(set(variables(f)))
    return [list(zip(vs, i)) for i in interpretacionesVar(len(vs))]
