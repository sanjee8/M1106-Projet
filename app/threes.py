# Module app.threes
from termcolor import colored
from life_cycle.play import get_user_menu, cycle_play, save_game, restore_game, highscore


####################################
#             PARTIE 3             #
####################################


def threes():
    """
    Permet d'enchainer les parties au jeu Threes, de reprendre une partie sauvegardée
    et de sauvegarder une partie en cours.

    :return: rien
    """

    ent = get_user_menu(None)  # Affichage du menu principal ( sans sauvegarde et reprendre )
    use = True  # Initialisation pour boucle
    while use:
        if ent == 'N':  # Si N est choisi dans le menu principal
            cyc, game = cycle_play(None)  # Affiche le jeu, etc

            if cyc:  # Si cyc est True, le jeu est terminé et gagné.
                # Affiche le message de fin de jeu
                print(colored("                                     ", "grey", "on_green"))
                print(colored(" Bravo ! Vous avez gagné la partie ! ", "grey", "on_green"))
                print(colored("                                     ", "grey", "on_green"))

                highscore(game['score'])

                use = False
            else:
                # Affiche le menu principal avec sauvegarde et reprendre
                ent = get_user_menu(game)

        elif ent == 'L':  # Si L est choisi dans le menu principal
            res = restore_game()  # Va chercher la game enregistrer
            cycle_play(res)  # Joue la game trouvée

        elif ent == 'S':  # Si S est choisi dans le menu principal
            save_game(game)  # Sauvagarde la partie
            use = False  # Met fin à la boucle

        elif ent == 'C':  # Si C est choisi dans le menu principal
            cyc, game = cycle_play(game)  # Affiche le jeu, etc
            if cyc:  # Si cyc est True, le jeu est terminé et gagné.
                # Affiche le message de fin de jeu
                print(colored("                                     ", "grey", "on_green"))
                print(colored(" Bravo ! Vous avez gagné la partie ! ", "grey", "on_green"))
                print(colored("                                     ", "grey", "on_green"))

                highscore(game['score'])

            else:  # Sinon
                # Affiche le menu principal avec sauvegarde et reprendre
                ent = get_user_menu(game)
        elif ent == 'Q':  # Si S est choisi dans le menu principal
            use = False  # Met fin à la boucle


threes()  # Appeler la fonction threes
