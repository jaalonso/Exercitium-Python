# Metodo_de_Heron_para_calcular_la_raiz_cuadrada.py
# Método de Herón para calcular la raíz_cuadrada.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 29-octubre-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El método de Herón para calcular la raíz cuadrada de un número se
# basa en las siguientes propiedades:
# + Si y es una aproximación de la raíz cuadrada de x, entonces
#   (y+x/y)/2 es una aproximación mejor.
# + El límite de la sucesión definida por
#       x_0     = 1
#       x_{n+1} = (x_n+x/x_n)/2
#   es la raíz cuadrada de x.
#
# Definir la función
#    raiz : (float) -> float
# tal que raiz(x) es la raíz cuadrada de x calculada usando la
# propiedad anterior con una aproximación de 0.00001 y tomando como
# valor inicial 1. Por ejemplo,
#    raiz(9)  ==  3.000000001396984
# ---------------------------------------------------------------------

# 1ª solución
# ===========

def raiz(x : float) -> float:
    def aceptable(y: float) -> bool:
        return abs(y*y-x) < 0.00001
    def mejora(y: float) -> float:
        return 0.5*(y+x/y)
    def raizAux(y: float) -> float:
        if aceptable(y):
            return y
        return raizAux(mejora(y))
    return raizAux(1)

# 2ª solución
# ===========

def raiz2(x: float) -> float:
    def aceptable(y: float) -> bool:
        return abs(y*y-x) < 0.00001
    def mejora(y: float) -> float:
        return 0.5*(y+x/y)
    y = 1.0
    while not aceptable(y):
        y = mejora(y)
    return y

# Verificación
# ============

def test_raiz() -> None:
    assert raiz(9)  ==  3.000000001396984
    assert raiz2(9)  ==  3.000000001396984
    print("Verificado")

# La verificación es
#    >>> test_raiz()
#    Verificado
