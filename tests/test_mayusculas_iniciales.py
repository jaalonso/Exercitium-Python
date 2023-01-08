from src.mayusculas_iniciales import titulo1, titulo2, titulo3


def test_titulo() -> None:
    for titulo in [titulo1, titulo2, titulo3]:
        assert titulo(["eL", "arTE", "DE", "La", "proGraMacion"]) == \
            ["El", "Arte", "de", "la", "Programacion"]
