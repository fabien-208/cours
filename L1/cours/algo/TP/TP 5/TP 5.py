import random

HUMAIN = 'X'
ORDI = 'O'
VIDE = ' '
T_PLATEAU = 3


# exercice 1

def init_plateau():
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ' ]]


# exercice 2

def print_plateau(plateau = init_plateau()):
    l  = plateau
    print(l[0][0]+'|'+l[0][1]+'|'+l[0][2]+ '\n'+
          '-----'+'\n'+
          l[1][0]+'|'+l[1][1]+'|'+l[1][2]+ '\n'+
          '-----'+'\n'+
          l[2][0]+'|'+l[2][1]+'|'+l[2][2])
    
    
# exercice 3

def input_humain(ll):
    entier = ['0', '1', '2', '3', '4', '5', '6', '7','8' ,'9']
    choix = ''
    while choix == '':
        choix = input('A quelle coordonnés voulait vous placez votre symbole x y:')
        if choix == 'q':
            return None
        if choix[0] not in entier or choix[2] not in entier:
            choix =''
        elif int(choix[0]) < 0 or int(choix[2]) < 0:
            choix = ''
        elif int(choix[0]) > T_PLATEAU or int(choix[2]) > T_PLATEAU:
            choix = ''
        elif ll[int(choix[0])][int(choix[2])] != ' ':
            choix = ''
    return (choix[0], choix[2])
            
            
# exercice 4


def coords_vides(ll):
    coord_vide = []
    for i in range(len(ll)):
        for j in range(len(ll[i])):
            if ll[i][j] == ' ':
                coord_vide.append((i, j))
    return coord_vide
   

# exercice 5

def input_ordi(ll):
    return random.choice(coords_vides(ll))
   
   
   
# exercice 6

def est_victoire(symb, ll):
    if ll[2][0] == ll[1][1] == ll[0][2] == symb:
        return True
    if ll[0][0] == ll[1][1] == ll[2][2] == symb:
        return True
    if ll[0][0] == ll[0][1] == ll[0][2] == symb:
        return True
    if ll[1][0] == ll[1][1] == ll[1][2] == symb:
        return True
    if ll[2][0] == ll[2][1] == ll[2][2] == symb:
        return True
    if ll[0][0] == ll[1][0] == ll[2][0] == symb:
        return True
    if ll[1][0] == ll[1][1] == ll[1][2] == symb:
        return True
    if ll[2][0] == ll[2][1] == ll[2][2] == symb:
        return True
    if ll[0][2] == ll[1][2] == ll[2][2] == symb:
        return True
    if ll[0][1] == ll[1][1] == ll[2][1] == symb:
        return True
    return False
   
# exercice 7
   
def joue_partie():
    plateau = init_plateau()
    print_plateau(plateau)
    while est_victoire(HUMAIN, plateau) ==False and est_victoire(ORDI, plateau) ==False:
        if coords_vides(plateau) == []:
            print('égalité')
            break 
        choix = input_humain(plateau)
        plateau[int(choix[0])][int(choix[1])] = HUMAIN
        print_plateau(plateau)
        if est_victoire(HUMAIN, plateau) == True:
            print('félicitations vous avez gagné !!!')
            break
        choix_ordi = input_ordi(plateau)
        plateau[int(choix_ordi[0])][int(choix_ordi[1])] = ORDI
        print("coup de l'odinateur:{} {}".format(choix_ordi[0], choix_ordi[1]))
        print_plateau(plateau)
        if est_victoire(ORDI, plateau) == True:
            print('vous avez perdu ;)')
            break 
        
# exercice 8

def input_rejouer(choix = ''):
    while choix == '':
        choix = input('voulez vous rejouez ? oui/non: ')
        if choix == 'oui':
            return True
        elif choix == 'non':
            return False
        choix = ''
      
      
# exercice 9

def main():
    while True == True:
        joue_partie()
        choix = input_rejouer()
        if choix == False :
            break
        
            
        
      
