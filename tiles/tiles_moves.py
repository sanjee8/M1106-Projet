# Module tiles moves
# form random import * ( à importer )

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
def get_next_alea_tiles(plateau, mode):
    """
    Retourne une ou deux tuile(s) dont la position (lig,col) est tirée
    aléatoirement et correspond à un emplacement libre du plateau.
    
    parametres:
    - plateau : dictionnaire contenant le plateau du jeu
    - mode : init ou encours
    """
    
    if(mode == 'init'): # Si mode = init
        # On génère des valeurs aléatoire pour le positionnement de la première case
        val1 = randint(0,3) 
        val2 = randint(0,3)
        # De même pour la deuxième case
        va1 = randint(0,3)
        va2 = randint(0,3)
        
        # On vérifie que on tombe pas sur la même case
        while((va1 == val1) and (va2 == val1)):
            va1 = randint(0,3)
            va2 = randint(0,3)
        # On génère aléatoirement la valeur de n1 et n2 (et vérifier qu'ils soient différements)  
        n1 = randint(1,2)
        n2 = randint(1,2)
        while(n1 == n2):
            n2 = randint(1,2)
        # On return le dictionnaire
        return {0:{'val':n1, 'lig':val1, 'col':val2},1:{'val':n2, 'lig': va1, 'col': va2}, 'check': True}
    else: # Sinon, on considère que c'est le mode encours
        val = randint(1,3) # On génère une valeur entre 1 et 3
        tab = [] # Init le tableau des positions des cases nulles
        i = 0 # Init boucle
        while i<len(p['tiles']):
            if p['tiles'][i] == 0: # Si la case est vide
                tab.append(i) # On ajoute la valeur de l'emplacement dans le tableau
            i += 1 # Incrémentation de i

        n = randint(0,len(tab)) # On prend une postions aléatoire dans le tableau
        num = tab[n]
    
        # On décompose la veuleur de la position dans le tableau en (lig,col)
        lig=0
        while num >= 4:
            num=num-4
            lig+=1
            col=num

        # On return le dictionnaire
        return {0: {'val': val, 'lig': lig, 'col': col},'check': True}
        
def line_pack(plateau,num_lig,debut,sens):
    """"
    Tasse les tuiles d'une ligne dans un sens donné
    
    paramètres:
    plateau - dictionnaire contenant le plateau du jeu
    num_lig - indice de la ligne à "tasser"
    debut - indice à partir duquel se fait le "tassement"
    sens: - du "tassement", 1 vers la gauche, 0 vers la droite
    """
    
    if sens == 1: # si le sens est égal à 1, alors on traite le sens gauche
        debut = num_lig*4+debut # On encadre les 4 éléments de la num_lig i-ème ligne
        j = num_lig*4+3 
        
        while debut < j: # Initialisation de la boucle 
            plateau['tiles'][debut] = plateau['tiles'][debut+1] #Décalage des valeurs
            debut+=1 #Incrémentation de début
        if plateau['tiles'][j] != 0: #On vérifie si la dernière valeur est différente de 0
            plateau['tiles'][j]=0 # On définie la dernière valeur à 0
    
    else: # sinon on traite le sens droite
        debut = num_lig*4+debut # On encadre les 4 éléments de la num_lig i-ème ligne
        j = num_lig*4
        
        while debut > j: # Initialisation de la boucle 
            plateau['tiles'][debut] = plateau['tiles'][debut-1] #Décalage des valeurs
            debut-=1 #Incrémentation de début
        if plateau['tiles'][j] != 0: #On vérifie si la première valeur de la ligne est différente de 0
            plateau['tiles'][j]=0 #On définie la première valeur à 0
        




def column_pack(plateau,num_col,debut,sens):
    """
    Tasse les tuiles d'une colonne donnée dans un sens donné
    
    paramètres:
    
    plateau - dictionnaire contenant le plateau du jeu
    num_col - indice de la colonne à "tasser"
    debut - indice à partir duquel se fait le "tassement"
    sens: - du "tassement", 1 vers le haut, 0 vers le bas
    
    """
    
    if sens == 1: # Si le sens est égal à 1 on traite le sens vers le haut
        j = num_col+4*debut # On encadre les 4 valeurs de la colonne
        debut = num_col
        while debut < j: #Initialisation de la boucle
            plateau['tiles'][debut] = plateau['tiles'][debut+4] #Décalage des valeurs
            debut+=4 #Incrémentation de début
        if plateau['tiles'][j] != 0: #On vérifie si la dernière valeur de la colonne est différente de 0
            plateau['tiles'][j] = 0 #On définie la dernière valeur à 0
    else:
        j = num_col+4*debut # On encadre les 4 valeurs de la colonne
        debut = num_col+3*4
        while debut > j: # Initialisation de la boucle
            plateau['tiles'][debut] = plateau['tiles'][debut-4] #Décalage des valeurs
            debut-=4 #Incrémentation de debut
        if plateau['tiles'][j] != 0:#On vérifie si la première valeur est différente de 0
            plateau['tiles'][j] = 0 #On définie la première valeur à 0
            
