# interpretaciones_de_una_formula.ps
# El tipo de las fórmulas proposicionales: Interpretaciones de una fórmula
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 02-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El tipo de las fórmulas proposicionales se puede definir por
#    @dataclass
#    class FProp:
#        pass
#
#    @dataclass
#    class Const(FProp):
#        x: bool
#
#    @dataclass
#    class Var(FProp):
#        x: str
#
#    @dataclass
#    class Neg(FProp):
#        x: FProp
#
#    @dataclass
#    class Conj(FProp):
#        x: FProp
#        y: FProp
#
#    @dataclass
#    class Impl(FProp):
#        x: FProp
#        y: FProp
# de modo que la fórmula A → ⊥ ∧ ¬B se representa por
#    Impl(Var('A'), Conj(Const(False), Neg (Var('B'))))
#
# Una interpretación de una fórmula es una función de sus variables en
# los booleanos. Por ejemplo, la interpretación que a la variable A le
# asigna verdadero y a la B falso se puede representar por
#    [('A', True), ('B', False)]
#
# El tipo de las intepretaciones de puede definir por
#    Interpretacion = list[tuple[str, bool]]
#
# Definir la función
#    interpretaciones : (FProp) -> list[Interpretacion]
# tal que interpretaciones(p) es la lista de las interpretaciones de
# la fórmula p. Por ejemplo,
#    >>> interpretaciones(Impl(Var('A'), Conj(Var('A'), Var('B'))))
#    [[('B', False), ('A', False)],
#     [('B', False), ('A', True)],
#     [('B', True), ('A', False)],
#     [('B', True), ('A', True)]]
# ---------------------------------------------------------------------

from dataclasses import dataclass


@dataclass
class FProp:
    pass

@dataclass
class Const(FProp):
    x: bool

@dataclass
class Var(FProp):
    x: str

@dataclass
class Neg(FProp):
    x: FProp

@dataclass
class Conj(FProp):
    x: FProp
    y: FProp

@dataclass
class Impl(FProp):
    x: FProp
    y: FProp

Interpretacion = list[tuple[str, bool]]

# variables(p) es la lista de las variables de la fórmula p. Por
# ejemplo,
#    >>> variables (Impl(Var('A'), Conj(Const(False), Neg (Var('B')))))
#    ['A', 'B']
#    >>> variables (Impl(Var('A'), Conj(Var('A'), Neg (Var('B')))))
#    ['A', 'A', 'B']
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
