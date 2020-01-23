####################################
#             PARTIE 1             #
####################################
def test_init_play():
    assert init_play() == {'n': 4, 'nb_cases_libres': 16,
                            'tiles': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}
    print("ok pour init_play")

def test_is_game_over():
    z = {'n': 4, 'nb_cases_libres': 0,
            'tiles': [1, 1, 2, 1, 1, 100, 1, 3, 1, 10, 1, 8, 1, 1, 3, 1]}
    p = init_play()
    assert is_game_over(p) == False
    assert is_game_over(z) == True
    print("ok pour is_game_over")

def test_get_score():
    z = {'n': 4, 'nb_cases_libres': 0,
            'tiles': [1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1]}
    p = init_play()
    assert get_score(p) == 0
    assert get_score(z) == 22
    print("ok pour get_score")

####################################
#             PARTIE 3             #
####################################
def test_create_new_play():
    plateau = init_play()  # On crée un plateau vide grâce à init_play
    assert create_new_play() == {
        'plateau': plateau,
        'next_tile': {},
        'score': 3
    }
    print("ok pour create_new_play")
    
