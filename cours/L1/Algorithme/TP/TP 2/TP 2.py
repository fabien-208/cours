

#exercice 1

def somme_chiffres(n):
    """
    fonction qui permet de fair la somme de chiffres
    >>> somme_chiffres(1234)
    10
    """
    
    somme = 0
    for elt in str(n):
        somme += int(elt)
    return somme

# exercice 2

def conv(n):
    """convertit un int en liste"""
    liste = []
    n=str(n)
    for i in n:
        liste.append(int(i))
    print(liste)

def nombre_ordonne(n):
    """
    fonction qui test si le nombre est ordonne
    >>> nombre_ordonne(1234)
    True
    >>> nombre_ordonne(12342)
    False
    >>> nombre_ordonne(12234)
    True
    """
    l = conv(n)
    elementPrecedent = l[0]
    for element in l:
        if elementPrecedent>element :
            return False
        elementPrecedent=element   
    return True
        

# exercice 3


def est_voyelle_min(l):
    """
    fonction qui verifie si la chaine de caracteres passee en parametre est une voyelle minuscule.
    >>> est_voyelle_min("a")
    True
    >>> est_voyelle_min("z")
    False
    >>> est_voyelle_min("A")
    False
    >>> est_voyelle_min("aa")
    False
    """

    voyelle = ['a', 'e', 'i', 'o', 'u', 'y']
    if l in voyelle:
        return True
    return False

# exercie 4

def est_voyelle_maj(l):
    """
    fonction qui verifie si la chaine de caracteres passee en parametre est une voyelle majuscule.
    >>> est_voyelle_maj("a")
    False
    >>> est_voyelle_maj("G")
    False
    >>> est_voyelle_maj("A")
    True

    """
    voyelle = ['A', 'E', 'I', 'O', 'U', 'Y']
    if l in voyelle:
        return True
    return False


# exercie 5


def est_voyelle(l):
    """
    fonction qui verifie si la chaine de caracteres passee en parametre est une voyelle.
    >>> est_voyelle("a")
    True
    >>> est_voyelle("G")
    False
    >>> est_voyelle("A")
    True
    """

    voyelle = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']
    if l in voyelle:
        return True
    return False


#exercice 6



def compte_voyelles(l):
    """
    fonction qui compte le nombre de voyelle
    >>> compte_voyelles('Hello')
    2
    >>> compte_voyelles('les fonctions')
    4
    """

    compt = 0
    voyelle = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']
    for elt in l:
        if elt in voyelle:
            compt += 1
    return compt

# exercice 7


def est_majuscule(name):
    """
    >>> est_majuscule("a")
    False
    >>> est_majuscule("J")
    True
    >>> est_majuscule("?")
    False
    """
    if name.lower() != name:
        return True 
    return False

# exercice 8

def est_minuscule(name):
    """
    >>> est_minuscule("a")
    True
    >>> est_minuscule("J")
    False
    >>> est_minuscule("?")
    False
    """
    if name.upper() != name:
        return True 
    return False

# exercice 9

def est_lettre(l):
    """
    fonction qui verifient si la chaine de caractère est une lettre
    >>> est_lettre("a")
    True
    >>> est_lettre("G")
    True
    >>> est_lettre("#")
    False
    """
    if est_minuscule(l) or est_majuscule(l):
        return True
    return False

# exercice 10

def compte_maj(l):
    """
    fonction qui sort le nombre majuscule
    >>> compte_maj('IAMTheBest')
    5
    >>> compte_maj('ILovePython')
    3
    """
    compt = 0
    for elt in l:
        if est_majuscule(elt):
            compt +=1
    return compt

# exercice 11

def contient_une_minuscule(l):
    for elt in l:
        if est_minuscule(elt):
            return True
    return False


def contient_une_majuscule(l):
    for elt in l:
        if est_majuscule(elt):
            return True
    return False

def contient_un_caractere(l):
    carac = ['+','-','@','?','!','*','$']
    for elt in l:
        if elt in carac:
            return True
    return False


def contient_un_chiffre(l):
    
    chiffre = ['1','2','3','3','4','5','6','7','8','9','0']
    for elt in l:
        if elt in chiffre:
            return True
    return False


def teste_mdp(l):
    """
    fonction qui verifient si le mot de passe est valide
    >>> teste_mdp("Abracadabra62?")
    True
    >>> teste_mdp("Ab62?")
    False
    >>> teste_mdp("Abracadabra?")
    False
    >>> teste_mdp("abracadabra?")
    False
    """
    if len(l) >= 8:
        if contient_une_minuscule(l):
            if contient_une_majuscule(l):
                if contient_un_caractere(l):
                    if contient_un_chiffre(l):
                        return True
    return False


# exercice 12

def copie_sauf(mot, u):
    """
    >>> copie_sauf('bonjour', 'o')
    'bnjur'
    >>> copie_sauf('coucou', 'u')
    'coco'
    """
    copie = ''
    for elt in mot:
        if elt != u:
            copie += elt
    return copie

# exercice 13


def remplace(mot, u, v):
    """
    >>> remplace('ton', 't', 's')
    'son'
    >>> remplace('papa', 'a', 'i')
    'pipi'
    >>> remplace('papa', 'b', 'u')
    'papa'
    """
    copie = ''
    for elt in mot:
        if elt == u:
            copie += v
        else:
            copie += elt
    return copie


#exercice 14

def derniers(mot, n):
    """
    fonction qui retourneles dernière lettre d'un mot 
    >>> derniers('bonjour', 2)
    'ur'
    >>> derniers('bonjour', 3)
    'our'
    """
    m = len(mot)
    dernier = ''
    for i in range(n, 0, -1):
        dernier += mot[m - i]
    return dernier

# exercice 15

def min_to_maj(n):
    """
    >>> min_to_maj('r')
    'R'
    """
    return n.upper()

# exercice 16

def maj_to_min(n):
    """
    >>> maj_to_min('D')
    'd'
    """
    return n.lower()

# exercice 17

def majuscules(mot):
    """
    >>> majuscules('IAMTheBest')
    'IAMTHEBEST'
    """
    return mot.upper()

def minuscules(mot):
    """
    >>> minuscules('ILovePython')
    'ilovepython'
    """
    return mot.lower()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
