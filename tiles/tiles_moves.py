# Modules tiles.tiles_moves
from random import randint
from tiles.tiles_acces import set_value


####################################
#             PARTIE 1             #
####################################


def get_nb_empty_rooms(plateau):
    """
    Met à jour le dictionnaire plateau avec le nombre de case libre(s) du plateau
    et renvoie le nombre de case(s) libre(s)
    :param plateau: dictionnaire contenant le plateau du jeu
    :return: int
    EXEMPLE:
    p = {'n' : 4, 'nb_cases_libres' : 6, 'tiles' : [6,2,3,2,0,2,6,2,0,2,2,0,1,0,0,0]}
    # Pour le test
    p['nombre_cases_libres'] = 5
    n=get_nb_empty_rooms(p) # n vaut 6
    print(p['nombre_cases_libres']) # Affiche 6
    """
    i = 0  # initialisation de i
    s = 0  # initialisation de s
    while i < len(plateau['tiles']):  # Boucle pour vérifier chaque élément de plateau['tiles']
        if plateau['tiles'][i] == 0:  # Vérifie si la valeur de la case i est égal à 0
            s += 1  # Alors rajoute 1 à s
        i += 1  # Incrémente i
    plateau['nb_cases_libres'] = s  # Met à jour plateau['nb_cases_libres'] avec la valeur trouvé

    return s  # Renvoie le nombre de cases libres


####################################
#             PARTIE 2             #
####################################

def get_next_alea_tiles(plateau, mode):
    """
    Retourne une ou deux tuile(s) dont la position (lig,col) est tirée
    aléatoirement et correspond à un emplacement libre du plateau.
    :param plateau: dictionnaire contenant le plateau du jeu
    :param mode: init ou encours
    :return: dictionnaire
    """

    if mode == 'init':  # Si mode = init
        # On génère des valeurs aléatoire pour le positionnement de la première case
        val1 = randint(0, 3)
        val2 = randint(0, 3)
        # De même pour la deuxième case
        va1 = randint(0, 3)
        va2 = randint(0, 3)

        # On vérifie que on tombe pas sur la même case
        while (va1 == val1) and (va2 == val1):
            va1 = randint(0, 3)
            va2 = randint(0, 3)
        # On génère aléatoirement la valeur de n1 et n2 (et vérifier qu'ils soient différements)
        n1 = randint(1, 2)
        n2 = randint(1, 2)
        while (n1 == n2):
            n2 = randint(1, 2)
        # On return le dictionnaire
        return {0: {'val': n1, 'lig': val1, 'col': val2}, 1: {'val': n2, 'lig': va1, 'col': va2}, 'check': True}
    else:  # Sinon, on considère que c'est le mode encours
        if get_nb_empty_rooms(plateau) == 0:  # Si le jeu ne peut être continué
            return {0: {}, 'check': False}  # Return check false
        val = randint(1, 3)  # On génère une valeur entre 1 et 3
        tab = []  # Init le tableau des positions des cases nulles
        i = 0  # Init boucle
        while i < len(plateau['tiles']):
            if plateau['tiles'][i] == 0:  # Si la case est vide
                tab.append(i)  # On ajoute la valeur de l'emplacement dans le tableau
            i += 1  # Incrémentation de i

        if len(tab) != 0:
            n = randint(0, len(tab) - 1)  # On prend une postions aléatoire dans le tableau
            num = tab[n]
        else:
            return {0: {}, 'check': False}

        # On décompose la veuleur de la position dans le tableau en (lig,col)
        lig = 0
        col = 0

        while num >= 4:
            num = num - 4
            lig += 1
            col = num

        # On return le dictionnaire

        return {0: {'val': val, 'lig': lig, 'col': col}, 'check': True}


def put_next_tiles(plateau, tiles):
    """
    Permet de placer une ou deux tuiles dans le plateau
    :param plateau: Plateau de jeu
    :param tiles: dictionnaire sous la forme de celui renvoyé par la fonction get_next_alea_tiles
    :return: rien
    """
    # Place la première tuile
    set_value(plateau, tiles[0]['lig'], tiles[0]['col'], tiles[0]['val'])

    # Si il y a une deuxième tuile
    if 1 in tiles:
        # La place
        set_value(plateau, tiles[1]['lig'], tiles[1]['col'], tiles[1]['val'])


