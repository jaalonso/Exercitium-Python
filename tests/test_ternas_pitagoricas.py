from src.ternas_pitagoricas import pitagoricas1, pitagoricas2, pitagoricas3


def test_pitagoricas() -> None:
    for pitagoricas in [pitagoricas1, pitagoricas2, pitagoricas3]:
        assert pitagoricas(10) == [(3, 4, 5), (6, 8, 10)]
        assert pitagoricas(15) == [(3, 4, 5), (5, 12, 13),
                                   (6, 8, 10), (9, 12, 15)]
