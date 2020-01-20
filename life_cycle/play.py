# Module life_cyble.play
from ui.play_display import *
from ui.user_entries import get_user_move
from tiles.tiles_moves import *
from game.play import create_new_play
from termcolor import colored
from json import *
from os import path

def cycle_play(partie):
    """
    Permet de jouer à Threes

    :param partie: Partie de jeu en cours ou None sinon
    :return: True si la partie est terminée, False si menu demandé

    Séquencement des actions pour cette fonction :
        1 - afficher le plateau de jeu
        2 - afficher la prochaine tuile pour informer le joueur
        3 - saisir le mouvement proposé par le joueur; deux cas possibles :
            * jouer le coup du joueur courant, mettre à jour le score et revenir au point 1
            * ou retourner False si menu demandé
        4 - si partie terminée, retourner True
    """
    while(True):  # On initialise une boucle sans fin jusqu'à return

        if partie is None:  # Si la partie n'est pas en cours
            partie = create_new_play()
        else:  # Sinon
            # Affiche un message contenant les touches de déplacement
            print(colored(' Touches de déplacement :', 'grey', "on_white"))
            print(colored('   h (↑), b (↓), d (→),  ', 'grey', "on_white"))
            print(colored('      g (←), m (menu)    ', 'grey', "on_white"))
            print(colored('                         ', 'grey', 'on_white'))

            if not partie['next_tile']:
                next_tile = get_next_alea_tiles(partie['plateau'], 'init')
                put_next_tiles(partie['plateau'], next_tile)

            next_tile_e = get_next_alea_tiles(partie['plateau'], 'encours')

            # Affiche la partie en cours
            full_display(partie['plateau'])
            # Affiche la prochaine tuile
            print(colored(' ', 'grey', 'on_white') + colored(' Prochaine tuile ', 'grey', "on_cyan") + colored('  ' + str(next_tile_e[0]['val']) + '  ', 'grey',"on_green")+ colored('  ', 'grey', 'on_white'))
            # Récupère le mouvement du joueur
            move = get_user_move()

            # Si le mouvement est m
            if (move == 'm'):
                return False  # On renvoie False
            elif (get_nb_empty_rooms == 0):  # Si il reste plus de cases vides ( jeu terminé )
                return True  # On renvoie True
            else:
                if(move == 'b'):
                    columns_move(partie['plateau'], 0)
                elif(move == 'h'):
                    columns_move(partie['plateau'], 1)
                elif(move == 'd'):
                    lines_move(partie['plateau'], 0)
                elif(move == 'g'):
                    lines_move(partie['plateau'], 1)




def save_game(partie):
    """
    Sauvegarde une partie dans le fichier saved_game.json

    :param partie: Partie en cours
    :return: rien
    """
    jso = dumps(partie)  # Fais passer un dictionnaire en str
    file = open('saved_game.json', 'w')  # Permet de créer un fichier saved_game.json

    file.write(jso)  # On écrit dans saved_game.json la partie en str

    file.close()  # On ferme le fichier

def restore_game():
    """
    Restaure et retourne une partie sauvegardée dans le fichier 'game_saved.json', ou retourne une nouvelle partie si
    aucune partie n'est sauvegardée.

    :return: dictionnaire partie
    """
    # Si saved_json existe
    if(path.exists('saved_game.json')):
        # On ouvre le fichier saved_game.json
        file = open('saved_game.json', 'r')
        # On lit et enregistre dans la variable txt
        txt = file.read()

        # Si txt est vide
        if(txt == '' or txt == ' '):
            # On renvoie une nouvelle partie
            return create_new_play()
        # Sinon on envoie le txt
        return loads(txt)
    # Sinon
    else:
        # On renvoie une nouvelle partie
        return create_new_play()

