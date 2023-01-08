from src.ternas_pitagoricas_con_suma_dada import (ternasPitagoricas1,
                                                  ternasPitagoricas2,
                                                  ternasPitagoricas3)


def test_ternasPitagoricas() -> None:
    for ternasPitagoricas in [ternasPitagoricas1, ternasPitagoricas2,
                              ternasPitagoricas3]:
        assert ternasPitagoricas(12) == [(3, 4, 5)]
        assert set(ternasPitagoricas(60)) == set([(10, 24, 26), (15, 20, 25)])
