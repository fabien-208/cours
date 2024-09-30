

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


def n_premiers_termes_suite(n:int) -> list[int]:
    """
    >>> n_premiers_termes_suite(3)
    [1, 4, 13]
    """
    lis = [1]
    for i in range(n-1):
        lis.append(3*lis[i]+1)
    return lis



# question 3 


def nieme_terme_suite(n:int) -> tuple[float, float]:
    """
    >>> nieme_terme_suite(3)
    (4.875, 5)
    """

    v, u = 5, 4
    for i in range(n):
        u, n = (u + v)/2, (u * v)**(1-2) # type: ignore
    return(u, v)



# question 5

def nb_occ(chaine, car, n=0):
    if chaine[]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)