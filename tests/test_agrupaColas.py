from src.agrupaColas import \
    (agrupaColas1, agrupaColas2, vacia, inserta)

def test_agrupaColas() -> None:
    ej1 = inserta(2, inserta(5, vacia()))
    ej2 = inserta(3, inserta(7, inserta(4, vacia())))
    ej3 = inserta(9, inserta(0, inserta(1, inserta(6, vacia()))))
    for agrupaColas in [agrupaColas1, agrupaColas2]:
        assert str(agrupaColas([ej1]))\
            == "5 | 2"
        assert str(agrupaColas([ej1, ej2]))\
            == "5 | 4 | 2 | 7 | 3"
        assert str(agrupaColas([ej1, ej2, ej3]))\
            == "5 | 6 | 4 | 1 | 2 | 0 | 7 | 9 | 3"
