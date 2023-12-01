

from copy import deepcopy 
## Labyrinthe 3
lab3 = [
    [0, 2, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 3, 0],
]

T = deepcopy(lab3)
T[3][2] = 'hello'
for ligne in lab3:
    print(ligne)
print('----------------------')
for liggne in T:
    print(ligne)



def mystere(Tab, t):
    """
    cette fonction permet .............
    param: Tab un tableau
    param: t un tuple de deux nombres entiers
    sortie: ..................
    """
    V = []
    i, j = t[0], t[1]
    for a in (-1, 1):
        if 0 <= i + a and i + a < nb_lignes:
            if Tab[i + a][j] == 1:
                V.append((i + a, j))
        if 0 <= j + a and j + a < nb_colonnes:
            if Tab[i][j + a] == 1:
                V.append((i, j + a))
    return V
t = ('0','1')
nb_lignes = len(lab3[0])
nb_colonnes = len(lab3)
print(mystere(lab3, t))