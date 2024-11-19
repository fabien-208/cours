
from  random import randint

def fusionner(liste1, liste2):
    if not liste1:
        return liste2
    if not liste2:
        return liste1
    if liste1[0] < liste2[0]:
        return [liste1[0]] + fusionner(liste1[1:], liste2)
    else:
        return [liste2[0]] + fusionner(liste1, liste2[1:])



def tri_par_dénombrement(liste):
    k = max(liste)
    tr = [0] * (k + 1)
    
    for num in liste:
        tr[num] += 1
    
    res = []
    for i in range(k + 1):
        res.extend([i] * tr[i])
    
    return res

def tri_a_bulles_rec(liste, n):
    if len(liste) <= 1:
        return n
    for i in range(n - 1):
        if liste[i+1] < liste[i]:
            liste[i], liste[i+1] = liste[i+1], liste[i]
    tri_a_bulles_rec(liste, n - 1)

def tri_a_peigne(liste, k):
    for i in range(len(liste) - 1):
        j  = 0
        while j + k < len(liste):
            if liste[j+k] < liste[j]:
                liste[j], liste[j+k] = liste[j+k], liste[j]
            j = j+k
        k = k-1
        if k <1:
            k = 1



def tri_fusion(liste):
    if len(liste) <= 1:
        return liste
    else:
        milieu = len(liste) // 2
        gauche = tri_fusion(liste[:milieu])
        droite = tri_fusion(liste[milieu:])
        return fusionner(gauche, droite)

def main():
    liste1 = [1, 3, 5, 7, 9]
    liste2 = [2, 4, 6, 8, 10]
    print(fusionner(liste1, liste2))
    liste = [randint(0, 25) for _ in range(30)]
    print(liste)
    print(tri_par_dénombrement(liste))



main()