# tipo_de_formulas.py
# El tipo de las fórmulas proposicionales.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 30-noviembre-2022
# ======================================================================

# La fórmula A → ⊥ ∧ ¬B se representa por
#    Impl(Var('A'), Conj(Const(False), Neg (Var('B'))))
# usando el tipo de las fórmulas proposicionales definido como se
# muestra a continuación.

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
