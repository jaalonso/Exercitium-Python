from src.aplanamiento_de_un_arbol import aplana
from src.arboles_binarios import H, N


def test_aplana() -> None:
    assert aplana (N(5, N(3, H(1), H(4)), N(7, H(6), (H(9)))))\
        == [1, 3, 4, 5, 6, 7, 9]
