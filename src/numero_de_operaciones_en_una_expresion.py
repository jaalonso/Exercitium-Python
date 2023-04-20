# numero_de_operaciones_en_una_expresion.hs
# El tipo de las expresiones aritméticas: Número de operaciones en una expresión.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 14-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las expresiones aritméticas](https://bit.ly/40vCQUh),
# definir la función
#    numeroOps :: Expr -> Int
# tal que (numeroOps e) es el número de operaciones de e. Por ejemplo,
#    numeroOps(Lit(3))                   == 0
#    numeroOps(Suma(Lit(7), Op(Lit(5)))) == 2
# ---------------------------------------------------------------------

from src.tipo_expresion_aritmetica import Expr, Lit, Op, SiCero, Suma


def numeroOps(e: Expr) -> int:
    match e:
        case Lit(_):
            return 0
        case Suma(x, y):
            return 1 + numeroOps(x) + numeroOps(y)
        case Op(x):
            return 1 + numeroOps(x)
        case SiCero(x, y, z):
            return 1 + numeroOps(x) + numeroOps(y) + numeroOps(z)
    assert False
