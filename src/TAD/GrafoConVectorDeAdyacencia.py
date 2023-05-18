# GrafoConVectorDeAdyacencia.py
# Representación del TAD grafo mediante vectores de adyacencia.
# José A. Alonso Jiménez <https://jaalonso.github.io>
# Sevilla, 15-mayo-2023
# ---------------------------------------------------------------------

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Grafo:
    orientacion: bool
    cotas: tuple[int, int]
    aristas: list[tuple[int, int, float]]

#    def dirigido(self) -> bool:
#        return self.orientacion
#
#    def nodos(self) -> list[int]:
#        cota_inicial, cota_final = self.cotas
#        return list(range(cota_inicial, 1 + cota_final))
#
#    def nodos2(self) -> list[int]:
#        nodos = []
#        for v1, v2, _ in self.aristas:
#            if v1 not in nodos:
#                nodos.append(v1)
#            if v2 not in nodos:
#                nodos.append(v2)
#        return sorted(nodos)
#
#    def adyacentes(self, vertice: int) -> list[int]:
#        adyacentes = []
#        for v1, v2, _ in self.aristas:
#            if v1 == vertice:
#                adyacentes.append(v2)
#            elif v2 == vertice and not self.orientacion:
#                adyacentes.append(v1)
#        return adyacentes
#
#    def obtener_aristas(self) -> list[tuple[int, int, float]]:
#        return self.aristas
#
#    def aristaEn(self, arista: tuple[int, int]) -> bool:
#        for v1, v2, _ in self.aristas:
#            if arista in ((v1, v2), (v2, v1)):
#                return True
#        return False
#
#    def peso(self, v1: int, v2: int) -> float:
#        for vertice1, vertice2, peso in self.aristas:
#            if (vertice1, vertice2) == (v1, v2) or (vertice2, vertice1) == (v1, v2):
#                return peso
#        raise ValueError("No se encontró una arista entre los vértices especificados.")

def creaGrafo(o: bool,
              cs: tuple[int, int],
              as_: list[tuple[int, int, float]]) -> Grafo:
    return Grafo(orientacion=o, cotas=cs, aristas=as_)

ejGrafo2 = creaGrafo(False,
                     (1, 5),
                     [(1,2,12),(1,3,34),(1,5,78),
                      (2,4,55),(2,5,32),
                      (3,4,61),(3,5,44),
                      (4,5,93)])

# ejGrafoND es el grafo
#             12
#        1 -------- 2
#        | \78     /|
#        |  \   32/ |
#        |   \   /  |
#      34|     5    |55
#        |   /   \  |
#        |  /44   \ |
#        | /     93\|
#        3 -------- 4
#             61
# representado mediante un vector de adyacencia; es decir,
#    λ> ejGrafoND
#    G ND array (1,5) [(1,[(2,12),(3,34),(5,78)]),
#                      (2,[(1,12),(4,55),(5,32)]),
#                      (3,[(1,34),(4,61),(5,44)]),
#                      (4,[(2,55),(3,61),(5,93)]),
#                      (5,[(1,78),(2,32),(3,44),(4,93)])])
ejGrafoND: Grafo = creaGrafo(False,
                             (1, 5),
                             [(1, 2, 12), (1, 3, 34), (1, 5, 78),
                              (2, 4, 55), (2, 5, 32),
                              (3, 4, 61), (3, 5, 44),
                              (4, 5, 93)])

# ejGrafoD es el mismo grafo que ejGrafoND pero orientando las aristas;
# es decir,
#    λ> ejGrafoD
#    G D array (1,5) [(1,[(2,12),(3,34),(5,78)]),
#                     (2,[(4,55),(5,32)]),
#                     (3,[(4,61),(5,44)]),
#                     (4,[(5,93)]),
#                     (5,[])])
ejGrafoD: Grafo = creaGrafo(True,
                            (1, 5),
                            [(1, 2, 12), (1, 3, 34), (1, 5, 78),
                             (2, 4, 55), (2, 5, 32),
                             (3, 4, 61), (3, 5, 44),
                             (4, 5, 93)])

#    >>> ejGrafoND.nodos()
#    [1, 2, 3, 4, 5]
#    >>> ejGrafoD.nodos()
#    [1, 2, 3, 4, 5]
