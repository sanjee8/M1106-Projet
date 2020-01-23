####################################
#             PARTIE 1             #
####################################

def test_get_nb_empty_rooms():
    p = {'n': 4, 'nb_cases_libres': 6, 'tiles': [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0],
         'nombre_cases_libres': 5}
    p['nombre_cases_libres'] = 5
    n = get_nb_empty_rooms(p)  # n vaut 6
    assert n == 6
    print("ok pour get_nb_empty_rooms")
    
####################################
#             PARTIE 2             #
####################################
def test_get_next_alea_tiles():
    p = {'n': 4, 'nb_cases_libres': 6, 'tiles': [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0],
         'nombre_cases_libres': 5}
    test = get_next_alea_tiles(p, 'init')
    assert 1 in test is True
    test = get_next_alea_tiles(p, 'encours')
    assert 1 in test is False
    print("ok pour get_next_alea_tiles")

def test_put_next_tiles():
    tiles = {0: {'val': '10', 'lig': 1, 'col': 0}, 'check': True}
    p = {'n': 4, 'nb_cases_libres': 6, 'tiles': [6, 2, 3, 2, 0, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0],
         'nombre_cases_libres': 5}
    put_next_tiles(p,tiles)
    assert p == {'n': 4, 'nb_cases_libres': 6, 'tiles': [6, 2, 3, 2, 10, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 0],
         'nombre_cases_libres': 4}
    tiles = {0: {'val': '5', 'lig': 3, 'col': 3}, 'check': True}
    put_next_tiles(p,tiles)
    assert p == {'n': 4, 'nb_cases_libres': 6, 'tiles': [6, 2, 3, 2, 10, 2, 6, 2, 0, 2, 2, 0, 1, 0, 0, 5],
         'nombre_cases_libres': 4}
    print("ok pour put_next_tiles")

