# Créé par 1SI, le 21/02/2022 en Python 3.7

#-----------------------------------------------------------------|
#                                                                 |
#                        #07_test_prog_synthese                   |
#                                                                 |
#-----------------------------------------------------------------|

#------------------------------------|
#            exercice 1              |
#------------------------------------|

#solution 1
prenom = input("saisir votre prénom")
print("Bonjour {} !".format(prenom))

#solution 2
print("Bonjour "+ prenom +" !")

#------------------------------------|
#            exercice 2              |
#------------------------------------|

annee_courante = 2022
naissance = int(input("saisir votre année de naisssance"))

#solution 1
print("votre age est : "+str(annee_courante-naissance))

#solution 2
print("votre age est : {}".format(annee_courante-naissance))

#solution 3
print("votre age est :", end=" ")
print(annee_courante-naissance)

#solution 4
print("votre age est :",annee_courante-naissance)

#------------------------------------|
#            exercice 3              |
#------------------------------------|

L =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#longeur ou nombre d élements
longeur = len(L)

#ajout de 1 à chaque élement
for n in range(longeur):
    L[n] += 1

#ajouter la valeur 11 a loa fin de la liste
L.append(11)

#ajouter les valeurs 12 et 13 a la fin de la liste
#solution 1
L.append(12)
L.append(13)

#solution 2
#L.extend([12, 13])

#afficher le premier élement, les deux premiers

print(L[0])
#solution 1
print(L[0],L[1])

#solution
print(L[:2])   # affiche une liste constitué des 2 premiers élement

#solution 2
for elt in L[:2]:
    print(elt, end=" ")

#affiche  le dernier , les deux derniers
print(L[-1])
print(L[-2])     #affiche avant dernier élement

#solution

for elt in L[-2:]:
    print(elt, end=" ")

#construire la liste "pairs" qui contient les chiffres pairs et
#une liste "impairs" qui contient les chiffres impairs

pairs= []
impairs = []
for elt in L:
    if elt %2 ==0:
        pairs.append(elt)
    else :
        impairs.append(elt)


#utiliser une structure de liste en compréhension pour répondre

paires_comp= [elt for elt in L if elt%2 ==0]
impairs_comp = [elt for elt in L if elt%2 !=0]


#ajouter la valeur 3,5 entre 3 et 4
#solution 1
L.insert(3,3.5)  # insert(index, valeur à insérer
#solution 2
L.insert(L.index(3)+1, 3.5)

#supprimer la valeur 3.5

L.remove(3.5)

#inverser l'ordre des elements
L.reverse()

#demander a l'utilkisateur de fournir un n,ombre au hasard
#et dirre si ce nombre est présent dans L
nombre = int (input("saisir un nombre"))

#solution 1
if nombre in L:
    print("le nombre est dans la liste")
else :
    print("le nombre n'est pas dans la liste")

#solution 2
message ="nombre dans la liste"if nombre in L else "nombre pas dans la liste"
print(message)


#------------------------------------|
#            exercice 4              |
#------------------------------------|


d = {'nom':'Dupuis','prenom':'jacque','age':30}

#affichage de la valeur de la clé: prenom

print(d['prenom'])
d['prenom'] = 'Jacques'
print(d['prenom'])

#afficher des tuples (cle, valeur du dictionnaire)

for cle in d.items():
    print(cle)

#afficher les cle du dictionnaire


for cle in d.keys():
    print(cle)

#afficher les valeurs du dictionnaire

for valeurs in d.values():
    print(valeurs)

#ecrire la phrase "Jacques dupuis a 30 ans

print(d['prenom'], d['nom'],"a", d['age'], "ans")

print("{} {} a {} ans".format(d['prenom'],d['nom'],d['age']))

#------------------------------------|
#            exercice 5              |
#------------------------------------|

import string
caractere = input("saisir un caractère")
if caractere in string.ascii_letters :
    if caractere in string.ascii_lowercase:
        message = "lettres minuscules "
    else :
        message =" lettres majuscules"
elif caractere in string.digits:
    message = "chiffres "
else :
    message = "inconnu"

print(message)


#------------------------------------|
#            exercice 6              |
#------------------------------------|

from random import randint
nb_alea = randint(1,100)
jeu = True

while jeu :
    nombre =int(input("saisir un nombre entre 1 et 100 "))
    while nombre <1 or nombre >100:
        nombre =int(input("saisir un nombre entre 1 et 100 "))
    if nombre == nb_alea:
        message = "Gagné !"
        jeu = False
    elif nombre<nb_alea:
        message = "nombre trop grand !"
    else :
        message = "nombre trop grand !"
    print(message)
print("le nombremystere est bien : ", nb_alea)



#------------------------------------|
#            exercice 7              |
#------------------------------------|

from math import pi

def SurfaceCercle(rayon):
    """
    permet de calculer la surface d'un cercle.
    param: rayon(float ou int) positif
    return:surfacecercle(float)
    >>> SurfaceCercle(2.5)
    19.634954084936208
    """
    #test de pré-condition
    assert rayon>=0, "rayon négatif"

    surfacecercle = pi *rayon *rayon
    return surfacecercle


#------------------------------------|
#            exercice 8              |
#------------------------------------|



def nbOccurences(caractere, phrase):
    """
    retourne le nombre de fois ou le "caractere" est présent dans la "phrase"
    param: caractere (str)
    param: phrase (str)
    return: cpt (int)
    >>>nbOccurences("e", Combien y a t'il de e dans cette phrase
    6
    """
    cpt =0
    for c in phrase:
        if c == caractere:
            cpt+=1

    return cpt




if __name__=="__main__":
    import doctest
    doctest.testmod(verbose = True)


