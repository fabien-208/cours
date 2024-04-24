import random

from copy import deepcopy


class Case():
    def __init__(self,coords:tuple, couleur:int, modele, atteinte:bool=False)->None:
        self.__coords = coords
        self.__couleur = couleur
        self.__atteinte = atteinte
        self.__dim_matrice = [modele.nb_col(),modele.nb_lig()]
        
    
    def coord(self)->tuple:
        return self.__coords
    def couleur(self)->int:
        return self.__couleur
    def touché(self)->bool:
        return self.__atteinte
    def dimension(self):
        return self.__dim_matrice
    
    def voisines(self)->list:
        if self.__coords == (0,0):
            return [(0,1),(1,0)]
        elif self.__coords == (0,self.__dim_matrice[1]-1):
            return [(1,self.__dim_matrice[1]-1),(0,self.__dim_matrice[1]-1)]
        elif self.__coords == (self.__dim_matrice[0]-1,0):
            return [(self.__dim_matrice[0]-1,0),(self.__dim_matrice[0]-1,1)]
        elif self.__coords == (self.__dim_matrice[0]-1, self.__dim_matrice[1]-1):
            return [(self.__dim_matrice[0]-1,self.__dim_matrice[1]-1),(self.__dim_matrice[0]-1,self.__dim_matrice[1]-1)]
        
        elif self.__coords[0] == 0:
            return [(0,self.__coords[1]+1),(0,self.__coords[1]-1),(1,self.__coords[1])]
        elif self.__coords[0] == self.__dim_matrice[0]-1:
            return [(self.__dim_matrice[0]-1,self.__coords[1]-1),(self.__dim_matrice[0]-1,self.__coords[1]+1),(self.__dim_matrice[0]-2,self.__coords[1])]
        elif self.__coords[1] == 0:
            return [(self.__coords[0],1),(self.__coords[0]-1,0),(self.__coords[0]+1,0)]
        elif self.__coords[1] == self.__dim_matrice[1]-1:
            return [(self.__coords[0]-1,self.__coords[1]),(self.__coords[0]+1,self.__coords[1]),(self.__coords[0],self.__coords[1]-1)]

        else:
            return [(self.__coords[0]-1,self.__coords[1]),(self.__coords[0]+1,self.__coords[1]),(self.__coords[0],self.__coords[1]+1),(self.__coords[0],self.__coords[1]-1)]

    def change_Couleur(self,couleur:int)->None:
        self.__couleur = couleur
    
    def change_touché(self)->None:
        self.__atteinte = True


