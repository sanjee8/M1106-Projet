# Module life_cyble.play
from ui.play_display import *
from ui.user_entries import *
from tiles.tiles_moves import *
from game.play import create_new_play, get_score
from termcolor import colored
from json import *
from os import path


####################################
#             PARTIE 3             #
####################################


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

    while True:  # On initialise une boucle sans fin jusqu'à return

        if partie is None:  # Si la partie n'est pas en cours
            partie = create_new_play()  # On crée une nouvelle partie
            # Place les deux tuiles de départ
            put_next_tiles(partie['plateau'], get_next_alea_tiles(partie['plateau'], 'init'))
        else:  # Sinon

            # Affiche un message contenant les touches de déplacement
            print(colored(' Touches de déplacement :', 'grey', "on_white"))
            print(colored('   h (↑), b (↓), d (→),  ', 'grey', "on_white"))
            print(colored('      g (←), m (menu)    ', 'grey', "on_white"))
            print(colored('                         ', 'grey', 'on_grey'))

            # Génère la tuile suivante ( sans la placer )
            partie['next_tile'] = get_next_alea_tiles(partie['plateau'], 'encours')

            # Affiche la partie en cours
            full_display(partie['plateau'])
            # Affiche la prochaine tuile
            if partie['next_tile']['check']:
                print(colored('  Prochaine tuile ', 'grey', "on_cyan") + colored(
                    '   ' + str(partie['next_tile'][0]['val']) + '   ', 'grey', "on_green"))
            # Affiche le score
            print(colored('       Score      ', 'grey', "on_cyan") + colored(
                ' ' + sized(partie['score']) + ' ', 'grey', "on_green"))
            # Afficher le highscore
            print(colored('      Record      ', 'grey', "on_cyan") + colored(
                ' ' + sized(get_highscore()) + ' ', 'grey', "on_green"))

            # Récupère le mouvement du joueur
            move = get_user_move()
            # Si le mouvement est m
            if move == 'm':
                return False, partie  # On renvoie False
            elif not partie['next_tile']['check']:  # Si il reste plus de cases vides ( jeu terminé )
                return True, partie  # On renvoie True
            else:
                play_move(partie['plateau'], move)  # Sinon prend en compte le déplacement

            # Vérification pour éviter les superpositions
            val = partie['next_tile'][0]['val']
            idc = (partie['next_tile'][0]['lig'] * 4) + partie['next_tile'][0]['col']
            if partie['plateau']['tiles'][idc] != 0:
                partie['next_tile'] = get_next_alea_tiles(partie['plateau'], 'encours')
                partie['next_tile'][0]['val'] = val

            # Place la tuile suivante
            put_next_tiles(partie['plateau'], partie['next_tile'])

            # Met à jour le score
            partie['score'] = get_score(partie['plateau'])



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

    # Affiche le message d'enregistrement
    print(colored("                                  ", "grey", "on_yellow"))
    print(colored(" La partie a bien été sauvegardée ", "grey", "on_yellow"))
    print(colored("                                  ", "grey", "on_yellow"))


def restore_game():
    """
    Restaure et retourne une partie sauvegardée dans le fichier 'game_saved.json', ou retourne une nouvelle partie si
    aucune partie n'est sauvegardée.

    :return: dictionnaire partie
    """
    # Si saved_json existe
    if path.exists('saved_game.json'):
        # On ouvre le fichier saved_game.json
        file = open('saved_game.json', 'r')
        # On lit et enregistre dans la variable txt
        txt = file.read()

        # Si txt est vide
        if txt == '' or txt == ' ':
            # On renvoie une nouvelle partie
            return create_new_play()
        # Sinon on envoie le txt
        return loads(txt)
    # Sinon
    else:
        # On renvoie une nouvelle partie
        return create_new_play()


def highscore(score):
    # On ouvre le fichier score.json
    file = open('score.json', 'r')
    # On lit et enregistre dans la variable txt
    txt = file.read()

    sco = loads(txt)

    if score > sco['highscore']:
        dic = {'highscore': score}
        jso = dumps(dic)  # Fais passer un dictionnaire en str
        file = open('score.json', 'w')  # Permet de créer un fichier score.json

        file.write(jso)  # On écrit dans highscore.json la partie en str
        file.close()  # On ferme le fichier
        print(colored("                                             ", "grey", "on_green"))
        print(colored(" Félicitations ! Vous avez battu le record ! ", "grey", "on_green"))
        print(colored("                                             ", "grey", "on_green"))


def get_highscore():
    # On ouvre le fichier score.json
    file = open('score.json', 'r')
    # On lit et enregistre dans la variable txt
    txt = file.read()

    sco = loads(txt)
    return sco['highscore']
