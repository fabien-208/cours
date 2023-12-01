# Créé par 1SI, le 02/05/2022 en Python 3.7

##|---------------------------------------|
##|                   KNN                 |
##|---------------------------------------|

##|---------------------------------------|
##|              exercice 1               |
##|---------------------------------------|

from math import *

Jean = (35,35,3,0)
Louis = (22,50,2,1)
Anne = (63,200,1,0)
Suzanne = (59,170,1,0)
Nicolas = (25,40,4,1)
David = (37,50,2,0)

def distance_cible(donné, cible):
    distance = sqrt((cible[0]-donné[0])**2+(cible[1]-donné[1])**2)
    return distance


##|---------------------------------------|
##|              exercice 2               |
##|---------------------------------------|

def plus_proche_voisin(table, cible, k):
    distance_donné = []
    for i in range(len(table)):
        distance = distance_cible(table[i], cible)
        distance_donné.append((distance, table[i]))
    table_trié = sorted(distance_donné)
    proche_voisin = []
    for i in range(k):
        proche_voisin.append(table_trié[i])
    return proche_voisin




table = [[1,28,'t1'],[3,27.2,'t1'],[8,37.6,'t1'],[13,40.7,'t1'],[2,30,'t2'],[3,26,'t2'],[10,9,'t2'],[15,35.5,'t2']]
cible = [7,28.4]
k = 3

print("la liste des",k," plus proche voisin de la cible:",plus_proche_voisin(table, cible, k))

##|---------------------------------------|
##|              exercice 3               |
##|---------------------------------------|

import matplotlib.pyplot as plt

liste_x_1=[table[i][0] for i in range(len(table)) if table[i][2]=='t1']
liste_y_1=[table[i][1] for i in range(len(table)) if table[i][2]=='t1']


liste_x_2=[table[i][0] for i in range(len(table)) if table[i][2]=='t2']
liste_y_2=[table[i][1] for i in range(len(table)) if table[i][2]=='t2']
plt.axis([0,15, 0, 50])
plt.axis('equal')
plt.xlabel('Caractéristique 1')
plt.ylabel('Caractéristique 2')
plt.title('Représentation des deux types')
plt.grid()
plt.scatter(liste_x_1,liste_y_1, label='type 1')
plt.scatter(liste_x_2,liste_y_2, label='type 2')
plt.scatter(cible[0],cible[1], label='cible')
plt.legend()
plt.show()
##|---------------------------------------|
##|              exercice 4               |
##|---------------------------------------|


def distance_manhattan(distance, cible):
    dist =abs(cible[0]-donné[0])+abs(cible[1]-donné[1])
    return dist

