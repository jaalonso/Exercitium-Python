from src.TAD_Conjunto_unitario import unitario


def test_unitario() -> None:
    assert str(unitario(5)) == "{5}"
