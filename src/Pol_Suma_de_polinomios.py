# Pol_Suma_de_polinomios.py
# TAD de los polinomios: Suma de polinomios.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 26-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu),
# definir la función
#    sumaPol : (Polinomio[A], Polinomio[A]) -> Polinomio[A]
# tal que sumaPol(p, q) es la suma de los polinomios p y q. Por ejemplo,
#    >>> ejPol1 = consPol(4, 3, consPol(2, -5, consPol(0, 3, polCero())))
#    >>> ejPol2 = consPol(5, 1, consPol(2, 5, consPol(1, 4, polCero())))
#    >>> ejPol1
#    3*x^4 + -5*x^2 + 3
#    >>> ejPol2
#    x^5 + 5*x^2 + 4*x
#    >>> sumaPol(ejPol1, ejPol2)
#    x^5 + 3*x^4 + 4*x + 3
#
# Comprobar con Hypothesis las siguientes propiedades:
# + polCero es el elemento neutro de la suma.
# + la suma es conmutativa.
# ---------------------------------------------------------------------

# pylint: disable=arguments-out-of-order

from typing import TypeVar

from hypothesis import given

from src.TAD.Polinomio import (Polinomio, coefLider, consPol, esPolCero, grado,
                               polCero, polinomioAleatorio, restoPol)

A = TypeVar('A', int, float, complex)

# 1ª solución
# ===========

def sumaPol(p: Polinomio[A], q: Polinomio[A]) -> Polinomio[A]:
    if esPolCero(p):
        return q
    if esPolCero(q):
        return p
    n1, a1, r1 = grado(p), coefLider(p), restoPol(p)
    n2, a2, r2 = grado(q), coefLider(q), restoPol(q)
    if n1 > n2:
        return consPol(n1, a1, sumaPol(r1, q))
    if n1 < n2:
        return consPol(n2, a2, sumaPol(p, r2))
    return consPol(n1, a1 + a2, sumaPol(r1, r2))

# 2ª solución
# ===========

def sumaPol2(p: Polinomio[A], q: Polinomio[A]) -> Polinomio[A]:
    if p.esPolCero():
        return q
    if q.esPolCero():
        return p
    n1, a1, r1 = p.grado(), p.coefLider(), p.restoPol()
    n2, a2, r2 = q.grado(), q.coefLider(), q.restoPol()
    if n1 > n2:
        return sumaPol(r1, q).consPol(n1, a1)
    if n1 < n2:
        return sumaPol(p, r2).consPol(n2, a2)
    return sumaPol(r1, r2).consPol(n1, a1 + a2)

# Equivalencia de las definiciones
# ================================

# La propiedad es
@given(p=polinomioAleatorio(), q=polinomioAleatorio())
def test_sumaPol(p: Polinomio[int], q: Polinomio[int]) -> None:
    assert sumaPol(p, q) == sumaPol2(p,q)

# Propiedad. El polinomio cero es el elemento neutro de la suma.
@given(p=polinomioAleatorio())
def test_neutroSumaPol(p: Polinomio[int]) -> None:
    assert sumaPol(polCero(), p) == p
    assert sumaPol(p, polCero()) == p

# -- Propiedad. La suma es conmutativa.
@given(p=polinomioAleatorio(), q=polinomioAleatorio())
def test_conmutativaSuma(p: Polinomio[int], q: Polinomio[int]) -> None:
    assert sumaPol(p, q) == sumaPol(q, p)

# La comprobación es
#    > poetry run pytest -v Pol_Suma_de_polinomios.py
#    test_sumaPol PASSED
#    test_neutroSumaPol PASSED
#    test_conmutativaSuma PASSED
