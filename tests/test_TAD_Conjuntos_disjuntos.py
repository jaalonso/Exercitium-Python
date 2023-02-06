from src.TAD_Conjuntos_disjuntos import \
    (disjuntos, disjuntos2, disjuntos3, disjuntos4, disjuntos5, inserta,
     vacio)

def test_disjuntos() -> None:
    ej1 = inserta(2, inserta(5, vacio()))
    ej2 = inserta(4, inserta(3, vacio()))
    ej3 = inserta(5, inserta(3, vacio()))
    for disjuntos_ in [disjuntos, disjuntos2, disjuntos3, disjuntos4,
                       disjuntos5]:
        assert disjuntos_(ej1, ej2)
        assert not disjuntos_(ej1, ej3)
