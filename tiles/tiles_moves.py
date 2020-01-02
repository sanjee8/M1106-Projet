# Module tiles moves

def get_nb_empty_rooms(plateau):
    """
    Met à jour le dictionnaire plateau avec le nombre de case libre(s) du plateau
    et renvoie le nombre de case(s) libre(s)
    
    EXEMPLE:
    p = {'n' : 4, 'nb_cases_libres' : 6, 'tiles' : [6,2,3,2,0,2,6,2,0,2,2,0,1,0,0,0]}
    # Pour le test
    p['nombre_cases_libres'] = 5
    n=get_nb_empty_rooms(p) # n vaut 6
    print(p['nombre_cases_libres']) # Affiche 6
    """
    i = 0 # initialisation de i
    s = 0 # initialisation de s
    while(i < len(plateau['tiles'])): # Boucle pour vérifier chaque élément de plateau['tiles']
        if(plateau['tiles'][i] == 0): # Vérifie si la valeur de la case i est égal à 0
            s+=1 # Alors rajoute 1 à s
        i+=1 # Incrémente i
    plateau['nb_cases_libres'] = s # Met à jour plateau['nb_cases_libres'] avec la valeur trouvé
    
    return s # Renvoie le nombre de cases libres
