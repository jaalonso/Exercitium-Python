# expresion_aritmetica_basica.py
# Expresión aritmética básica.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 5-enero-2023
# ---------------------------------------------------------------------

# La expresión aritmética 2*(3+7) se representa por
#    P(C(2), S(C(3), C(7)))
# usando el tipo de dato definido a continuación.

from dataclasses import dataclass


@dataclass
class Expr:
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
