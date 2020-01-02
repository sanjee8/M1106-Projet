# Module play

def init_play():
    """
    Retroune un plateau correspondant à une nouvelle partie
    Une nouvelle partie est dictionnaire avec les clefs et valeurs suivantes :
    - 'n' : vaut 4
    - 'nb_cases_libres' : 16 au départ
    - 'tiles' : tableau de 4*4 cases initialisées à 0
    
    EXEMPLE:
    p = init_play() # retourne le dictionnaire
    
    p contient le dictionnaire {'n' : 4, 'nb_cases_libres' : 16, 'tiles' : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
    
    """
    
    return {'n' : 4, 'nb_cases_libres' : 16, 'tiles' : [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]} # retourne le dictionnaire demandé

def is_game_over(plateau):
    """
    Retourne True si la partie est terminée, False sinon
    
    EXEMPLE:
    p = {'n' : 4, 'nb_cases_libres' : 6, 'tiles' : [6,2,3,2,0,2,6,2,0,2,2,0,1,0,0,0]}
    gamover = is_game_over(p) # gamover vaut False
    
    p = {'n' : 4, 'nb_cases_libres' : 6, 'tiles' : [6,2,3,2,12,2,6,2,6,2,2,12,1,6,3,1]}
    gamover = is_game_over(p) # gamover vaut True
    """
    if(get_nb_empty_rooms(plateau) == 0): # Vérifie si le nombre de cases vides est 0
        return True # Alors renvoie True
    else:
        return False # Sinon renvoie False
    
def get_score(plateau):
    """
    Retourne le score du plateau
    
    EXEMPLE:
    p = {'n' : 4, 'nb_cases_libres' : 6, 'tiles' : [6,2,3,2,12,2,6,2,6,2,2,12,1,6,3,1]}
    score = get_score(p) # score vaut 68
    """
    i = 0 # initialisation de i
    s = 0 # initialisation de s
    while(i < len(plateau['tiles'])): # Boucle pour vérifier chaque élément de plateau['tiles']
        s+=plateau['tiles'][i] # Ajoute la valeur de la case plateau['tiles'][i] à s
        i+=1 # Incrémente i
    return s # Retourne le score s

