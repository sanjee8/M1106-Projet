# Module tiles.tiles_acces

####################################
#             PARTIE 1             #
####################################

   
def check_indice(plateau, indice):
    """
    Retourne True si indice correspond à un indice valide de case pour le plateau ( entre 0 et n-1)

    :param plateau: dictionnaire contenant le plateau du jeu
    :param indice: indice valide de case du plateau
    :return: True ou False

    EXEMPLE:
    p = init_play()
    check_indice(p,0) # Retourne True
    check_indice(p,10) # Retourne False
    check_indice(p,3) # Retourne True
    check_indice(p,4) # Retourne False
    check_indice(p,-1) # Retourne False
    """
    n = plateau['n']  # On va chercher la valeur de n
    if 0 <= indice < n:  # Vérifie si indice est compris entre 0 et n-1
        return True  # Alors renvoie True
    else:
        return False  # Sinon renvoie False
    
def check_room(plateau, lig, col):
    """
    Retourne True si (lig, col) est une case du plateau (lig et col sont des indices valides)

    :param plateau: dictionnaire contenant le plateau du jeu
    :param lig: indice valide de ligne du plateau
    :param col: indice valide de colonne du plateau
    :return: True ou False

    EXEMPLE:
    p = init_play()
    check_room(p,2,1) # Retourne True
    check_room(p,10,2) # Retourne False
    check_room(p,-1,3) # Retourne False
    check_room(p,3,3) # Retourne True
    """

    # Utilise la fonction check_indice pour vérifier si col et lig sont bien valides
    return check_indice(plateau, lig) and check_indice(plateau, col)

def get_value(plateau, lig, col):
    """
    Retourne la valeur de la case (lig,col)
    Erreur si (lig,col) n'est pas valide

    :param plateau: dictionnaire contenant le plateau du jeu
    :param lig: indice de ligne du plateau
    :param col: indice de colonne du plateau
    :return: int
    
    EXEMPLE:
    p = {'n' : 4, 'nb_cases_libres' : 16, 'tiles' : [6,2,3,2,0,2,6,2,0,2,2,0,1,0,0,0]}
    get_value(p,0,0) # retourne 6
    get_value(p,2,3) # retourne 0 (la case est vide)
    get_value(p,1,3) # retourne 2
    get_value(p,3,0) # retourne 1
    get_value(p,18,3) # lève une erreur
    """
    if check_room(plateau, lig, col):  # Vérifie que les indices sont valides
        indice = (lig * 4) + col  # Calcule d'incide final à l'aide de lig et col
        return plateau['tiles'][indice]  # Retourne la valeur dans le tableau tiles du dictionnaire plateau
    else: 
        return 'Erreur'  # Retourne erreur si les indices sont invalides

def set_value(plateau, lig, col, val):
    """
    Affecte la valeur val dans la case (lig, col) du plateau.
    Erreur si (lig, col) n'est pas une case valide
    ou si val n'est pas supérieur ou égal à 0
    Met aussi à jour le nombre de cases libres ( sans tuile(s) )

    :param plateau: dictionnaire contenant le plateau du jeu
    :param lig: indice de ligne du plateau
    :param col: indice de colonne du plateau
    :param val: valeur int
    :return: rien ou Erreur
    
    EXEMPLE:
    p = init_play()
    set_case(p,0,0,1) # met la valeur 1 dans la case (0,0)
    set_case(p,1,2,0) # met la valeur 0 dans la case (1,2)
    set_case(p,18,3,1) # génère une erreur
    set_case(p,2,3,6) # met la valeur 6 dans la case (2,3)
    """
    if val > 0:  # Vérifie que val soit supérieur à 0
        if check_room(plateau, lig, col):  # Vérifie que les indices sont valides
            indice = (lig * 4) + col  # Calcule d'incide final à l'aide de lig et col
            plateau['tiles'][indice] = val  # Affecte la valeur val dans la case (lig,col) du plateau.
        else:
            print('Erreur 1')  # Si les indices sont invalides, renvoie erreur
    else:
        print('Erreur')  # Si val est égal ou plus petit que 0, renvoie erreur
    
def is_room_empty(plateau, lig, col):
    """
    Teste si une case du plateau est libre ou pas
    return True si la case est libre, False sinon

    :param plateau: dictionnaire contenant le plateau du jeu
    :param lig: indice de ligne du plateau
    :param col: indice de colonne du plateau
    :return: True, False ou Erreur

    Exemple:
    p = init_play()
    is_room_empty(p,0,1) # return False
    is_room_empty(p,3,2) # return True
    is_room_empty(p,15,2) # génère une Erreur
    """
    if check_room(plateau, lig, col):  # Vérifie que les indices sont valides
        indice = (lig * 4) + col  # Calcule d'incide final à l'aide de lig et col
        if plateau['tiles'][indice] == 0:  # Vérifie si la valeur de la case (lig,col) est égal à 0
            return True  # Alors renvoie True
        else:
            return False  # Sinon renvoie False
    else:
        return 'Erreur'  # Si les indices sont invalides, renvoie Erreur
