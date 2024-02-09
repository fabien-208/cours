import random


class Case():
    
    def __init__(self, valeur = 0, cache = True):
        """
        >>> c1 = Case()	
        >>> c1.est_cache()
        'cache'
        >>> c1.est_visible()
        False
        >>> c1.est_vide()
        'la case est vide'
        >>> c2 = Case(-1)
        >>> c2.est_bombe()
        'la case est une bombe'
        >>> c2.montre_toi()
        >>> c2.est_cache()
        'non cache'
        >>> c2.str()
        ['*']
        >>> c1.str()
        [' ', '-']
        """
        self.__valeur = valeur
        self.__cache = cache
        

    def valeur(self):
        return self.__valeur
        
        
    def est_cache(self):
        if self.__cache:
            return 'cache'
        else:
            return 'non cache'
        
        
    def est_visible(self):
        return self.__cache 

        
        
    def est_bombe(self):
        if self.__valeur == -1:
            return 'la case est une bombe'    
    
    
    def est_vide(self):
        if self.__valeur == 0:
            return 'la case est vide'
    

    def incremente_valeur(self):
        if self.__valeur != -1:
            self.__valeur += 1

    def montre_toi(self):
        self.__cache = False

    def str(self):
        tu = []
        if self.__valeur == -1:
            tu.append('*')
        if self.__valeur == 0:
            tu.append(' ')
        if self.__cache == True:
            tu.append('-')
        return tu

        




class demineur:

    def __init__(self, nb_llgne = 20, nb_colonne = 10) -> None:
        """
        >>> dem = demineur()
        >>> dem.affiche_plateau()
        >>> dem.partie_finie(1, 2)
        False
        >>> dem.montre(3, 5)
        >>> dem.montre(4, 4)
        >>> dem.montre(3, 9)
        >>> dem.montre(1, 6)
        >>> dem.montre(5, 9)
        >>> dem.montre(9, 14)

        """
        self.__nb_ligne = nb_llgne
        self.__nb_colonne = nb_colonne
        self.plateau = []
        
        for i in range(self.__nb_colonne):
            cs = []
            for j in range(self.__nb_ligne):
                fek = Case()
                cs.append(fek)
            self.plateau.append(cs)


        
    def affiche_plateau(self):
        self.pose_bombes()
        jn = ' '
        for i in range(self.__nb_ligne):
            jn += '   {}'.format(i)
        print(jn)
        for i in range(len(self.plateau)):
            print(self.affiche_ligne_traits(i))
            print(self.affiche_traits(i))
        print(self.affiche_ligne_traits())

    
    def affiche_ligne_traits(self, ind = 0):
        ls = '  +'
        elt = self.plateau[ind]        
        for i in range(len(elt)):
            ls += '---+'
        return ls
        

    def affiche_traits(self, ind = 0):
        frbh = '{} |'.format(ind)
        elt = self.plateau[ind]

        for i in range(len(elt)):
            truc  = elt[i]
            if truc.est_cache() == 'non cache':
                if truc.est_bombe() == 'la case est une bombe':
                    frbh += ' * |'
                else:
                    frbh += ' {} |'.format(truc.valeur())
            else :
                frbh += ' - |'
        return frbh
    


    def pose_bombes(self, nb_bombes = 15):
        for i in range(nb_bombes):
            col = random.randint(1, self.__nb_colonne-2)
            lig = random.randint(1, self.__nb_ligne-2)
            self.plateau[col][lig].__valeur = -1
            for j in range(-1, 2):
                for k in range(-1, 2):
                    self.plateau[col+j][lig+k].incremente_valeur()




    def partie_finie(self, l, c):
        if self.plateau[l][c].est_bombe != 'la case est une bombe':
            return False
        else:
            for i in range(len(self.plateau)):
                for j in range(len(self.plateau[i])):
                    if self.plateau[i][j].est_cache != 'non cache':
                        return False
        return True
                        







    def montre(self,l,c) :
        """Demineur, int, int, -> None
        decouvre la case (l,c) et affiche le plateau.
        l et c doivent etre positfs et inferieurs `a, respectivement, __nb_lig et __nb_col.
        """
        self.montre_case(l,c)
        self.affiche_plateau()

    def montre_case(self,l,c) :
        """Demineur, int, int, -> None
        decouvre la case (l,c) et ses voisines le cas echeant.
        l et c doivent etre positfs et inferieurs a, respectivement,__nb_lig et __nb_col.
        """
        if not self.plateau[l][c].est_visible() == False:
            self.plateau[l][c].montre_toi()
            if self.plateau[l][c].est_bombe() == 'la case est une bombe':
                print("Boum!!")
            elif self.plateau[l][c].est_vide() == 'la case est vide' :
                if c > 0 :
                    self.montre_case(l,c-1)
                    if l > 0 :
                        self.montre_case(l-1,c-1)
                    if l < self.__nb_ligne-1 :
                        self.montre_case(l+1,c-1)
                if c < self.__nb_colonne-1 :
                    self.montre_case(l,c+1)
                    if l > 0 :
                        self.montre_case(l-1,c+1)
                    if l < self.__nb_ligne-1 :
                        self.montre_case(l+1,c+1)
                if l > 0 :
                    self.montre_case(l-1,c)
                if l < self.__nb_ligne-1 :
                    self.montre_case(l+1,c)






if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    