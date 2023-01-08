from src.base_de_dato_de_actividades import (musicos, musicos2, nombres,
                                             personas, seleccion, vivas)


def test_base_de_datos() -> None:
    assert nombres(personas) == [
        'Cervantes', 'Velazquez', 'Picasso', 'Beethoven', 'Poincare',
        'Quevedo', 'Goya', 'Einstein', 'Mozart', 'Botticelli',
        'Borromini', 'Bach']
    assert musicos(personas) == ['Beethoven', 'Mozart', 'Bach']
    assert seleccion(personas, 'Pintura') == [
        'Velazquez', 'Picasso', 'Goya', 'Botticelli']
    assert seleccion(personas, 'Musica') == [
        'Beethoven', 'Mozart', 'Bach']
    assert musicos2(personas) == ['Beethoven', 'Mozart', 'Bach']
    assert vivas(personas, 1600) == [
        'Cervantes', 'Velazquez', 'Quevedo', 'Borromini']
