# tipo_expresion_aritmetica.py
# El tipo de las expresiones aritméticas: Valor_de_una_expresión.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 12-diciembre-2022
# ---------------------------------------------------------------------

# El tipo de las expresiones aritméticas formadas por
# + literales (p.e. Lit 7),
# + sumas (p.e. Suma (Lit 7) (Suma (Lit 3) (Lit 5)))
# + opuestos (p.e. Op (Suma (Op (Lit 7)) (Suma (Lit 3) (Lit 5))))
# + expresiones condicionales (p.e. (SiCero (Lit 3) (Lit 4) (Lit 5))
# se define como se muestra a continuación.

from dataclasses import dataclass


@dataclass
class Expr:
    pass

@dataclass
class Lit(Expr):
    x: int

@dataclass
class Suma(Expr):
    x: Expr
    y: Expr

@dataclass
class Op(Expr):
    x: Expr

@dataclass
class SiCero(Expr):
    x: Expr
    y: Expr
    z: Expr
