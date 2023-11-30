## exercice 1

def plateau(l):
    """
    plateau([1, 2, 2, 1, 1, 1, 1, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 1, 1, 1, 1])
    (2, 6)
    """
    val_courante = l[0]
    nb_occurence_val = 1
    val_maximale = l[0]
    nb_occurence_max = 1
    if len(l) == 0:
        return None, 0
    for i in range(1, len(l)):
        if l[i] == val_courante:
            nb_occurence_val +=1
            if nb_occurence_val > nb_occurence_max:
                val_maximale, nb_occurence_max = val_courante, nb_occurence_val
        else:
            val_courante, nb_occurence_val = l[i], 1
    return (val_maximale, nb_occurence_max)
    
 
## exercice 2


def decompresse(l):
    liste = []
    for i in range(len(l)):
        for j in range(l[i][0]):
            liste.append(l[i][1])
    return liste

## exercice 3

def compresse(liste):
    ll = []
    nb_occ = 1
    for i in range(len(liste)-1):
        if liste[i] == liste[i+1]:
            nb_occ += 1
        else :
            ll.append([nb_occ, liste[i]])
            nb_occ = 1
        if i == len(liste):
            ll.append(nb_occ, liste[i-1])
    return ll
            
            
def compresse2(l):
    occ = 1
    elt = l[0]
    ll =[]
    for i in range(1, len(l)):
        if l[i] != elt:
            ll.append([occ, elt])
            elt = l[i]
            occ =1
        else :
            occ += 1
        if i == len(l) -1:
            ll.append([occ, elt])
    return ll
              

# exercice 4

    
        
def drapeau1(l):
    liste = []
    nb_1 = 0
    nb_0 = 0
    nb_2 = 0
    for i in range(len(l)):
        if l[i] == 0:
            nb_0 += 1
        elif l[i] == 1:
            nb_1 += 1
        elif l[i] == 2:
            nb_2 += 1
    for k in range(nb_0):
        liste.append(0)
    for s in range(nb_1):
        liste.append(1)
    for d in range(nb_2):
        liste.append(2)
    return liste
        
        
        
#exercice 5

# def drapeau(l):
#     i = 0
#     j = len(l)-1
#     elt  = ''
#     u = len(l)% 2
#     while i != j:
#         if l[i] == 0:
#             i += 1
#         elif l[i] == 2:
#             elt = l[j]
#             l[j] = l[i]
#             l[i] = elt
#             j -= 1
#         elif l[i] == 1:
#             elt = l[u]
#             l[u] = l[i]
#             l[i] = elt
#     return l


def drapeau(l):
    ind_cour = 0
    ind0 = 0
    ind2 = len(l)-1
    for i in range(len(l)):
        if ind_cour == 0 and ind0 > ind_cour:
            l[ind_cour] = l[ind0]
            l[ind0] = 0
            ind0 += 1
        elif ind_cour == 2:
            l[ind_cour] = l[ind2]
            l[ind2] = 2
            ind2 -= 1
        else:
            ind_cour += 1
    return l
    
        
        
        
        
        