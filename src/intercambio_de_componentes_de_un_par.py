# intercambio_de_componentes_de_un_par.py
# Intercambio de componentes de un par.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 5-septiembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Definir la función
#    intercambia : (tuple[A, B]) -> tuple[B, A]
# tal que intercambia(p)  es el punto obtenido intercambiando las
# coordenadas del punto p. Por ejemplo,
#    intercambia((2,5))  ==  (5,2)
#    intercambia((5,2))  ==  (2,5)
# ---------------------------------------------------------------------

def intercambia(p):
    (x, y) = p
    return (y, x)
