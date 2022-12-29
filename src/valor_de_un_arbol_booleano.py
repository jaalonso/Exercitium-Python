# valor_de_un_arbol_booleano.py
# Valor de un árbol booleano.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 4-enero-2023
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Se consideran los árboles con operaciones booleanas definidos por
#    @dataclass
#    class Arbol:
#        pass
#
#    @dataclass
#    class H(Arbol):
#        x: bool
#
#    @dataclass
#    class Conj(Arbol):
#        i: Arbol
#        d: Arbol
#
#    @dataclass
#    class Disy(Arbol):
#        i: Arbol
#        d: Arbol
#
#    @dataclass
#    class Neg(Arbol):
#        a: Arbol
#
# Por ejemplo, los árboles
#                Conj                            Conj
#               /   \                           /   \
#              /     \                         /     \
#           Disy      Conj                  Disy      Conj
#          /   \       /  \                /   \      /   \
#       Conj    Neg   Neg True          Conj    Neg   Neg  True
#       /  \    |     |                 /  \    |     |
#    True False False False          True False True  False
#
# se definen por
#    ej1: Arbol = Conj(Disy(Conj(H(True), H(False)),
#                           (Neg(H(False)))),
#                      (Conj(Neg(H(False)),
#                            (H(True)))))
#
#    ej2: Arbol = Conj(Disy(Conj(H(True), H(False)),
#                           (Neg(H(True)))),
#                      (Conj(Neg(H(False)),
#                            (H(True)))))
#
# Definir la función
#    valor : (Arbol) -> bool
# tal que valor(a) es el resultado de procesar el árbol a realizando
# las operaciones booleanas especificadas en los nodos. Por ejemplo,
#    valor(ej1) == True
#    valor(ej2) == False
# ---------------------------------------------------------------------

from dataclasses import dataclass

@dataclass
class Arbol:
    pass

@dataclass
class H(Arbol):
    x: bool

@dataclass
class Conj(Arbol):
    i: Arbol
    d: Arbol

@dataclass
class Disy(Arbol):
    i: Arbol
    d: Arbol

@dataclass
class Neg(Arbol):
    a: Arbol

ej1: Arbol = Conj(Disy(Conj(H(True), H(False)),
                       (Neg(H(False)))),
                  (Conj(Neg(H(False)),
                        (H(True)))))

ej2: Arbol = Conj(Disy(Conj(H(True), H(False)),
                       (Neg(H(True)))),
                  (Conj(Neg(H(False)),
                        (H(True)))))

def valor(a: Arbol) -> bool:
    match a:
        case H(x):
            return x
        case Neg(b):
            return not valor(b)
        case Conj(i, d):
            return valor(i) and valor(d)
        case Disy(i, d):
            return valor(i) or valor(d)
    assert False
