from src.union_conjuntista_de_listas import union1, union2, union3, union4


def test_union():
    assert sorted(union1([3, 2, 5], [5, 7, 3, 4])) == [2, 3, 4, 5, 7]
    assert sorted(union2([3, 2, 5], [5, 7, 3, 4])) == [2, 3, 4, 5, 7]
    assert sorted(union3([3, 2, 5], [5, 7, 3, 4])) == [2, 3, 4, 5, 7]
    assert sorted(union4([3, 2, 5], [5, 7, 3, 4])) == [2, 3, 4, 5, 7]
