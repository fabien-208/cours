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
    n = len(matrice)
    
    if n == 1:
        return matrice[0][0]
    
    deter = 0
    for i in range(n):
        sous_matrice = [row[1:] for j, row in enumerate(matrice) if j != i]
        
        deter += (-1) ** i * matrice[i][0] * det(sous_matrice)
    
    return deter

# question 5 

def nb_occ(chaine, car, nb=0, x = 0):
    """
    >>> nb_occ('parapluie', 'a')
    2
    """
    if x == len(chaine):
        return nb
    else:
        if car == chaine[x]:
            nb_occ(chaine, car, nb+1, x+1)
        else:
            nb_occ(chaine, car, nb, x+1)
    


# question 6

def anagramme(mot, mot2):
    """
    >>> anagramme("chien", "niche") 
    True
    >>> anagramme("rat", "tarte")
    False
    """

    if len(mot) != len(mot2):
        return False
    if len(mot) == 0 and len(mot2) == 0:
        return True
    if mot[0] in mot2[-1]:
        return anagramme(mot[1:], mot2)
    else:
        return False
    


# question 7

def Syracuse(N):
    """
    >>> Syracuse(10000000)
    1000
    """
    nb = 0
    while N != 0:
        if N % 2 == 0:
            N = 3 * N + 1
            nb += 1 
        else: 
            N = N / 2
    return nb


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)