def line_pack(plateau, num_lig, debut, sens):
    """"
    Tasse les tuiles d'une ligne dans un sens donné
    :param plateau: dictionnaire contenant le plateau du jeu
    :param num_lig: indice de la ligne à "tasser"
    :param debut: indice à partir duquel se fait le "tassement"
    :param sens: du "tassement", 1 vers la gauche, 0 vers la droite
    :return: rien
    """

    if sens == 1:  # si le sens est égal à 1, alors on traite le sens gauche
        debut = num_lig * 4 + debut  # On encadre les 4 éléments de la num_lig i-ème ligne
        j = num_lig * 4 + 3

        while debut < j:  # Initialisation de la boucle
            plateau['tiles'][debut] = plateau['tiles'][debut + 1]  # Décalage des valeurs
            debut += 1  # Incrémentation de début
        if plateau['tiles'][j] != 0:  # On vérifie si la dernière valeur est différente de 0
            plateau['tiles'][j] = 0  # On définie la dernière valeur à 0

    else:  # sinon on traite le sens droite

        debut = (num_lig * 4) + 3 - debut  # On encadre les 4 éléments de la num_lig i-ème ligne
        j = num_lig * 4

        while debut > j:  # Initialisation de la boucle
            plateau['tiles'][debut] = plateau['tiles'][debut - 1]  # Décalage des valeurs
            debut -= 1  # Incrémentation de début

        if plateau['tiles'][j] != 0:  # On vérifie si la première valeur de la ligne est différente de 0
            plateau['tiles'][j] = 0  # On définie la première valeur à 0


def column_pack(plateau, num_col, debut, sens):
    """
    Tasse les tuiles d'une colonne donnée dans un sens donné
    :param plateau: dictionnaire contenant le plateau du jeu
    :param num_col: indice de la colonne à "tasser"
    :param debut: indice à partir duquel se fait le "tassement"
    :param sens: du "tassement", 1 vers le haut, 0 vers le bas
    :return: rien
    """

    if sens == 1:  # Si le sens est égal à 1 on traite le sens vers le haut
        j = num_col + (3 * 4)  # On encadre les 4 valeurs de la colonne
        debut = num_col + (4 * debut)
        while debut < j:  # Initialisation de la boucle
            plateau['tiles'][debut] = plateau['tiles'][debut + 4]  # Décalage des valeurs
            debut += 4  # Incrémentation de début
        if plateau['tiles'][j] != 0:  # On vérifie si la dernière valeur de la colonne est différente de 0
            plateau['tiles'][j] = 0  # On définie la dernière valeur à 0
    else:
        j = num_col  # On encadre les 4 valeurs de la colonne
        debut = num_col + (3 * 4) - (debut * 4)
        while debut > j:  # Initialisation de la boucle
            plateau['tiles'][debut] = plateau['tiles'][debut - 4]  # Décalage des valeurs
            debut -= 4  # Incrémentation de debut
        if plateau['tiles'][j] != 0:  # On vérifie si la première valeur est différente de 0
            plateau['tiles'][j] = 0  # On définie la première valeur à 0


