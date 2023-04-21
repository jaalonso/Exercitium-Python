# validez_de_una_formula.py
# Reconocedor de tautologías.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 05-diciembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Una fórmula es una tautología si es verdadera en todas sus
# interpretaciones. Por ejemplo,
# + (A ∧ B) → A es una tautología
# + A → (A ∧ B) no es una tautología
#
# Usando el [tipo de las fórmulas proposicionales](https://bit.ly/3L3G2SX),
# definir la función
#    esTautologia :: FProp -> Bool
# tal que (esTautologia p) se verifica si la fórmula p es una
# tautología. Por ejemplo,
#    >>> esTautologia(Impl(Conj(Var('A'), Var ('B')), Var('A')))
#    True
#    >>> esTautologia(Impl(Var('A'), Conj(Var('A'), Var('B'))))
#    False
# ---------------------------------------------------------------------

# pylint: disable=unused-import

from src.interpretaciones_de_una_formula import interpretaciones
from src.tipo_de_formulas import Conj, Const, FProp, Impl, Neg, Var
from src.valor_de_una_formula import valor


def esTautologia(p: FProp) -> bool:
    return all((valor(i, p) for i in interpretaciones(p)))
