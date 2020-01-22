# Module ui.play_display
from termcolor import colored

####################################
#             PARTIE 1             #
####################################


def get_color(val):
    """
    Retourne une couleur selon la valeur rentré en paramètre

    :param val: int
    :return: str
    
    EXEMPLE:
    color = get_color(0) # color vaut on_blue
    """
    if val == 0 or val == 1:  # Vérifie si val est égal à 1 ou 0
        return 'on_blue'  # Renvoie on_blue
    elif val == 2:  # Si c'est égal à 2
        return 'on_red'  # Renvoie on_red
    else:  # Sinon
        return 'on_white'  # Renvoie on_white


def sized(score):
    """
    Retourne un texte adapté à la taille du score

    :param score: int
    :return: str

    EXEMPLE:
    texte = sized(3) # texte vaut '  3  '
    texte2 = sized(300) # texte vaut ' 300 '
    """
    if score >= 10000:  # Verifier la taille de score
        return '' + str(score) + ''  # Adapter le texte selon la taille du score
    elif score >= 1000:
        return ' ' + str(score) + ''
    elif score >= 100:
        return ' ' + str(score) + ' '
    elif score >= 10:
        return '  ' + str(score) + ' '
    else:
        return '  ' + str(score) + '  '


def full_display(plateau):
    """
    Affichage en couleurs du jeu
    Prend en paramètre le plateau

    :param plateau: dictionnaire contenant le plateau de jeu
    :return: affichage complet avec termcolor
    """
    i = 0  # Initialisation boucle LIGNE PRINCIPALES
    while i < 4:
        h = 0  # Initialisation boucle LIGNE SECONDAIRES
        while h < 3:
            if h == 1:
                j = 0  # Initialisation boucle COLONNE AVEC TEXTE
                li = colored(' ', 'grey', 'on_grey')  # Initialisation ligne secondaire
                while j < 4:
                    indice = (i * 4) + j  # Calcul indice
                    # Concaténation texte coloré
                    li += colored(sized(plateau['tiles'][indice]), 'grey',
                                  get_color(plateau['tiles'][indice])) + colored(' ', 'grey', 'on_grey')
                    j += 1  # Incrémentation j
            else:
                j = 0  # Initialisation boucle COLONNE SANS TEXTE
                li = colored(' ', 'grey', 'on_grey')  # Initialisation ligne secondaire
                while j < 4:
                    indice = (i * 4) + j  # Calcul indice
                    # Concaténation texte coloré
                    li += colored('     ', 'grey', get_color(plateau['tiles'][indice])) + colored(' ', 'grey',
                                                                                                  'on_grey')
                    j += 1  # Incrémentation j
            print(li)  # Afficher la ligne secondaire (1 ligne principale est composée de 3 lignes secondaires)
            h += 1  # Incrémentation h
        i += 1  # Incrémentation i
        # Permet de séparer les lignes principales (sans couleurs)
        print(colored('                         ', 'grey', 'on_grey'))
