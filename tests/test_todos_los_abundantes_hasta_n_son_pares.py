from src.todos_los_abundantes_hasta_n_son_pares import (todosPares1,
                                                        todosPares2,
                                                        todosPares3)


def test_todosPares() -> None:
    assert todosPares1(10)
    assert todosPares1(100)
    assert not todosPares1(1000)
    assert todosPares2(10)
    assert todosPares2(100)
    assert not todosPares2(1000)
    assert todosPares3(10)
    assert todosPares3(100)
    assert not todosPares3(1000)
