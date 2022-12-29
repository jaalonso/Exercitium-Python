from src.valor_de_un_arbol_booleano import \
    ej1, ej2, valor

def test_valor() -> None:
    assert valor(ej1) is True
    assert valor(ej2) is False
