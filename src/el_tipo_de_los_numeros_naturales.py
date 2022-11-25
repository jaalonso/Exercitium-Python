# el_tipo_de_los_numeros_naturales.py
# El tipo de los números naturales.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 25-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# El tipo de los números raturales se puede definir por
#    @dataclass
#    class Nat:
#        pass
#
#    @dataclass
#    class Cero(Nat):
#        pass
#
#    @dataclass
#    class Suc(Nat):
#        n: Nat
# de forma que Suc(Suc(Suc(Cero()))) representa el número 3.
#
# Definir las siguientes funciones
#    nat2int : (Nat) -> int
#    int2nat : (int) -> Nat
#    suma    : (Nat, Nat) -> Nat
# tales que
# + nat2int(n) es el número entero correspondiente al número natural
#   n. Por ejemplo,
#      nat2int(Suc(Suc(Suc(Cero())))) == 3
# + int2nat(n) es el número natural correspondiente al número entero
#   n. Por ejemplo,
#      int2nat(3) == Suc(Suc(Suc(Cero())))
# + suma(m, n) es la suma de los número naturales m y n. Por ejemplo,
#      >>> suma(Suc(Suc(Cero())), Suc(Cero()))
#      Suc(Suc(Suc(Cero())))
#      >>> nat2int(suma(Suc(Suc(Cero())), Suc(Cero())))
#      3
#      >>> nat2int(suma(int2nat(2), int2nat(1)))
#      3
# ---------------------------------------------------------------------

from dataclasses import dataclass

@dataclass
class Nat:
    pass

@dataclass
class Cero(Nat):
    pass

@dataclass
class Suc(Nat):
    n: Nat

def nat2int(n: Nat) -> int:
    match n:
        case Cero():
            return 0
        case Suc(n):
            return 1 + nat2int(n)
    assert False

def int2nat(n: int) -> Nat:
    if n == 0:
        return Cero()
    return Suc(int2nat(n - 1))

def suma(m: Nat, n: Nat) -> Nat:
    match m:
        case Cero():
            return n
        case Suc(m):
            return Suc(suma(m, n))
    assert False

# suma :: Nat -> Nat -> Nat
# suma Cero    n = n
# suma (Suc m) n = Suc (suma m n)
