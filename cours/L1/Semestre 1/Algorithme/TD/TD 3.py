## exercice 7
nb_etages = 11
taille_ascenseur = 13
bouton_ascenseur = [2, 3, 5, -4, -11]

# 1

def commence_et_se_temine_par_0(l:list[int])-> bool:
    return l[0] == 0 and l[-1] == 0

# 2

def est_dans_batiment(l:list[int])-> bool:
    for i in range(len(l)):
        if l[i] < 0 or l[i] >= nb_etages:
            return False
    return True


# 3

def etages_tous_visites(l:list[int])-> bool:
    for i in range(nb_etages):
        if i not in l:
            return False
    return True 
    
# 4
   
def etages_suivant_valide(depart, arrive):
    for i in range(len(bouton_ascenseur)):
        if depart + bouton_ascenseur[i] == arrive:
            return True
    return False 
    
# 5

def tous_les_deplacements_valides(l):
    for i in range(len(l)-1):
        if etages_suivant_valide(l[i] , l[i+1]) == False:
            return False
    return True 

# 6

def solution_valide(l):
    if len(l) > nb_etages:
        return False 
    else:
        retur 
    
    
    
