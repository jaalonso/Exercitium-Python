# Pol_Producto_polinomios.py
# TAD de los polinomios: Producto de polinomios.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 27-abril-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu),
# definir la función
#    multPol : (Polinomio[A], Polinomio[A]) -> Polinomio[A]
# tal que multPol(p, q) es el producto de los polinomios p y q. Por
# ejemplo,
#    >>> ejPol1 = consPol(4, 3, consPol(2, -5, consPol(0, 3, polCero())))
#    >>> ejPol2 = consPol(5, 1, consPol(2, 5, consPol(1, 4, polCero())))
#    >>> ejPol1
#    3*x^4 + -5*x^2 + 3
#    >>> ejPol2
#    x^5 + 5*x^2 + 4*x
#    >>> multPol(ejPol1, ejPol2)
#    3*x^9 + -5*x^7 + 15*x^6 + 15*x^5 + -25*x^4 + -20*x^3 + 15*x^2 + 12*x
#
# Comprobar con Hypothesis las siguientes propiedades
# + El producto de polinomios es conmutativo.
# + El producto es distributivo respecto de la suma.
# ---------------------------------------------------------------------

# pylint: disable=arguments-out-of-order

from typing import TypeVar

from hypothesis import given

from src.Pol_Suma_de_polinomios import sumaPol
from src.Pol_Termino_lider import termLider
from src.TAD.Polinomio import (Polinomio, coefLider, consPol, esPolCero, grado,
                               polCero, polinomioAleatorio, restoPol)

A = TypeVar('A', int, float, complex)

# multPorTerm(t, p) es el producto del término t por el polinomio
# p. Por ejemplo,
#    ejTerm                     ==  4*x
#    ejPol2                     ==  x^5 + 5*x^2 + 4*x
#    multPorTerm ejTerm ejPol2  ==  4*x^6 + 20*x^3 + 16*x^2
def multPorTerm(term: Polinomio[A], pol: Polinomio[A]) -> Polinomio[A]:
    n = grado(term)
    a = coefLider(term)
    m = grado(pol)
    b = coefLider(pol)
    r = restoPol(pol)
    if esPolCero(pol):
        return polCero()
    return consPol(n + m, a * b, multPorTerm(term, r))

def multPol(p: Polinomio[A], q: Polinomio[A]) -> Polinomio[A]:
    if esPolCero(p):
        return polCero()
    return sumaPol(multPorTerm(termLider(p), q),
                   multPol(restoPol(p), q))

# El producto de polinomios es conmutativo.
@given(p=polinomioAleatorio(),
       q=polinomioAleatorio())
def test_conmutativaProducto(p: Polinomio[int], q: Polinomio[int]) -> None:
    assert multPol(p, q) == multPol(q, p)

# El producto es distributivo respecto de la suma.
@given(p=polinomioAleatorio(),
       q=polinomioAleatorio(),
       r=polinomioAleatorio())
def test_distributivaProductoSuma(p: Polinomio[int],
                                  q: Polinomio[int],
                                  r: Polinomio[int]) -> None:
    assert multPol(p, sumaPol(q, r)) == sumaPol(multPol(p, q), multPol(p, r))

# La comprobación es
#    > poetry run pytest -v Pol_Producto_polinomios.py
#    test_conmutativaProducto PASSED
#    test_distributivaProductoSuma PASSED
