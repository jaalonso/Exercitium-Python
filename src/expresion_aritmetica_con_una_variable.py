# expresion_aritmetica_con_una_variable.py
# Tipo de expresiones aritméticas con una variable.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 9-enero-2023
# ---------------------------------------------------------------------

# La expresión X*(13+X) se representa por
#    P(X(), S(C(13), X()))
# usando el tipo de las expresiones aritméticas con una variable
# (denotada por X) que se define como se muestra a continuación,

from dataclasses import dataclass


@dataclass
class Expr:
    pass

@dataclass
class X(Expr):
    pass

@dataclass
class C(Expr):
    x: int

@dataclass
class S(Expr):
    x: Expr
    y: Expr

@dataclass
class P(Expr):
    x: Expr
    y: Expr
