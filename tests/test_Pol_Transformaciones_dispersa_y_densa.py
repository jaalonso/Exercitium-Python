from src.Pol_Transformaciones_dispersa_y_densa import (densaAdispersa,
                                                       densaAdispersa2,
                                                       densaAdispersa3,
                                                       dispersaAdensa,
                                                       dispersaAdensa2,
                                                       dispersaAdensa3)


def test_Transformaciones_dispersa_y_densa() -> None:
    for densaAdispersa_ in [densaAdispersa, densaAdispersa2,
                            densaAdispersa3]:
        assert densaAdispersa_([9, 0, 0, 5, 0, 4, 7])\
            == [(6, 9), (3, 5), (1, 4), (0, 7)]
    for dispersaAdensa_ in [dispersaAdensa, dispersaAdensa2,
                            dispersaAdensa3]:
        assert dispersaAdensa_([(6,9),(3,5),(1,4),(0,7)])\
            == [9, 0, 0, 5, 0, 4, 7]
