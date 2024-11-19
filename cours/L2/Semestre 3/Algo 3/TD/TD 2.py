from math import factorial


# exerice 1

def nb_chiffres(n, nb = 0):
    if n == 0:
        return nb
    else:
        return nb_chiffres(int(n/10), nb+1)
    

# exerice 2

def somme_chiffres(n, nb = 0):
    if n ==0:
        return nb
    else:
        return somme_chiffres(int(n/10), nb + (n%10))

# exerice 3

def conversion_binaire(n, res = ''):
    if n == 0:
        return res
    else:
        res = '{}'.format(n%2) + res
        return conversion_binaire(n//2, res)


# exercice 4

def palindrome(txt):
    if len(txt) == 0 or len(txt) == 1:
        return True
    else:
        if txt[0] != txt[-1]:
            return False
        else:
            return palindrome(txt[1:-1]) 


# exerice 5


def nb_occ_mot(txt, mot):
    if len(txt) < len(mot):
        return False
    if mot == txt[:len(mot)]:
        return 1 + nb_occ_mot(txt[1:], mot)
    return nb_occ_mot(txt[1:], mot)

# exercice 6

def inverse_chaine(txt, res = ''):
    if len(txt) == 0:
        return res
    else:
        return inverse_chaine(txt[:-1], res + txt[-1])
    

# exerice 7

def nb_premiers(n):
    if n == 1:
        return [1]
    if est_premiers(n):
        return nb_premiers(n-1) + [n]
    return nb_premiers(n-1)


def est_premiers(n):
    if n <= 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# exercice 8

def communs(l1, l2, l3 = []):
    if len(l1) == 0 or len(l2) == 0:
        return l3
    else:
        if l1[0] in l2:
            l3.append(l1[0])
        return communs(l1[1:], l2, l3)


# exerice 9


def permutations(lis):
    pass



# exercice 10

def coef_binomial(n , k):
    return factorial(n)/(factorial(k)*factorial(n-k))





# |--------------------------------------------|
# |                    test                    |
# |--------------------------------------------|


def main():
    print(nb_chiffres(12034))
    print(somme_chiffres(12034))
    print(conversion_binaire(25))
    print(palindrome('python'))
    print(palindrome('ABBA'))
    print(nb_occ_mot( 'voiture velo voiture velo voiture', 'voiture'))
    print(inverse_chaine('python'))
    print(nb_premiers(100))
    print(communs([1, 3, 10, 12, 27], [2, 3, 11, 12, 27]))
    print(coef_binomial(24, 12))



main()