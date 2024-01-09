import math

## exercice 1
def aire_triangle(h):
    """ fonction qui permet de calculer l'aire d'un triangle"""
    return (h**2*math.sqrt(3))/4

## exercice 2

def etoile_six_branches(h):
    """ fonction qui permet de calculer l'aire d'une étoile a six branche"""
    a = (1/3)*h
    return aire_triangle(a)*12

## exercice 3

def dimension_mur(longeur,largeur,  hauteur):
    dim = (longeur*hauteur)*2 + (largeur*hauteur)*2
    return dim

def dimension_plafond(longeur, largeur):
    return largeur * longeur

def dimension_a_peindre(longeur, largeur, hauteur):
    return dimension_mur(longeur, largeur, hauteur) + dimension_plafond(longeur, largeur)

def nb_pots_de_peinture(longeur, largeur, hauteur):
    dim = dimension_a_peindre(longeur, largeur, hauteur)
    contenance = 5
    un_litre_couvre = 3
    return "il faut {} pots de peinture".format(dim/(contenance*un_litre_couvre))

## exercice 4
"""
>>> a= 6
>>>type(a)
<class 'int'>
>>>b = a / 4
>>>type(b)
<class 'float'>
>>>nom = "Dupont"
>>>type(nom)
<class 'str'>
>>>condi = a < b
>>>type(condi)
<class 'bool'>
"""

## exercice 5

def annee_bissextile(annee):
    """
    fonction qui permet de savoir si une année est bissextile
    
    >>> annee_bissextile(2020)
    True
    >>> annee_bissextile(2021)
    False
    >>> annee_bissextile(2000)
    True
    >>> annee_bissextile(2100)
    False
    """
    
    if annee % 4 == 0 and annee % 100 !=0:
        return True
    elif annee % 400 == 0:
        return True
    return False


## exercice 6

def nbre_jours_mois(mois, annee):
    """
    fonction qui permet de savoir le nombre de jours d'un mois
    >>> nbre_jours_mois(2,2020)
    29
    >>> nbre_jours_mois(2,2021)
    28
    >>> nbre_jours_mois(7,2021)
    31
    >>> nbre_jours_mois(9,2021)
    30
    """
    
    if mois == 2:
        if annee_bissextile(annee) == True:
            return 29
        return 28
    else:
        if mois in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        return 30
    
    
## exercice 7


def numero_jour(jour, mois , annee):
    """
    fonction qui permet de savoir le numéro du jour dans l'année
    >>> numero_jour(14,9,2020)
    258
    """
    
    nb_jour = 0
    for i in range(1, mois):
        nb_jour += nbre_jours_mois(i, annee)
    nb_jour += jour
    return nb_jour


## exercice 8

def nbre_jours_debut_ere(annee):
    """
    fonction qui donne le nombre de jours depuis le debut de l’ere chretienne
    >>> nbre_jours_debut_ere(1)
    365
    >>> nbre_jours_debut_ere(2020)
    737790
    """
    
    nb_jours = 0
    for i in range(1,annee + 1):
        if annee_bissextile(i):
            nb_jours += 366
        else:
            nb_jours += 365
    return nb_jours

## exercice 9

def nbre_jours_debut_ere_jma(jour,mois, annee):
    """
    fonction qui donne le nombre de jours depuis le debut de l’ere chretienne pour une date donnée
    >>> nbre_jours_debut_ere_jma(5,2,2020)
    737460
    """
    if annee_bissextile(annee):
        return (nbre_jours_debut_ere(annee) - 366) + numero_jour(jour, mois, annee)
    return (nbre_jours_debut_ere(annee) - 365) + numero_jour(jour, mois, annee)
    

## exercie 10

def nbre_jours_entre_deux_dates(jours, mois, annee, jours2, mois2, annee2):
    """
    >>> nbre_jours_entre_deux_dates(5,2,2020,14,9,2020)
    222
    >>> nbre_jours_entre_deux_dates(5,2,2020,14,9,2021)
    587
    >>> 587 - 222
    365
    """
    nb = nbre_jours_mois(mois, annee)-jours+jours2
    for i in range(12 - mois):
        nb = nb+nbre_jours_mois(mois+i,annee)
    for j in range(12 - mois2 + 1):
        nb = nb-nbre_jours_mois(mois2+jours2, annee2)
    if annee_bissextile(annee)!=True:
        nb = nb-1
    while annee != annee2:
        if annee_bissextile(annee):
            nb = 366+ nb
        else:
            nb = 365+ nb
        annee = annee+1
    return nb

## exercice 11

def suivant_syracuse(n):
    """
    >>> suivant_syracuse(5)
    16
    >>> suivant_syracuse(2)
    1
    """

    if n % 2 == 0:
        val = n//2
    else:
        val = 3 * n + 1
    return val
      
##exercice 12

def nb_etapes_syracuse(n):
    """
    >>> nb_etapes_syracuse(5)
    5
    >>> nb_etapes_syracuse(11)
    14
    """
    v = suivant_syracuse(n)
    nb_etape = 1
    while v !=1:
        v = suivant_syracuse(v)
        nb_etape += 1
    return nb_etape

## exercice 13

def altitude_syracuse(n):
    
    """
    >>> altitude_syracuse(11)
    52
    >>> altitude_syracuse(5)
    16
    """
    max = n
    v = suivant_syracuse(n)
    if v >= max:
        max = v
    while v != 1:
        v = suivant_syracuse(v)
        if v >= max:
            max = v
    return max    
    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

