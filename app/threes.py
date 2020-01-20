# Module app.threes
from ui.user_entries import *
from life_cycle.play import *

def threes():
    """
    Permet d'enchainer les parties au jeu Threes, de reprendre une partie sauvegardée
    et de sauvegarder une partie en cours.

    :return: rien
    """

    ent = get_user_menu(None)
    if(ent == 'N'):
        cyc = cycle_play(None)

    elif(ent == 'L'):
        res = restore_game()
        cycle_play(res)





threes()