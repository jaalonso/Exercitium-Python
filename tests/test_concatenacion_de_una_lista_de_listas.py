from src.concatenacion_de_una_lista_de_listas import \
    conc1, conc2, conc3, conc4

def test_conc() -> None:
    for conc in [conc1, conc2, conc3, conc4]:
        assert conc([[1, 3], [2, 4, 6], [1, 9]]) == [1, 3, 2, 4, 6, 1, 9]
