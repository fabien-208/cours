# -------------------------------------------------------------------------------
# Name:        DM Labyrinthe Pile
# Author:      Fabien Piat
# Created:     2022
#
# Licence:     Prof
# -------------------------------------------------------------------------------
from copy import deepcopy
from tkinter import *

"""
# Bibliotheque qui permet de fabriquer une interface graphique
# La connaissance de cette bibliotheque n'est pas une exigance du programmme
# mais cela permet d'avoir un viseul plus agréable

Lisez la docstring des 2 fonctions ci-dessous.
NE PAS LES MODIFIER
"""


def AfficherLab(laby):
    """
    Affiche le labyrinthe
    param : list (liste de listes)
    return : None (Interface graphique du labyrinthe)
    """
    fenetre = Tk()
    fenetre.title("labyrinthe")
    largeur = len(laby[0])
    hauteur = len(laby)
    taille = 50
    num_line = 0
    num_case = 0

     ##----- Création des boutons -----##
    bouton_quitter = Button(fenetre, text='Quitter', command=fenetre.destroy)
    bouton_quitter.grid(row = 1, column = 1, sticky=W+E, padx=3, pady=3)

    ##----- Création des canevas -----##
    canvas = Canvas(fenetre, width = hauteur*taille+2, height = hauteur*taille+2, bg = 'grey')
    canvas.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3)

    for line in laby:
        num_line = num_line + 1

        for case in line:
            num_case = num_case + 1
            if case == 0:
                canvas.create_rectangle(
                    (num_case - 1) * taille,
                    (num_line - 1) * taille,
                    num_case * taille,
                    num_line * taille,
                    fill="green",
                )
        ## affichage des tuples dans les cases
            canvas.create_text(
                ((num_case-1) * taille + taille/2),
                ((num_line-1) * taille + taille/2),
                text="(" + str(num_line - 1) + "," + str(num_case - 1) + ")",
                fill='black')
        ## fin affichage des tuples
        num_case = 0
    fenetre.mainloop()


def AfficherSol(laby, pile):
    """
    Affiche le labyrinthe avec la solution
    parm : laby (list)
           pile (list) liste de tuple qui forme la solution
    return : None (Interface graphique du labyrinthe et de sa solution)
    """
    fenetre = Tk()
    fenetre.title("labyrinthe SOLUTION")
    largeur = len(laby[0])
    hauteur = len(laby)
    taille = 50
    num_line = 0
    num_case = 0
    ##----- Création des boutons -----##
    bouton_quitter = Button(fenetre, text='Quitter', command=fenetre.destroy)
    bouton_quitter.grid(row = 1, column = 1, sticky=W+E, padx=3, pady=3)

    ##----- Création des canevas -----##
    canvas = Canvas(fenetre, width = hauteur*taille+2, height = hauteur*taille+2, bg = 'grey')
    canvas.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3)
##    canvas = Canvas(
##        fenetre, width=taille * largeur, height=taille * hauteur, background="grey"
##    )
    for line in laby:
        num_line = num_line + 1
        for case in line:
            num_case = num_case + 1
            if case == 0:
                canvas.create_rectangle(
                    (num_case - 1) * taille,
                    (num_line - 1) * taille,
                    num_case * taille,
                    num_line * taille,
                    fill="green",
                )
        num_case = 0
    for elt in pile:
        canvas.create_oval(
            taille * elt[1] + taille / 3,
            taille * elt[0] + taille / 3,
            taille * elt[1] + taille - taille / 3,
            taille * elt[0] + taille - taille / 3,
            fill="red",
            width=0,
        )

##    canvas.pack()
    fenetre.mainloop()

## partie à complèter ou créer

## Question 3
## à compléter
def depart(laby):
    """
    permet de commettre les coordonnées du point de départ du labyrinthe
    param: (list) labyrinthe liste de listes
    return: (tuple) coordonnées entrée du labyrinthe
    """
    n = len(laby)
    m = len(laby[0])
    for ligne in range(n):
        for colonne in range(m):
            if laby[ligne][colonne] ==2:
                return (ligne, colonne)


