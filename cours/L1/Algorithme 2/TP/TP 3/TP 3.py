import random

class Case():
    
    def __init__(self, valeur = 0, cache = True):
        """
        >>> c1 = Case()	
        >>> c1.est_cache()
        'cache'
        >>> c1.est_visible()
        'non visible'
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
        ['-', ' ']
        """
        self.__valeur = valeur
        self.__cache = cache
        
        
        
    def est_cache(self):
        if self.__cache:
            return 'cache'
        else:
            return 'non cache'
        
        
    def est_visible(self):
        if self.__cache:
            return 'non visible'
        else:
            return 'visible'
        
        
    def est_bombe(self):
        if self.__valeur == -1:
            return 'la case est une bombe'    
    
    
    def est_vide(self):
        if self.__valeur == 0:
            return 'la case est vide'
    

    def incremente_valeur(self):
        if self.__valeur == 0:
            self.__valeur += 1

    def montre_toi(self):
        self.__cache = False

    def str(self):
        tu = []
        if self.__valeur == -1:
            tu.append('*')
        if self.__cache == True:
            tu.append('-')
        if self.__valeur == 0:
            tu.append(' ')
        return tu

        




class demineur:

    def __init__(self, nb_llgne = 20, nb_colonne = 10) -> None:
        """
        >>> dem = demineur()
        >>> dem.affiche_plateau()
        """
        self.__nb_ligne = nb_llgne
        self.__nb_colonne = nb_colonne
        self.plateau = []
        
        for i in range(self.__nb_colonne):
            cs = []
            for j in range(self.__nb_ligne):
                fek = Case()
                cs.append(fek.str())
            self.plateau.append(cs)


        
    def affiche_plateau(self):
        self.pose_bombes()
        for i in range(len(self.plateau)):
            print(self.affiche_ligne_traits(i))
            print(self.affiche_traits(i))
        print(self.affiche_ligne_traits())

    
    def affiche_ligne_traits(self, ind = 0):
        ls = '+'
        elt = self.plateau[ind]        
        for i in range(len(elt)):
            ls += '--+'
        return ls
        

    def affiche_traits(self, ind = 0):
        frbh = '|'
        elt = self.plateau[ind]
        for truc in elt:
            if truc[0]== '-':
                if truc[1] == ' ':
                    frbh += '  |'
                else:
                    frbh += ' {}|'.format(truc[1])
            else :
                frbh += ' *|'
        return frbh
    


    def pose_bombes(self, nb_bombes = 15):
        for i in range(nb_bombes):
            col = random.randint(0, self.__nb_colonne-1)
            lig = random.randint(0, self.__nb_ligne-1)
            self.plateau[col][lig][0] = ' *'
            self.plateau[col-1][lig-1].incremente_valeur()
            self.plateau[col-1][lig].incremente_valeur()
            self.plateau[col-1][lig+1].incremente_valeur()
            self.plateau[col][lig-1].incremente_valeur()
            self.plateau[col][lig+1].incremente_valeur()
            self.plateau[col+1][lig-1].incremente_valeur()
            self.plateau[col+1][lig+1].incremente_valeur()
            self.plateau[col+1][lig].incremente_valeur()





if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    