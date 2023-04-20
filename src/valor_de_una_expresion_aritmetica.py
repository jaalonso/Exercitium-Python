# valor_de_una_expresion_aritmetica.py
# El tipo de las expresiones aritméticas: Valor_de_una_expresión.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 12-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo de las expresiones aritméticas](https://bit.ly/40vCQUh),
# definir la función
#    valor : (Expr) -> int
# tal que valor(e) es el valor de la expresión e (donde el valor de
# (SiCero e e1 e2) es el valor de e1 si el valor de e es cero y el es
# el valor de e2, en caso contrario). Por ejemplo,
#    valor(Op(Suma(Lit(3), Lit(5))))       == -8
#    valor(SiCero(Lit(0), Lit(4), Lit(5))) == 4
#    valor(SiCero(Lit(1), Lit(4), Lit(5))) == 5
# ---------------------------------------------------------------------

from src.tipo_expresion_aritmetica import Expr, Lit, Op, SiCero, Suma

# 1ª solución
# ===========

def valor(e: Expr) -> int:
    match e:
        case Lit(n):
            return n
        case Suma(x, y):
            return valor(x) + valor(y)
        case Op(x):
            return -valor(x)
        case SiCero(x, y, z):
            return valor(y) if valor(x) == 0 else valor(z)
    assert False

# 2ª solución
# ===========

def valor2(e: Expr) -> int:
    if isinstance(e, Lit):
        return e.x
    if isinstance(e, Suma):
        return valor2(e.x) + valor2(e.y)
    if isinstance(e, Op):
        return -valor2(e.x)
    if isinstance(e, SiCero):
        if valor2(e.x) == 0:
            return valor2(e.y)
        return valor2(e.z)
    assert False
