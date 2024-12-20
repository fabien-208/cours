
def algo (liste:list) -> int:
    
    dico = {}
    max_oc = 0
    for elt in liste:
        if elt in dico:
            dico[elt] += 1
        else:
            dico[elt] = 1
    for nb in dico.values():
        if nb > max_oc:
            max_oc = nb
    return max_oc


def puissance (n:int, k:int) -> int:
        if k == 0 :
             return 1
        res = n
        for i in range(k-1):
             res = res *n
        return res

            

def puissance_2 (x:int, k:int):
    if k == 0:
        return 1
    if k % 2 == 0:
        y = puissance_2( x, k//2)
        return y * y
    

def polynome(liste, x):
    res = 0
    for i in range(len(liste)):
          res += liste[i]*x**i
    return res




# exerice 8

def somme_egale_k(liste, k):
    assert(len(liste) > 1)
    i = 0
    j = len(liste) - 1
    while i < j:
        somme = liste[i] + liste[j]
        if somme == k:
            return (liste[i], liste[j])
        elif somme < k:
            i += 1
        else:
            j -= 1
    return None 