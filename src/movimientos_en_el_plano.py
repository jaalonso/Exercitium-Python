# movimientos_en_el_plano.py
# Movimientos en el plano.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 23-noviembre-2022
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Se consideran el tipo de las posiciones del plano definido por
#    Posicion = tuple[int, int]
# y el tipo de las direcciones definido por
#    Direccion = Enum('Direccion', ['Izquierda', 'Derecha', 'Arriba', 'Abajo'])
# Definir las siguientes funciones
#    opuesta     : (Direccion) -> Direccion
#    movimiento  : (Posicion, Direccion) -> Posicion
#    movimientos : (Posicion, list[Direccion]) -> Posicion
# tales que
# + opuesta(d) es la dirección opuesta de d. Por ejemplo,
#      opuesta1(Direccion.Izquierda) == Direccion.Derecha
# + movimiento(p d) es la posición reultante de moverse, desde la
#   posición p, un paso en la dirección d . Por ejemplo,
#      movimiento1((2, 5), Direccion.Arriba)          == (2, 6)
#      movimiento1((2, 5), opuesta1(Direccion.Abajo)) == (2, 6)
# + movimientos(p, ds) es la posición obtenida aplicando la lista de
#   movimientos según las direcciones de ds a la posición p. Por
#   ejemplo,
#     >>> movimientos1((2, 5), [Direccion.Arriba, Direccion.Izquierda])
#     (1, 6)
# ---------------------------------------------------------------------

from enum import Enum
from functools import reduce

Posicion = tuple[int, int]

Direccion = Enum('Direccion', ['Izquierda', 'Derecha', 'Arriba', 'Abajo'])

# 1ª definición de opuesta
# ========================

def opuesta1(d: Direccion) -> Direccion:
    if d == Direccion.Izquierda:
        return Direccion.Derecha
    if d == Direccion.Derecha:
        return Direccion.Izquierda
    if d == Direccion.Arriba:
        return Direccion.Abajo
    if d == Direccion.Abajo:
        return Direccion.Arriba
    assert False

# 2ª definición de opuesta
# ========================

def opuesta2(d: Direccion) -> Direccion:
    match d:
        case Direccion.Izquierda:
            return Direccion.Derecha
        case Direccion.Derecha:
            return Direccion.Izquierda
        case Direccion.Arriba:
            return Direccion.Abajo
        case Direccion.Abajo:
            return Direccion.Arriba
    assert False

# 1ª definición de movimiento
# ===========================

def movimiento1(p: Posicion, d: Direccion) -> Posicion:
    (x, y) = p
    if d == Direccion.Izquierda:
        return (x - 1, y)
    if d == Direccion.Derecha:
        return (x + 1, y)
    if d == Direccion.Arriba:
        return (x, y + 1)
    if d == Direccion.Abajo:
        return (x, y - 1)
    assert False

# 2ª definición de movimiento
# ===========================

def movimiento2(p: Posicion, d: Direccion) -> Posicion:
    (x, y) = p
    match d:
        case Direccion.Izquierda:
            return (x - 1, y)
        case Direccion.Derecha:
            return (x + 1, y)
        case Direccion.Arriba:
            return (x, y + 1)
        case Direccion.Abajo:
            return (x, y - 1)
    assert False

# 1ª definición de movimientos
# ============================

def movimientos1(p: Posicion, ds: list[Direccion]) -> Posicion:
    if not ds:
        return p
    return movimientos1(movimiento1(p, ds[0]), ds[1:])

# 2ª definición de movimientos
# ============================

def movimientos2(p: Posicion, ds: list[Direccion]) -> Posicion:
    return reduce(movimiento1, ds, p)
