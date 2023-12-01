
#|---------------------------------------|
#| name: tour de france                  |
#|---------------------------------------|


import math
import urllib
import json

def creation_dico_region(nom_fichier, encode='utf-8', sep=';'):
    """
    Création d'un dictionnaire :
    clé = nom de région
    valeur = liste des couples ('NOM_DE_VILLE', NOMBRE_HABITANTS)
    """
    dico = {}
    
    with open(nom_fichier, 'r', encoding=encode) as entree:
        for ligne in entree:
            ligne = ligne.rstrip()
            ligne = ligne.split(sep)
            region = ligne[1]
            ville = ligne[6]
            habitant = int(ligne[-1])
            if region not in dico:
                dico[region] = []
            couple = (ville, habitant)
            dico[region].append(couple)
    return dico



population = creation_dico_region('populations.csv')
print(population['Hauts-de-France'][972])

def ville_habitant_min(population):
    """
    Création d'une fonction retournant la ville ayant le nombre d'habitants le plus faible.
    
    param: dictionnaire
    return: tuple
    """
    habitant_max = ("X", math.inf)

    for ville in population:
        if ville[1] < habitant_max[1]:
            habitant_max = ville
        
    return habitant_max

population = creation_dico_region('populations.csv')

for region in population:
    print(ville_habitant_min(population[region]))

#------------------------|
#          URL           |
#------------------------|


def coordonnés_ville(ville):
    url = 'https://nominatim.openstreetmap.org/search?city={}&format=json&limit=1'.format(ville)
    rep = urllib.request.urlopen(url).read()
    rep = rep.decode('utf-8')
    rep = json.loads(rep)
    
    return rep (rep[0]["lon"], rep[0]["lat"])

print(coordonnés_ville("Douai"))
