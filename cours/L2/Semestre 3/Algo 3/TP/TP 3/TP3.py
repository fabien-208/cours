from random import randint

# exercice 1

def tri_selection(tab):
    for i in range(len(tab)):
        min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[min]:
                min = j
        tab[i], tab[min] = tab[min], tab[i]
    return tab

def tri_insertion(tab):
    for i in range(1, len(tab)):
        x = tab[i]
        j = i
        while j > 0 and tab[j-1] > x:
            tab[j] = tab[j-1]
            j = j - 1
        tab[j] = x
    return tab

def tri_bulle(tab):
    for i in range(len(tab)):
        for j in range(0, len(tab)-i-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab


# exercice 4




def tri_piles(tab):
    piles1 = tab[:]
    piles2 = []
    piles3 = []

    while piles1:
        min = piles1.pop()
        while piles2 and piles2[-1] < min:
            piles1.append(piles2.pop())
        piles2.append(min)

    while piles2:
        piles3.append(piles2.pop())

    return piles3


# exerice 5

def tri_fusion(tab):
    if len(tab) > 1:
        mid = len(tab)//2
        ga = tab[:mid]
        dr = tab[mid:]
        tri_fusion(ga)
        tri_fusion(dr)
        i = j = k = 0
        while i < len(ga) and j < len(dr):
            if ga[i] < dr[j]:
                tab[k] = ga[i]
                i += 1
            else:
                tab[k] = dr[j]
                j += 1
            k += 1
        while i < len(ga):
            tab[k] = ga[i]
            i += 1
            k += 1
        while j < len(dr):
            tab[k] = dr[j]
            j += 1
            k += 1

    return tab

# exerice 7


def tri_mixte(tab, k):
    
    liste = [tab[i::k] for i in range(k)]
    for i in range(k):
        liste[i] = tri_insertion(liste[i])
    res = []
    indices = [0] * k
    
    while len(res) < len(tab):
        min_val = float('inf')
        min_idx = -1
        for i in range(k):
            if indices[i] < len(liste[i]) and liste[i][indices[i]] < min_val:
                min_val = liste[i][indices[i]]
                min_idx = i
        res.append(min_val)
        indices[min_idx] += 1
    
    return res

# exerice 8

def tri_chaine(str:str) -> str:
    if len(str) < 2:
        return str
    else:
        mid = len(str) // 2
        left = tri_chaine(str[:mid])
        right = tri_chaine(str[mid:])
        return (left + right)
    

# exerice 10

def tri_shaker(tab):
    for i in range(len(tab)):
        for j in range(0, len(tab)-i-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
        for j in range(len(tab)-i-1, 0, -1):
            if tab[j] < tab[j-1]:
                tab[j], tab[j-1] = tab[j-1], tab[j]
    return tab


# exerice 11

def tri_rapide(tab):
    if len(tab) <= 1:
        return tab
    else:
        pivot = tab.pop()
        inf = [i for i in tab if i <= pivot]
        sup = [i for i in tab if i > pivot]
        return tri_rapide(inf) + [pivot] + tri_rapide(sup)


# exercice 13

def partition(tab, min, max):
    pivot = tab[max]
    i = min - 1
    for j in range(min, max):
        if tab[j] <= pivot:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[max] = tab[max], tab[i + 1]
    return i + 1

def tri_rapide_recursive(tab, min, max):
    if min < max:
        pi = partition(tab, min, max)
        tri_rapide_recursive(tab, min, pi - 1)
        tri_rapide_recursive(tab, pi + 1, max)
    return tab


def main():
    tab = [randint(0, 100) for i in range(100)]
    print(tri_selection(tab))
    print(tri_insertion(tab))
    print(tri_bulle(tab))
    print(tri_piles(tab))
    print(tri_fusion(tab))
    print(tri_mixte(tab, 5))
    print(tri_shaker(tab))
    print(tri_rapide(tab))


main()