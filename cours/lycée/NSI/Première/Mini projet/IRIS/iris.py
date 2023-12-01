#Créé par 1SI, le 04/04/2022 en Python 3.7

#|---------------------------------------|
#|                 IRIS                  |
#|---------------------------------------|


import collections


sepal_length = 0
sepal_width = 1
petal_length = 2
petal_width = 3
species = 4

def csv2list(liste):
    with open('iris.csv') as fichier:
        lignes = fichier.readlines()
        iris = []
        for ligne in lignes:
            liste = ligne.rstrip().split(',')
            iris.append(liste)
        return iris


def csv2tuple(liste):
    with open('iris.csv') as fichier:
        lignes = fichier.readlines()
        iris= ()
        for ligne in lignes:
            liste = ligne.rstrip().split(',')
            iris = (liste[0],liste[1],liste[2],liste[3],liste[4])
        return iris

def csv2dict(dico):
    with open('iris.csv') as fichier:
        lignes = fichier.readlines()
        iris = {}
        for i in range(len(dico)):
            iris = {'sepal_length':dico[i][0], 'sepal_width':dico[i][1], 'petal_length':dico[i][2], 'petal_width':dico[i][3], 'species': dico[i][4]}
        return iris






iris = csv2list('iris.csv')
iris1 = csv2tuple('iris.csv')
print(iris1[sepal_length])
print(iris1[species])
liste = csv2dict('iris.csv')
Iris = collections.namedtuple('Iris', 'sepal_length sepal_width petal_length petal_width species')




