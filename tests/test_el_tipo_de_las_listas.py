from src.el_tipo_de_las_listas import Cons, Nil, longitud


def test_longitud() -> None:
    assert longitud(Cons(4, Cons(2, Cons(5, Nil())))) == 3
