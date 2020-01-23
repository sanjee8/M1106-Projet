def test_check_indice():
    p = init_play()
    assert check_indice(p,0) == True # Retourne True
    assert check_indice(p,10) == False # Retourne False
    assert check_indice(p,1) == True # Retourne True
    assert check_indice(p,45) == False # Retourne False
    assert check_indice(p,-9) == False # Retourne False
    print("ok pour check_indice")
    
def test_check_room():
    p = init_play()
    assert check_room(p,1,1) == True # Retourne True
    assert check_room(p,6,3) == False# Retourne False
    assert check_room(p,-10,5) == False # Retourne False
    assert check_room(p,3,3) == True # Retourne True
    print("ok pour check_room")
def test_get_value():
    p = {'n' : 4, 'nb_cases_libres' : 16, 'tiles' : [6,2,3,2,0,2,6,2,0,2,2,0,1,0,0,0]}
    assert get_value(p,0,0) == 6 # retourne 6
    assert get_value(p,2,3) == 0 # retourne 0 (la case est vide)
    assert get_value(p,1,3) == 2 # retourne 2
    assert get_value(p,3,0) == 1# retourne 1
    assert get_value(p,18,3) == 'Erreur'# lève une erreur
    print("ok pour get_value")
  
def test_set_value():
    p = init_play()
    set_value(p, 0, 0, 1)
    assert p == {'n': 4, 'nb_cases_libres': 15,
                 'tiles': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}  # met la valeur 1 dans la case (0,0)
    set_value(p, 1, 2, 4)
    assert p == {'n': 4, 'nb_cases_libres': 14,
                 'tiles': [1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0]}  # met la valeur 4 dans la case (1,2)
    assert set_value(p, 18, 3, 1) == 'Erreur'  # génère une erreur
    set_value(p, 2, 3, 6)
    assert p == {'n': 4, 'nb_cases_libres': 13,
                 'tiles': [1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 6, 0, 0, 0, 0]}  # met la valeur 6 dans la case (2,3)
    print("ok pour set_value")
 def test_is_room_empty():
    p = {'n': 4, 'nb_cases_libres': 15,
           'tiles': [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
    assert is_room_empty(p,0,1) == False # return False
    assert is_room_empty(p,3,2) == True# return True
    assert is_room_empty(p,15,2) == 'Erreur' # génère une Erreur
    print("ok pour is_room_empty")
