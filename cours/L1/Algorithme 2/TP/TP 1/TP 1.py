import math

# Exercice 1

def distance(point1: tuple, point2: tuple)-> float:
    return math.sqrt((point1[0]- point2[0])**2 + (point1[1]- point2[1])**2)



def perimetre(figure:list[tuple[int]]) -> float:
    peri = 0
    for i in range(len(figure)-1):
        peri += distance(figure[i], figure[i+1])
    peri += distance(figure[-1], figure[0])
    return peri


def max_distance(figure:list[tuple[int]]) -> float:
    max_dist = 0
    for i in range(len(figure)):
        for j in range(len(figure)):
            if distance(figure[i], figure[j]) > max_dist:
                max_dist = distance(figure[i], figure[j])
    return max_dist
        
    
    
# Exercice 2



livre1 = {"Auteur": "Sartre", "Annee":19964, "Titre": "Les mots","Prix":13.5, "Quantité":20}
livre2 = {"Auteur": "Simon Veil", "Annee":2007, "Titre":"Une vie", "Prix":15, "Quantité":35}
livre3 = {"Auteur": "Rousseau", "Annee":1770, "Titre":"Les confessions", "Prix":13.5, "Quantité":45}
livre4 = {"Auteur": "Zola", "Annee":1861, "Titre":"Perrette", "Prix":11.5, "Quantité":51}
livre5 = {"Auteur": "De Musset", "Annee":1849, "Titre":"Louison", "Prix":11, "Quantité":34}

catalogue = {"Autobiographie":[livre2, livre3], "Roman":[livre1],"Pièces de théâtre":[livre4, livre5]}

def ajoute_livre(auteur, annee, titre, quantité, genre, catalogue):
    if genre not in catalogue:
        catalogue[genre] = []
    return catalogue[genre].append({"Auteur": auteur, "Annee": annee, "Titre":titre, "Quantité": quantité})


def estpresent(catalogue, titre):
    for genre in catalogue:
        for livre in genre:
            if titre == livre['Titre']:
                return True
    return False 


def affiche_livre(livre):
    print("'Auteur': {}".format(livre['Auteur']) + '\n' + "'Titre': {}".format(livre['Titre'])+ '\n' + "'Titre': {}".format(livre['Titre'])+ '\n' + "'Prix': {}".format(livre['Prix'])+ '\n' + "'Quantité': {}".format(livre['Quantité']))



def changer_prix(livre , prix):
    livre['Prix'] = prix
    
    
def ajoute_quantité(catalogue, titre, quantité):
    for genre in catalogue:
        for livre in genre:
            if livre['Titre'] == titre:
                livre['Quantité'] += quantité
                
                
                
def livre_auteur(nom_auteur, catalogue):
    liste_livre = []
    for genre in catalogue:
        for livre in genre:
            if livre['Auteur'] == nom_auteur:
                liste_livre.append(livre['Titre'])
    return liste_livre




def livre_anne(catalogue, date):
    liste_livre = []
    for genre in catalogue:
        for livre in genre:
            if livre['Annee'] == date:
                liste_livre.append(livre['Titre'])
    return liste_livre


def les_plus_chers(catalogue):
    liste = []    
    for genre in catalogue:
        max = 0
        for livre in genre:
            if livre['Prix'] > max:
                max = livre['Prix']
                livr = livre['Titre']
        liste.append(livr)
    return liste



def genre_littéraire(auteur, catalogue):
    liste = []
    for genre in catalogue:
        for livre in genre:
            if livre['Auteur'] == auteur:
                liste.append(genre)
    return liste
        