def line_move(plateau, num_lig, sens):
    """
    Déplacement des tuiles d'une ligne donnée dans un sens donné en appliquant les règles du jeu Threes.
    :param plateau: dictionnaire contenant le plateau du jeu
    :param num_lig: indice de la ligne pour laquelle il faut déplacer les tuiles
    :param sens: sens du déplacement des tuiles, 1 vers la gauche, 0 vers la droite
    :return: rien
    """

    if sens == 1:  # On vérifie si le sens est 'gauche'
        i = 4 * num_lig  # On encadre les 4 valeurs de la ligne
        j = (4 * num_lig) + 3

        n = 0  # On initialise n
        while i < j:  # Initialisation boucle
            if plateau['tiles'][i] == 0:  # On vérifie que les tuiles ont la même valeur avant le déplacement
                line_pack(plateau, num_lig, n, sens)  # On déplace les tuiles
                i += 1  # Incrémentation de i et n
                n += 1

            # On vérifie que les tuiles ont la même valeur avant le déplacement
            elif plateau['tiles'][i] == 1:
                if plateau['tiles'][i + 1] == 2:
                    line_pack(plateau, num_lig, n, sens)  # On déplace les tuiles
                    plateau['tiles'][i] = 3

            # On vérifie que les tuiles ont la même valeur avant le déplacement
            elif plateau['tiles'][i] == 2:
                if plateau['tiles'][i + 1] == 1:
                    line_pack(plateau, num_lig, n, sens)  # On déplace les tuiles
                    plateau['tiles'][i] = 3

            # On vérifie que les tuiles ont la même valeur avant le déplacement
            elif plateau['tiles'][i] == plateau['tiles'][i + 1]:
                if plateau['tiles'][i] > 2:
                    tuile = plateau['tiles'][i]  # On enregistre la valeur de i
                    line_pack(plateau, num_lig, n, sens)  # On déplace les tuiles
                    plateau['tiles'][i] = tuile * 2

            i += 1  # Incrémentation de i et n
            n += 1

    else:  # Sinon ( sens droit )
        i = (4 * num_lig) + 3  # On encadre les 4 valeurs de la ligne
        j = 4 * num_lig
        n = 0  # Initialisation de n
        while i > j:  # initialisation boucle

            if plateau['tiles'][i] == 0:  # On vérifie que les tuiles ont la même valeur avant le déplacement
                line_pack(plateau, num_lig, n, 0)  # On déplace les tuiles
                i -= 1  # Incrémentation de i et n
                n += 1

            # On vérifie que les tuiles ont la même valeur avant le déplacement
            elif plateau['tiles'][i] == 1:
                if plateau['tiles'][i - 1] == 2:
                    line_pack(plateau, num_lig, n, sens)  # On déplace les tuiles
                    plateau['tiles'][i] = 3  # On change la valeur de la tuile

            # On vérifie que les tuiles ont la même valeur avant le déplacement
            elif plateau['tiles'][i] == 2:
                if plateau['tiles'][i - 1] == 1:
                    line_pack(plateau, num_lig, n, sens)  # On déplace les tuiles
                    plateau['tiles'][i] = 3  # On change la valeur de la tuile

            # On vérifie que les tuiles ont la même valeur avant le déplacement
            elif plateau['tiles'][i] == plateau['tiles'][i - 1]:
                if plateau['tiles'][i] > 2:
                    tuile = plateau['tiles'][i]  # On enregistre la valeur de i
                    line_pack(plateau, num_lig, n, sens)  # On déplace les tuiles
                    plateau['tiles'][i] = tuile * 2  # On change la valeur de la tuile

            i -= 1  # Incrémentation de i et n
            n += 1


