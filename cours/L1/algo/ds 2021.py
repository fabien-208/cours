
# exercice 1

# question 1

def minimum(l : list[int], dep : int)->list[int]:
    ind_min = dep
    mini = l[dep]
    for i in range(dep, len(l)):
        if l[i] < mini:
            mini = l[i]
            ind_min = i
    return ind_min


# question 2

def permuter(l:list[int], i:int, j:int):
    hnn = l[i]
    l[i] = l[j]
    l[j] = hnn
    return l


# question 3



def tri_par_minimum(l):
    for i in range(len(l)):
        min = minimum(l, i)
        permuter(l, min, i)
    return l


# exercice 2

# question 1


def est_voyelle(car: str)-> bool:
    voyelle = ['a','e','i','o','u','y']
    if len(car) > 1:
        return False
    return(car in voyelle)

# question 2



def javanais(l):
    liste = ''
    car = ''
    for elt in l:
        if est_voyelle(elt) and not est_voyelle(car): 
            liste += 'av'
        liste += elt
        car = elt
    return liste


# exercice 3

# question 1

def les_commestibles(dic):
    lescomes = []
    for elt in dic :
        if elt['comestible']:
            lescomes.append(elt)
    return lescomes

# question 2

def est_plus_grand(champ1, champ2):
    if champ1['taille'] > champ2['taille']:
        return True
    elif champ1['taille'] == champ2['taille']:
        return(champ1['largeur'] > champ2['largeur'])
    else:
        return False
    
    
# question 3

def par_famille(base):
    famille = {}
    for elt in base:
        if elt['famille'] not in famille:
            base[elt['famille']] = 1
        else:
            base[elt['famille']] += 1
    return base
                 
                 
