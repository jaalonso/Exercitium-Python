from src.maximo_de_una_lista import maximo1, maximo2, maximo3


def test_maximo() -> None:
    for maximo in [maximo1, maximo2, maximo3]:
        assert maximo([3, 7, 2, 5]) == 7
        assert maximo(["todo", "es", "falso"]) == "todo"
        assert maximo(["menos", "alguna", "cosa"]) == "menos"
