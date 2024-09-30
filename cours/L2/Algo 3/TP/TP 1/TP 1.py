
# exrcice 1

def fact(n:int) -> int:
    if n == 0:
        return 1
    else:
        return n * fact(n-1)



def somme_factorielle(n: int) -> int:
    """
    >>> somme_factorielle(0)
    1
    >>> somme_factorielle(3)
    10
    """
    somme = 0
    for i in range(n+1):
        somme += fact(i)
    return somme
    
# exercice 2


def premier_repetition(liste:list[int]):
    """
    >>> lis = [1, 2, 3, 5, 7, 5, 2, 12, 1]
    >>> premier_repetition(lis)
    5
    """
    l = []
    for elt in liste:
        if elt in l:
            return elt
        else:
            l.append(elt)

# exercice 3

def print_diag_mat(matrice:list[list[int]]):
    """
    >>> l = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
    >>> print_diag_mat(l)
    1
    5 2
    9 6 3
    13 10 7 4
    14 11 8
    15 12
    16 
    
    """
    ligne = len(matrice)
    colonne = len(matrice[0])
    for col in range(colonne):
        i, j = 0, col
        while i < ligne and j >= 0:
            print(matrice[i][j], end=" ")
            i += 1
            j -= 1
        print()
    for lig in range(1, ligne):
        i, j = lig, colonne - 1
        while i < ligne and j >= 0:
            print(matrice[i][j], end=" ")
            i += 1
            j -= 1
        print()

            
# exercice 4

def intrus(liste:list[int]) -> int:
    """
    >>> l = [1, 2, 3, 5, 7, 5, 2, 1, 3]
    >>> intrus(l)
    7
    """
    l = []
    for elt in liste:
        if elt not in l:
            l.append(elt)
        else:
            l.remove(elt)
    return l[0]



# exercice 5


def intervalle_est_dans_liste(liste:list[int], min:int, max:int)-> bool:
    """
    >>> l = [4, 1, 2, 3, 5, 7, 5, 2, 1, 3, 6, 9]
    >>> intervalle_est_dans_liste(l, 1, 12)
    False
    >>> intervalle_est_dans_liste(l, 1, 7)
    True
    """
    i = min
    while i <= max:
        if i not in liste:
            return False
        i += 1
    return True


# exercice 6

def triplet_avec_ordre(liste:list[int]):
    """
    >>> l = [4, 0, 7, 3, 5, 7, 5, 2, 1, 3, 6, 9]
    >>> triplet_avec_ordre(l)
    (3, 5, 7)
    >>> l = [14, 12, 7, 5, 5, 3, 0]
    >>> triplet_avec_ordre(l)
    (-1, -1, -1)
    """
    minu = liste[0]
    tup = []
    i = 0
    while len(tup) <3 and i < len(liste):
        if liste[i] > minu:
            minu = liste[i]
            tup.append(i)
        i += 1

    if len(tup) >= 3:
        return (liste[tup[0]], liste[tup[1]], liste[tup[2]])
    else :
        return (-1, -1, -1)
    
            
    


if __name__ =="__main__":
    import doctest
    doctest.testmod(verbose = True)