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