def column_move(plateau, num_col, sens):
    """
    Déplacement des tuiles d'une colonne donnée dans un sens donné en appliquant les règles du jeu Threes.
    :param plateau: dictionnaire contenant le plateau de jeu
    :param num_col: indicide la colonne pour laquelle il faut déplacer les tuiles
    :param sens: sens du déplacement des tuiles, 1 vers le haut, 0 vers le bas
    :return: rien
    """

    if sens == 1:  # On vérifie si le sens est 'haut'
        i = num_col  # On encadre les 4 valeurs de la ligne
        j = num_col + (4 * 3)
        n = 0  # Initialisation de n
        while i < j:  # initialisation boucle
            if plateau['tiles'][i] == 0:  # On vérifie que les tuiles ont la même valeur avant le déplacement
                column_pack(plateau, num_col, n, sens)  # On déplace les tuiles
                i += 4  # Incrémentation de i et n
                n += 1

            # On vérifie que les tuiles ont la même valeur avant le déplacement
            elif plateau['tiles'][i] == 1:
                if plateau['tiles'][i + 4] == 2:
                    column_pack(plateau, num_col, n, sens)  # On déplace les tuiles
                    plateau['tiles'][i] = 3

            # On vérifie que les tuiles ont la même valeur avant le déplacement
            elif plateau['tiles'][i] == 2:
                if plateau['tiles'][i + 4] == 1:
                    column_pack(plateau, num_col, n, sens)  # On déplace les tuiles
                    plateau['tiles'][i] = 3

            # On vérifie que les tuiles ont la même valeur avant le déplacement
            elif plateau['tiles'][i] == plateau['tiles'][i + 4]:
                if plateau['tiles'][i] > 2:
                    tuile = plateau['tiles'][i]  # On enregistre la valeur de i
                    column_pack(plateau, num_col, n, sens)  # On déplace les tuiles
                    plateau['tiles'][i] = tuile * 2

            i += 4  # Incrémentation de i et n
            n += 1
    else:  # Sinon ( sens bas )
        i = num_col + (4 * 3)  # On encadre les 4 valeurs de la ligne
        j = num_col
        n = 0  # Initialisation de n
        while i > j:  # initialisation boucle

            if plateau['tiles'][i] == 0:  # On vérifie que les tuiles ont la même valeur avant le déplacement
                column_pack(plateau, num_col, n, sens)  # On déplace les tuiles
                i -= 4  # Incrémentation de i et n
                n += 1

            # On vérifie que les tuiles ont la même valeur avant le déplacement
            elif plateau['tiles'][i] == 1:
                if plateau['tiles'][i - 4] == 2:
                    column_pack(plateau, num_col, n, sens)  # On déplace les tuiles
                    plateau['tiles'][i] = 3

            # On vérifie que les tuiles ont la même valeur avant le déplacement
            elif plateau['tiles'][i] == 2:
                if plateau['tiles'][i - 4] == 1:
                    column_pack(plateau, num_col, n, sens)  # On déplace les tuiles
                    plateau['tiles'][i] = 3

            # On vérifie que les tuiles ont la même valeur avant le déplacement
            elif plateau['tiles'][i] == plateau['tiles'][i - 4]:
                if plateau['tiles'][i] > 2:
                    tuile = plateau['tiles'][i]  # On enregistre la valeur de i
                    column_pack(plateau, num_col, n, sens)  # On déplace les tuiles
                    plateau['tiles'][i] = tuile * 2

            i -= 4  # Incrémentation de i et n
            n += 1


def lines_move(plateau, sens):
    """
    Déplace les tuiles de toutes les ligne du plateau dans un sens donné en appliquant les règles du jeu Threes
    :param plateau: dictionnaire contenant le plateau de jeu
    :param sens: sens du déplacement, 1 vers la gauche, 0 vers la droite
    :return: rien
    """

    i = 0  # Initialisation de i
    while i < 4:  # Initialisation boucle
        line_move(plateau, i, sens)  # On déplace la line i dans le sens sens
        i += 1  # On incrémente i


def columns_move(plateau, sens):
    """
    Déplace les tuiles de toutes les colonnes du plateau dans un sens donné en appliquant les règles du jeu Threes
    :param plateau: dictionnaire contenant le plateau de jeu
    :param sens: sens du déplacement, 1 vers le haut, 0 vers le bas
    :return: rien
    """

    i = 0  # Initialisation de i
    while i < 4:  # Initialisation boucle
        column_move(plateau, i, sens)  # On déplace la colonne i dans le sens sens
        i += 1  # On incrémente i


def play_move(plateau, sens):
    """
    Déplace les tuiles du plateau dans un serns donné en appliquant les règles du jeu Threes.
    :param plateau: dictionnaire contenant le plateau de jeu
    :param sens: sens de déplacement
                    'b' : bas
                    'h' : haut
                    'd' : droite
                    'g' : gauche
    :return: rien
    """

    if sens == 'b':  # Si le sens est b
        columns_move(plateau, 0)  # Alors on columns move dans le sens 0 ( bas )
    elif sens == 'h':  # Si le sens est h
        columns_move(plateau, 1)  # Alors on columns move dans le sens 1 ( haut )
    elif sens == 'd':  # Si le sens est d
        lines_move(plateau, 0)  # Alors on lines move dans le sens 0 ( droite )
    else:  # Sinon
        lines_move(plateau, 1)  # On lines move dans le sens 1 ( gauche )
