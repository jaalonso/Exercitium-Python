# expresion_aritmetica_con_variables.py
# El tipo de las expresiones aritméticas con variables
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 11-enero-2023.
# ---------------------------------------------------------------------

# La expresión 2*(a+5) puede representarse por
#    P(C(2), S(V('a'), C(5)))
# usando el tipo de las expresiones aritméticas con variables definido
# como se muestra a continuación.

from dataclasses import dataclass


@dataclass
class Expr:
    pass

@dataclass
class C(Expr):
    x: int

@dataclass
class V(Expr):
    x: str

@dataclass
class S(Expr):
    x: Expr
    y: Expr

@dataclass
class P(Expr):
    x: Expr
    y: Expr
