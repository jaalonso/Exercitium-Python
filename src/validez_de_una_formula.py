# validez_de_una_formula.py
# Reconocedor de tautologías.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 05-diciembre-2022
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
# Una fórmula es una tautología si es verdadera en todas sus
# interpretaciones. Por ejemplo,
# + (A ∧ B) → A es una tautología
# + A → (A ∧ B) no es una tautología
#
# Definir la función
#    esTautologia :: FProp -> Bool
# tal que (esTautologia p) se verifica si la fórmula p es una
# tautología. Por ejemplo,
#    >>> esTautologia(Impl(Conj(Var('A'), Var ('B')), Var('A')))
#    True
#    >>> esTautologia(Impl(Var('A'), Conj(Var('A'), Var('B'))))
#    False
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

# interpretaciones(p) es la lista de las interpretaciones de la fórmula
# p. Por ejemplo,
#    >>> interpretaciones(Impl(Var('A'), Conj(Var('A'), Var('B'))))
#    [[('B', False), ('A', False)],
#     [('B', False), ('A', True)],
#     [('B', True), ('A', False)],
#     [('B', True), ('A', True)]]
def interpretaciones(f: FProp) -> list[Interpretacion]:
    vs = list(set(variables(f)))
    return [list(zip(vs, i)) for i in interpretacionesVar(len(vs))]

def esTautologia(p: FProp) -> bool:
    return all((valor(i, p) for i in interpretaciones(p)))
