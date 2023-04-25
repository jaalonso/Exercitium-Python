from src.arboles_binarios import H, N
from src.pertenencia_de_un_elemento_a_un_arbol import pertenece


def test_pertenece() -> None:
    assert pertenece(4, N(5, N(3, H(1), H(4)), N(7, H(6), (H(9)))))
    assert not pertenece(0, N(5, N(3, H(1), H(4)), N(7, H(6), (H(9)))))
