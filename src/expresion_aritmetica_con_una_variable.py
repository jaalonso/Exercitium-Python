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
class Exp:
    pass

@dataclass
class X(Exp):
    pass

@dataclass
class C(Exp):
    x: int

@dataclass
class S(Exp):
    x: Exp
    y: Exp

@dataclass
class P(Exp):
    x: Exp
    y: Exp
