# variables_de_una_formula.py
# El tipo de las fórmulas proposicionales: Variables de una fórmula
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 30-noviembre-2022
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
# Definir la función
#    variables : (FProp) -> list[str]:
# tal que variables(p) es la lista de las variables de la fórmula
# p. Por ejemplo,
#    >>> variables (Impl(Var('A'), Conj(Const(False), Neg (Var('B')))))
#    ['A', 'B']
#    >>> variables (Impl(Var('A'), Conj(Var('A'), Neg (Var('B')))))
#    ['A', 'A', 'B']
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