## Question 4
## à complèter
def nb_cases_vides(laby):
    """
    permet de trouver le nombre de cases vides du labyrinthe
    param: (list) tableau (liste de listes du labyrinthe)
    return: (int) nombre de cases vides
    """
    n = len(laby)
    m = len(laby[0])
    case_vide = 2
    for ligne in range(n):
        for colonne in range(m):
            if laby[ligne][colonne] ==1:
                case_vide +=1
    return case_vide 
## Question 7
## à complèter
def mystere(T, v):
    """
    cette fonction permet savoir les case vide a coté d'une case données
    param: T un tableau
    param: v un tuple de deux nombres entiers
    sortie: une liste de case vid a coté de T et v
    """
    V = []
    i, j = v[0], v[1]
    for a in (-1, 1):
        if 0 <= i + a and i + a < nb_lignes:
            if T[i + a][j] == 1 or T[i + a][j] == 3:
                V.append((i + a, j))
        if 0 <= j + a and j + a < nb_colonnes:
            if T[i][j + a] == 1 or T[i][j + a] == 3:
                V.append((i, j + a))
    return V


def parcours(laby, depart, arrivee):
    """
    Permet de parcourir le labyrinthe de l'entrée vers la sortie
    param: (list) tableau (liste de listes du labyrinthe)
    param: (tuple) coordonnées de l'entrée du labyrinthe
    param: (tuple) coordonnées de la sortie du labyrinthe
    return: (list) Pile du chemin de l'entrée vers la sortie
    """
    pile = [depart]
    copie = pile = [depart]
    copie = copy.deepcopy(laby)

    copie[depart[0]][depart[1]] = 2
    copie[arrivee[0]][arrivee[1]] = 3

    while pile:
        valeur = pile[-1]
        if valeur == arrivee:
            return pile
        voisins = mystere(copie, valeur)
        if voisins:
            voisin = voisins[0]
            pile.append(voisin)
            copie[voisin[0]][voisin[1]] = 2
        else:
            copie[valeur[0]][valeur[1]] = 0
            pile.pop()
    return pile

    copie[depart[0]][depart[1]] = 2
    copie[arrivee[0]][arrivee[1]] = 3

    while pile:
        valeur = pile[-1]
        if valeur == arrivee:
            return pile
        voisins = mystere(copie, valeur)
        if voisins:
            voisin = voisins[0]
            pile.append(voisin)
            copie[voisin[0]][voisin[1]] = 2
        else:
            copie[valeur[0]][valeur[1]] = 0
            pile.pop()
    return pile



## Programme principal

## Ne pas modifier les lignes suivantes
## Labyrinthe 1
lab1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [2, 1, 0, 1, 1, 1, 0, 1, 0, 1, 3],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

## Labyrinthe 2
lab2 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 3, 0],
]

## Labyrinthe 3
lab3 = [
    [0, 2, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 3, 0],
]

AfficherLab(lab1)
AfficherLab(lab2)
AfficherLab(lab3)

## Question 1
## à complèter
lab2[1][0] = 2
AfficherLab(lab2)

## Question 2
## à complèter
nb_lignes = len(lab2[0])
nb_colonnes = len(lab2)

## Question 3
## ne pas modifier
assert depart(lab1) == (5, 0), "Entrée labyrinthe incorrect"
assert depart(lab2) == (1, 0), "Entrée labyrinthe incorrect"
assert depart(lab3) == (0, 1), "Entrée labyrinthe incorrect"

# Question 4
# ne pas modifier
assert nb_cases_vides(lab2) == 19, "Nombres de cases vides incorrect"

# Question 5
# à complèter

# Question 6
# à complèter
assert mystere(lab3, (0, 1)) ==[(1,1)] , "Retour de mystere incorrect"



# Question 7
# ne pas modifier
# Affichage de la solution lab3
# pile=[(0,1),(1,1),(1,2),(1,3),(2,3),(3,3),(3,4),(4,4),(5,4)]
assert parcours(lab3, (0, 1), (5, 4)) == [(0,1),(1,1),(1,2),(1,3),(2,3),(3,3),(3,4),(4,4),(5,4)], "Retour de mystere incorrect"
pile = parcours(lab3, (0, 1), (5, 4))
AfficherSol(lab3, pile)

