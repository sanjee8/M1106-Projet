# from tkinter import *
# from tkinter.messagebox import *

def full_affichage(plateau):
    """
    Affichage en couleur
    """


    # On crée une fenêtre, racine de notre interface
    fenetre = Tk()
    # On défini un titre
    fenetre.title('Threes')
    # On défini un icon
    fenetre.iconbitmap('icon.ico')
    fenetre.resizable(0, 0)


    def alert():
        """
        Affiche l'alert A propos.
        """
        showinfo("A propos", "Jeu crée par Sanjeevan et Enrick\n\nProjet M1106 - Année 2019/2020")

    def get_color(val):
        """
        Retourne une couleur selon la valeur rentré en paramètre

        EXEMPLE:
        color = get_color(0) # color vaut on_blue
        """
        if (val == 0 or val == 1):  # Vérifie si val est égal à 1 ou 0
            return 'dark turquoise'  # Renvoie on_blue
        elif (val == 2):  # Si c'est égal à 2
            return 'OrangeRed3'  # Renvoie on_red
        else:  # Sinon
            return 'old lace'  # Renvoie on_white

    def sized(score):
        """
        Retourne un texte adapté à la taille du score

        EXEMPLE:
        texte = sized(3) # texte vaut '  3  '
        texte2 = sized(300) # texte vaut ' 300 '
        """
        if (score > 10000):  # Verifier la taille de score
            return '' + str(score) + ''  # Adapter le texte selon la taille du score
        elif (score > 1000):
            return ' ' + str(score) + ''
        elif (score > 100):
            return ' ' + str(score) + ' '
        elif (score > 10):
            return '  ' + str(score) + ' '
        else:
            return '  ' + str(score) + '  '

    # Menu du haut
    menubar = Menu(fenetre)

    # Catégorie JEU > Lancer une partie/Quitter
    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Lancer une partie", command=alert)
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=fenetre.quit)
    menubar.add_cascade(label="Jeu", menu=menu1)

    # Catégorie Aide > A propos
    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="A propos", command=alert)
    menubar.add_cascade(label="Aide", menu=menu3)

    fenetre.config(menu=menubar)

    i = 0 # Initialisation boucle ligne
    while(i < 4):
        j=0 # Initialisation boucle colonne
        p = PanedWindow(fenetre, orient=HORIZONTAL)
        p.pack()
        while(j < 4):
            indice = (i*4)+j # Calcul indice

            p.add(Label(p, text=sized(plateau['tiles'][indice]), font=("Helvetica", 14), background=get_color(plateau['tiles'][indice]), fg='grey25', width=6, height=4, anchor=CENTER))

            j+=1 # Incrémentation j
        p.pack()
        i+=1 # Incrémentation i
        print(" ") # Permet de séparer les lignes principales (sans couleurs)



    # On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
    fenetre.mainloop()
