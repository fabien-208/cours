
# exercice 1

def arongement(n, k):
    res = 1
    for i in range (k):
        res = res * (n-1)
    return res


# exercice 2

def est_dans(cha, ind, chb):
    if len(chb) +ind > len(cha):
        return False
    for i in range(len(cha)):
        if cha[i] != chb[i +ind]:
            return False
    return True

def rechercher_remplacer(texte, ancien, nouv):
    res = ''
    ind = 0
    while ind < len(texte):
        if est_dans(ancien,ind , nouv):
            res += nouv
            ind += len(ancien)
        else:
            res += texte[i]
            ind += 1
    return res