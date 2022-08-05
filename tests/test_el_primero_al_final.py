from src.el_primero_al_final import rota1


def test_rota1():
    assert rota1([3, 2, 5, 7]) == [2, 5, 7, 3]
    assert rota1(['a', 'b', 'c']) == ['b', 'c', 'a']
