import time

# ------------------- Exercice 1 -------------------


def somme_n_entier(n):
    somme = 0
    for i in range(1, n+1):
        somme += i
    return somme


#²------------------- Exercice 2 -------------------

# question 1

def mini(liste):
    min = liste[0]
    for elt in liste:
        if elt < min:
            min = elt
    return min


def maxi(liste):
    max = liste[0]
    for elt in liste:
        if elt > max:
            max = elt
    return max


# question 2

def minmax(liste):

    min = liste[0]
    max = liste[0]
    comparisons = 0  # Compteur de comparaisons

    for elt in liste[1:]:
        comparisons += 1
        if elt < min:
            min = elt
        comparisons += 1
        if elt > max:
            max = elt

    return (min, max), comparisons


# ------------------- Exercice 3 -------------------


def division_euclidienne(a, b):
    q = 0
    r = a
    while r >= b:
        q += 1
        r -= b
    return q, r


def division_euclidienne_decimale(a, b):
    q = 0
    r = a
    while r >= b:
        q += 1
        r -= b
    r = r * 10
    while r >= b:
        q += 1
        r -= b
    return q, r


def division_euclidienne_binaire(a, b):
    q = 0
    r = a
    while r >= b:
        q += 1
        r -= b
    r = r * 2
    while r >= b:
        q += 1
        r -= b
    return q, r

# ------------------- Exercice 4 -------------------

def no2slash(name):
    l = list(name)
    x = 1
    while x < len(l):
        if (l[x-1] == '/') and (l[x] == '/'):
            for y in range(x+1, len(l)):
                l[y-1] = l[y]
            l = l[:-1]
        else:
            x += 1
    return ''.join(l)


def no2slash_linear(name):
    result = []
    prev_char = None
    for char in name:
        if not (char == '/' and prev_char == '/'):
            result.append(char)
        prev_char = char
    return ''.join(result)


# ------------------- TEST -------------------


print("\n Exercice 1")
start = time.time()
somme_n_entier(10000)
end = time.time()
print("\nle temps d'execution de somme_n_entier est : ",  end - start)
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\n Exercice 2")
start = time.time()
mini(lis)
end = time.time()
print("\nle temps d'execution de mini() est : ",  end - start)
start = time.time()
maxi(lis)
end = time.time()
print("\nle temps d'execution de maxi() est : ",  end - start)
resultat, nb_comparaisons = minmax(lis)
print("\nle nombre de comparaisons de minmax() est : ", nb_comparaisons)

print("\n Exercice 3")
start = time.time()
division_euclidienne(10, 3)
end = time.time()
print("\nle temps d'execution de division_euclidienne() est : ",  end - start)
start = time.time()
division_euclidienne_decimale(10, 3)
end = time.time()
print("\nle temps d'execution de division_euclidienne_decimale() est : ",  end - start)
start = time.time()
division_euclidienne_binaire(10, 3)
end = time.time()
print("\nle temps d'execution de division_euclidienne_binaire() est : ",  end - start)

print("\n Exercice 4")
name = "bonjour//tout//le//monde//comment//ca//va"
start = time.time()
no2slash(name)
end = time.time()
print("\nle temps d'execution de no2slash() est : ",  end - start)
start = time.time()
no2slash_linear(name)
end = time.time()
print("\nle temps d'execution de no2slash_linear() est : ",  end - start)