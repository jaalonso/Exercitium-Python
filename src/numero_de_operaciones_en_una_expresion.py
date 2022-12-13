# numero_de_operaciones_en_una_expresion.hs
# El tipo de las expresiones aritméticas: Número de operaciones en una expresión.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 14-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Se considera el tipo de las expresiones aritméticas definido por
#    @dataclass
#    class Expr:
#        pass
#
#    @dataclass
#    class Lit(Expr):
#        x: int
#
#    @dataclass
#    class Suma(Expr):
#        x: Expr
#        y: Expr
#
#    @dataclass
#    class Op(Expr):
#        x: Expr
#
#    @dataclass
#    class SiCero(Expr):
#        x: Expr
#        y: Expr
#        z: Expr
#
# formado por
# + literales (p.e. Lit 7),
# + sumas (p.e. Suma (Lit 7) (Suma (Lit 3) (Lit 5)))
# + opuestos (p.e. Op (Suma (Op (Lit 7)) (Suma (Lit 3) (Lit 5))))
# + expresiones condicionales (p.e. (SiCero (Lit 3) (Lit 4) (Lit 5))
#
# Definir la función
#    numeroOps :: Expr -> Int
# tal que (numeroOps e) es el número de operaciones de e. Por ejemplo,
#    numeroOps(Lit(3))                   == 0
#    numeroOps(Suma(Lit(7), Op(Lit(5)))) == 2
# ---------------------------------------------------------------------

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

def numeroOps(e: Expr) -> int:
    match e:
        case Lit(n):
            return 0
        case Suma(x, y):
            return 1 + numeroOps(x) + numeroOps(y)
        case Op(x):
            return 1 + numeroOps(x)
        case SiCero(x, y, z):
            return 1 + numeroOps(x) + numeroOps(y) + numeroOps(z)
    assert False
