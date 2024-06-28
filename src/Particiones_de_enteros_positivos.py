# Particiones_de_enteros_positivos.py
# Particiones de enteros positivos.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 19-junio-2024
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Una [partición)(http://bit.ly/1KtLkNZ) de un entero positivo n es una
# manera de escribir n como una suma de enteros positivos. Dos sumas
# que sólo difieren en el orden de sus sumandos se consideran la misma
# partición. Por ejemplo, 4 tiene cinco particiones: 4, 3+1, 2+2, 2+1+1
# y 1+1+1+1.
#
# Definir la función
#    particiones : (int) -> list[list[int]]
# tal que particiones(n) es la lista de las particiones del número
# n. Por ejemplo,
#    particiones(4)  ==  [[4],[3,1],[2,2],[2,1,1],[1,1,1,1]]
#    particiones(5)  ==  [[5],[4,1],[3,2],[3,1,1],[2,2,1],[2,1,1,1],[1,1,1,1,1]]
#    length (particiones 50)  ==  204226
# ---------------------------------------------------------------------

from timeit import Timer, default_timer

# 1ª solución
# ===========

def particiones1(n: int) -> list[list[int]]:
    if n == 0:
        return [[]]
    return [[x] + y
            for x in range(n, 0, -1)
            for y in particiones1(n - x)
            if not y or x >= y[0]]

# 2ª solución
# ===========

def particiones2(n: int) -> list[list[int]]:
    def particiones(m: int, aux: list[list[list[int]]]) -> list[list[int]]:
        return [[m]] + [
            [x] + p
            for x in range(m, 0, -1)
            for p in aux[m - x]
            if p and x >= p[0]
        ]
    aux: list[list[list[int]]] = [[]]
    for i in range(1, n + 1):
        aux.append(particiones(i, aux))
    return aux[n]

# Verificación
# ============

def test_particiones() -> None:
    for particiones in [particiones1,
                        particiones2]:
        assert particiones(4) ==\
            [[4],[3,1],[2,2],[2,1,1],[1,1,1,1]]
        assert particiones(5) ==\
            [[5],[4,1],[3,2],[3,1,1],[2,2,1],[2,1,1,1],[1,1,1,1,1]]
    print("Verificado")

# La verificación es
#    >>> test_particiones()
#    Verificado

# Comprobación de equivalencia
# ============================

# La propiedad es
def test_particiones_equiv(n: int) -> bool:
    return [particiones1(k) for k in range(1, n)]  ==\
           [particiones2(k) for k in range(1, n)]

# La comprobación es
#    >>> test_particiones_equiv(20)
#    True

# Comparación de eficiencia                                        --
# =========================

def tiempo(e: str) -> None:
    """Tiempo (en segundos) de evaluar la expresión e."""
    t = Timer(e, "", default_timer, globals()).timeit(1)
    print(f"{t:0.2f} segundos")

# La comparación es
#    >>> tiempo('particiones1(23)')
#    4.00 segundos
#    >>> tiempo('particiones2(23)')
#    0.01 segundos
