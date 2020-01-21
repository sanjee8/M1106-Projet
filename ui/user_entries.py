# Module ui.user_entries
from termcolor import colored


####################################
#             PARTIE 3             #
####################################

def get_user_move():
    """
    Saisie et retourne le coup joué par le joueur parmi les choix :

    :return: - 'h' pour haut,
             - 'b' pour bas,
             - 'g' pour gauche
             - 'd' pour droite
             - 'm' pour menu principal
    """

    while True:  # Création boucle qui se répète à l'infini jusqu'à return
        ent = input()  # Entrée du joueur
        if ent == 'h' or ent == 'H':  # Vérifie si l'entrée est égal à h ou H
            return 'h'  # On renvoie h
        elif ent == 'b' or ent == 'B':  # Vérifie si l'entrée est égal à b ou B
            return 'b'  # On renvoie h
        elif ent == 'g' or ent == 'G':  # Vérifie si l'entrée est égal à g ou G
            return 'g'  # On renvoie g
        elif ent == 'd' or ent == 'D':  # Vérifie si l'entrée est égal à d ou D
            return 'd'  # On renvoie d
        elif ent == 'm' or ent == 'M':  # Vérifie si l'entrée est égal à m ou M
            return 'm'  # On renvoie m


def get_user_menu(partie):
    """
    Saisi et retourne le choix du joueur dans le menu principal

    :param partie: Partie en cours ou None sinon
    :return: Choix de l'utilisateur ( en majuscule )
        - 'N': Commencer une nouvelle partie,
        - 'L': Charger une partie,
        - 'S': Sauvegarder la partie en cours (si le paramètre partie correspond à une partie en cours),
        - 'C': Reprendre la partie en cours (si le paramètre partie correspond à une partie en cours),
        - 'Q': Terminer le jeu
    """

    print(colored('          Menu principal          ', 'grey', "on_white"))
    print(colored(' N ', 'grey', "on_green") + colored(' Commencer une nouvelle partie ', 'grey', "on_white"))
    print(colored(' L ', 'grey', "on_green") + colored(' Charger une partie            ', 'grey', "on_white"))
    if partie is not None:
        print(colored(' S ', 'grey', "on_green") + colored(' Sauvegarder la partie en cours', 'grey', "on_white"))
        print(colored(' C ', 'grey', "on_green") + colored(' Reprendre la partie en cours  ', 'grey', "on_white"))
    print(colored(' Q ', 'grey', "on_green") + colored(' Terminer le jeu               ', 'grey', "on_white"))

    while True:  # Création boucle qui se répète à l'infini jusqu'à return
        ent = input()  # Entrée du joueur
        if ent == 'n' or ent == 'N':  # Vérifie si l'entrée est égal à n ou N
            return 'N'  # On renvoie N
        elif ent == 'l' or ent == 'L':  # Vérifie si l'entrée est égal à l ou L
            return 'L'  # On renvoie L
        elif ent == 's' or ent == 'S':  # Vérifie si l'entrée est égal à s ou S
            return 'S'  # On renvoie S
        elif ent == 'c' or ent == 'C':  # Vérifie si l'entrée est égal à c ou C
            return 'C'  # On renvoie C
        elif ent == 'q' or ent == 'Q':  # Vérifie si l'entrée est égal à Q ou q
            return 'Q'  # On renvoie Q
