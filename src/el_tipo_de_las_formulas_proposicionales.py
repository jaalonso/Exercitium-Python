# el_tipo_de_las_formulas_proposicionales.py
# El tipo de las fórmulas proposicionales.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 30-noviembre-2022
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

p1 = Conj(Var('A'), Neg(Var('A')))
p2 = Impl(Conj(Var('A'), Var('B')), Var('A'))
p3 = Impl(Var('A'), Conj(Var('A'), Var('B')))
p4 = Impl(Conj(Var('A'), Impl(Var('A'), Var('B'))), Var('B'))

Interpretacion = list[tuple[str, bool]]

# >>> busca('B', [('A', True), ('B', False), ('C', True)])
# False
def busca(c: str, i: Interpretacion) -> bool:
    return [v for (d, v) in i if d == c][0]

# valor([('A',False),('B',True)], p3)  ==  True
# valor([('A',True),('B',False)], p3)  ==  False
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

# variables(p3) == ['A', 'A', 'B']
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

# >>> interpretacionesVar(2)
# [[False, False], [False, True], [True, False], [True, True]]
def interpretacionesVar(n: int) -> list[list[bool]]:
    if n == 0:
        return [[]]
    bss = interpretacionesVar(n-1)
    return [[False] + x for x in bss] + [[True] + x for x in bss]

# >>> interpretaciones(p3)
# [[('A', False), ('B', False)],
#  [('A', False), ('B', True)],
#  [('A', True), ('B', False)],
#  [('A', True), ('B', True)]]
def interpretaciones(f: FProp) -> list[Interpretacion]:
    vs = list(set(variables(f)))
    return [list(zip(vs, i)) for i in interpretacionesVar(len(vs))]

# esTautologia(p1) == False
# esTautologia(p2) == True
# esTautologia(p3) == False
# esTautologia(p4) == True
def esTautologia(f: FProp) -> bool:
    return all((valor(i, f) for i in interpretaciones(f)))
