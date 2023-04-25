# Pol_Derivada_de_un_polinomio.py
# TAD de los polinomios: Derivada de un polinomio.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 2-mayo-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Usando el [tipo abstracto de los polinomios](https://bit.ly/3KwqXYu),
# definir la función
#    derivada :: (Eq a, Num a) => Polinomio a -> Polinomio a
# tal que (derivada p) es la derivada del polinomio p. Por ejemplo,
#    >>> ejPol = consPol(5, 1, consPol(2, 5, consPol(1, 4, polCero())))
#    >>> ejPol
#    x^5 + 5*x^2 + 4*x
#    >>> derivada(ejPol)
#    5*x^4 + 10*x + 4
# ---------------------------------------------------------------------

from typing import TypeVar

from hypothesis import given

from src.Pol_Suma_de_polinomios import sumaPol
from src.TAD.Polinomio import (Polinomio, coefLider, consPol, grado, polCero,
                               polinomioAleatorio, restoPol)

A = TypeVar('A', int, float, complex)


def derivada(p: Polinomio[A]) -> Polinomio[A]:
    n = grado(p)
    if n == 0:
        return polCero()
    b = coefLider(p)
    r = restoPol(p)
    return consPol(n - 1, b * n, derivada(r))

# Propiedad. La derivada de la suma es la suma de las derivadas.
@given(p=polinomioAleatorio(), q=polinomioAleatorio())
def test_derivada(p: Polinomio[int], q: Polinomio[int]) -> None:
    assert derivada(sumaPol(p, q)) == sumaPol(derivada(p), derivada(q))

# La comprobación es
#    > poetry run pytest -q Pol_Derivada_de_un_polinomio.py
#    1 passed in 0.46s
