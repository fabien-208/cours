# question 1


def somme_inverse_carrees(n:int) -> float:
    """
    >>> somme_inverse_carrees(2)
    1.25
    """
    
    somme = 0
    for i in range(1, n+1):
        somme += 1/(i**2)
    return somme


# question 2

def n_premier_termes_suites(n:int) -> list[int]:
    """
    >>> n_premier_termes_suites(3)
    [1, 4, 13]
    """
    
    l =[1]
    for i in range(1, n):
        l.append(3*l[i-1]+1)
    return l

# question 3

def niemes_termes_suites(n:int):
    """
    >>> niemes_termes_suites(2)
    (4.48606797749979, 4.486046343663662)
    """
    u, v, w = 4, 5, 0
    for i in range(n):
        w = u
        u =(u+v)/2
        v = (w*v)**(1/2)
        
    return (u, v)


# question 4

def det(matrice:list[list[int]]) -> int:
    """
    >>> matrice = [[1,2],[3,4]]
    >>> det(matrice)
    -2
    """
    pass

# question 5 

def nb_occ(chaine, car, nb=0, x = 0):
    """
    >>> nb_occ('parapluie', 'a')"""
    if x == len(chaine):
        return nb
    else:
        if car == chaine[x]:
            nb_occ(chaine, car, nb+1, x+1)
        else:
            nb_occ(chaine, car, nb, x+1)


# question 6

def anagremme(mot, mot2, i=0):
    if 

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)