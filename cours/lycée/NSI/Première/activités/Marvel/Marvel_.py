# Créé par 1SI, le 07/03/2022 en Python 3.7

import csv
with open("bd_marvel.csv","r", encoding="utf-8") as data:
    table= list(csv.DictReader(data, delimiter=';'))
    for ligne in table:
        print(ligne)

print(table[0]['Original Title'])
print(type(table[0]['Original Title']))
table[0]['Sortie']=int(table[0]['Sortie'])
print(table[0]['Sortie'])
print(type(table[0]['Sortie']))
#---------------------------------------|
#               exercice                |
#---------------------------------------|
un_dico=ligne
def validation(un_dico):
    """
    prend en entré un dictionnaire de la table
    et retourne un dictionnaire valide
    param:un dictionnaire
    return:un dictionnaire
    """

    identifiant=int(un_dico['id'])
    titre=un_dico['Original Title']
    company=un_dico['Company']
    note=float(un_dico['Note'])
    if note>10 or note<0:
        exit("Note invalide dans le fichier")
    score=un_dico['Score']
    duree=float(un_dico['Durée'])
    sortie=un_dico['Sortie']
    budget=float(un_dico['Budget'])
    week=int(un_dico["Weekend d'ouverture USA"])
    usa=int(un_dico['USA'])
    monde= int(un_dico['Monde'])
    return{ 'Id': identifiant,'Titre' :titre,'Company':company,'Note': note,'Score':score,'Durée':duree,'Sortie':sortie,'Budget':budget,"Weekend d'ouverture USA":week,'USA':usa,'Monde':monde}

print(validation(un_dico))

def present(titre, table):
    """
    permet de savoir si le film est dans la table
    """
    if titre in  table:
        print("le film est dans la table")
    else:
        print("le film n'est pas dans la liste")