class Modele():

    def __init__(self, nb_lignes:int=12, nb_colonnes:int=12, nb_couleurs:int=6)->None:

        self.__score = 0
        self.__lig = nb_lignes
        self.__col = nb_colonnes
        self.__couleurs = nb_couleurs
        self.__matrice = []
        for i in range(self.__lig):
            self.__matrice.append([])
            for j in range(self.__col):
                self.__matrice[i].append(Case((i,j),random.randint(0,self.__couleurs-1),self))
        self.__finie = False
        self.__max_coups = self.monte_carlo()
        self.__pile = Pile([])
        #self.__pile.append(self.__matrice)
        self.__nb_reinit = 3


    def nb_lig(self)->int:
        return self.__lig
    
    def nb_col(self)->int:
        return self.__col
    
    def nb_couleurs(self)->int:
        return self.__couleurs
    
    def score(self)->int:
        return self.__score
    
    def max_coups(self) -> int:
        return self.__max_coups
    
    def couleur(self,l:int,c:int)->int:
        return self.__matrice[l][c].couleur()
    
    def choisit_couleur(self,l:int,c:int)->None:
        self.__matrice[0][0].changeCouleur(self.__matrice[l][c].couleur())
    
    def reinit(self)->None:
        self.__score = 0
        self.__finie = False
        self.__matrice = []
        for i in range(self.__lig):
            self.__matrice.append([])
            for j in range(self.__col):
                self.__matrice[i].append(Case((i,j),random.randint(0,self.__couleurs-1),self))
        self.__max_coups = self.monte_carlo()
    

    def __str__(self) -> str:
        plateau = ' |'
        for i in range(self.nb_col):
            plateau += (' {} |'.format(i))
        plateau += '\n'
        for l in range(self.nb_lig):
            for j in range(self.__nb_lig):
                plateau += '----'
            plateau += '\n'
            plateau += ('{}'.format(l))
            for k in range(self.nb_col):
                plateau+= ('| {} '.format(self.__jeu[l][k]))
            plateau += '\n'
        return plateau


    def voisines(self,l:int,c:int)->list:
        return self.__matrice[l][c].voisines()

    def calcul_atteinte(self):
        a_verif=[]
        verif=[(0,0)]
        for i in self.voisines(0,0):
            if self.__matrice[i[0]][i[1]].couleur() == self.__matrice[0][0].couleur():
                self.__matrice[i[0]][i[1]].change_touché()
                for j in self.voisines(i[0],i[1]):
                    if not(j in a_verif) and not(j in verif):
                        a_verif.append(j)
            verif.append(self.__matrice[i[0]][i[1]].coord())
        while len(a_verif) != 0:
            compt = 0
            for i in range(len(a_verif)):
                if self.__matrice[a_verif[0][0]][a_verif[0][1]].couleur() == self.__matrice[0][0].couleur():
                    self.__matrice[a_verif[0][0]][a_verif[0][1]].change_touché()
                    verif.append(self.__matrice[a_verif[0][0]][a_verif[0][1]].coord())
                    for j in self.voisines(a_verif[0][0],a_verif[0][1]):
                        if not(j in a_verif) and not(j in verif):
                            a_verif.append(j)
                else:
                    verif.append(self.__matrice[a_verif[0][0]][a_verif[0][1]].coord())
                a_verif.pop(0)
                compt+=1
    
    def partie_finie(self):
        self.__finie = True
        for i in range(len(self.__matrice)):
            for j in range(len(self.__matrice[i])):
                if self.couleur(i, j) != self.couleur(0, 0):
                    self.__finie = False
                    return False
        return True
   
    def finie(self):
        return self.__finie

    def pose_couleur(self,coul:int):
        modele = self
        self.calcul_atteinte()
        self.__score+=1
        self.__matrice[0][0].change_Couleur(coul)
        for i in self.__matrice:
            for j in i:
                if j.touché():
                    j.change_Couleur(coul)
        self.partie_finie()
        #self.push()
        

    def monte_carlo(self)->int:
        compt = 0
        min = 100

        for i in range(7):
            jeu = deepcopy(self)
            while jeu.finie() == False:
                couleur = random.randint(0, self.nb_couleurs())
                jeu.calcul_atteinte()
                jeu.pose_couleur(couleur)
                compt += 1
            if compt <= min:
                min = compt
            compt = 0

        return min
    
    def win(self) -> bool:
        return self.__score < self.__max_coups
    
    def pop(self):
        tr = self.__pile.pop()
        if tr == None:
            pass
        else:
            self.__matrice = tr
            self.__score -= 1 

    #def push(self):
    #    self.__pile.push(self.__matrice)

    def reinit_partielle(self):
        if self.__nb_reinit < 1:
            pass
        else:        
            self.calcul_atteinte()
            for i in self.__matrice:
                for j in i:
                    if j.coord() == (0,0):
                        pass
                    else:
                        if j.touché() == False:
                            j.change_Couleur(random.randint(0, self.__couleurs))




    def enleve_reinit(self):
        if self.__nb_reinit == 0:
            pass
        else:
            self.__nb_reinit -=1

    def nb_reinit(self):
        return self.__nb_reinit
class Pile:

    def __init__(self, pile) -> None:
        self.__pile = pile
        self.__modele = Modele

    def push(self, truc:any):
        self.__pile.append(truc)

    def pop(self):
        print('fgbthiejklqs!gdjnizevjtfl:bnozrilskjdrtgtjgnjgrgbnjgbngjn')
        
        if len(self.__pile) == 0:
            return None
        else:
            return self.__pile.pop()
        
    def __len__(self):
        return len(self.__pile)