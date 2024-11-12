# question 2


def trouver_couple(lis, k):
    """
    >>> trouver_couple([1,2,3,4], 6)
    (1, 3)
    >>> trouver_couple([1,2,3,4], 8)
    (-1, -1)
    """
    for i in range(len(lis)):
        for j in range(i+1, len(lis)):
            if lis[i] + lis[j] == k:
                return (i, j)
    return (-1, -1)

# question 3


def suite_Un(n):
    """
    >>> suite_Un(3)
    2.25
    """
    vf  = 1
    res = 0
    u0 , u1 = 3, 2
    while vf < n:
        res = (u1 + u0) / 2
        vf += 1
        u0 = u1
        u1 = res
    return res


def suite_Un_REC(n):
    """
    >>> suite_Un_REC(3)
    2.25
    """
    if n == 0:
        return 3
    if n == 1:
        return 2
    else:
        return (suite_Un_REC(n-1) + suite_Un_REC(n-2)) /2



 # question 4


def fussioner_trois_liste(lis_1, lis_2, lis_3):
    """
    >>> lis1 = [1, 3, 5, 7, 9]
    >>> lis2 = [2, 4, 6, 8, 10]
    >>> lis3 = [1, 2, 3, 4, 5]
    >>> fussioner_trois_liste(lis1, lis2, lis3)
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10]
    """

    i, j, k = 0, 0, 0
    liste = []
    while i < len(lis_1) and j < len(lis_2) and k < len(lis_3):
        if lis_1[i] < lis_2[j]:
            if lis_1[i] < lis_3[k]:
                liste.append(lis_1[i])
                i += 1
            else:
                liste.append(lis_3[k])
                k += 1
        elif lis_2[j] < lis_3[k]:
            liste.append(lis_2[j])
            j += 1
        else:
            liste.append(lis_3[k])
            k +=1

    if i != len(lis_1)-1:
        while i < len(lis_1):
            liste.append(lis_1[i])
            i+=1
    
    if j != len(lis_2)-1:
        while j < len(lis_2):
            liste.append(lis_2[j])
            j+=1

    if k != len(lis_3)-1:
        while k < len(lis_3):
            liste.append(lis_3[k])
            k+=1

    return liste



# question 5

def 



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)