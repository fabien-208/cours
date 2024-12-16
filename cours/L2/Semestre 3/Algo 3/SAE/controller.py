from collections import Counter
from math import log2


class Pile:
    def __init__(self):
        self.__elements = []

    def empiler(self, element):
        self.__elements.append(element)

    def depiler(self):
        if not self.est_vide():
            return self.__elements.pop()
        else:
            raise IndexError("depiler from empty stack")

    def est_vide(self):
        return len(self.__elements) == 0

    def sommet(self):
        if not self.est_vide():
            return self.__elements[-1]
        else:
            raise IndexError("sommet from empty stack")


class File:
    def __init__(self):
        self.__elements = []

    def ajouter(self, element):
        self.__elements.append(element)

    def supprimer(self):
        if not self.est_vide():
            return self.__elements.pop(0)
        else:
            raise IndexError("supprimer from empty queue")

    def est_vide(self):
        return len(self.__elements) == 0




class node:
    def __init__(self, val, fg=None, fd=None):
        self.__val = val
        self.__fg = fg
        self.__fd = fd
    
    def get(self):
        return self.__val
    
    def fd(self):
        return self.__fd
    
    def fg(self):
        return self.__fg
    
    def aFG(self):
        return self.__fg != None
    
    def aFD(self):
        return self.__fd != None
    
    def estFeuille(self):
        return self.__fg == None and self.__fd == None
    

    def cherche_dfs(self,val):
        if self.__val == val:
            return self
        if self.aFG():
            sommet=self.__fg.cherche_dfs(val)
            if sommet is not None:
                return sommet
        if self.aFD():
            sommet=self.__fd.cherche_dfs(val)
            if sommet is not None:
                return sommet
        return None
    

    def nb_sommets_dfs(self):
        nb1,nb2 = 0,0
        if self.aFG():
            nb1 = self.__fg.nb_sommets_dfs()
        if self.aFD():
            nb2 = self.__fd.nb_sommets_dfs()
            return 1+nb1+nb2
    



class tree_bin:

    def __init__(self):
        self.__root = None

    def cherche_dfs(self,val):
        assert self is not None
        pile = Pile()
        pile.empiler(self.__racine)
        while not pile.est_vide():
            sommet = pile.depiler()
            if sommet.__val == val:
                return sommet
            if sommet.aFD():
                pile.empiler(sommet.fd())
                if sommet.aFG():
                    pile.empiler(sommet.fg())
        return None
    

    def cherche_bfs(self, valeur):
        if self.__racine != None:
            f = File()
            f.ajouter(self.__racine)
            while not f.est_vide():
                sommet = f.supprimer()
                if sommet.get() == valeur:
                    return sommet
                if sommet.fg() != None:
                    f.empile(sommet.fg())
                if sommet.fd() != None:
                    f.ajouter(sommet.fd())
            return None
        


    def cherche(self, val):
        assert self is not None
        f = File()
        f.ajouter(self.__racine)
        while not f.est_vide():
            sommet = f.enlever()
            if sommet.valeur == val:
                return sommet
            if sommet.aFG():
                f.ajouter(sommet.fg())
            if sommet.aFD():
                f.ajoute(sommet.fd())
        return None
    

    def nb_sommets_bfs(self) :
        cpt = 0
        if self.__racine != None:
            f = File()
            f.ajoute(self.__racine)
            while not f.est_vide():
                sommet = f.supprimer()
                cpt += 1
                if sommet.aFG():
                    f.ajouter(sommet.fg())
                if sommet.aFD():
                    f.ajouter(sommet.fd())
            return cpt
        
    def nb_sommets_dfs(self):
        if self.__racine != None:
            return self.__racine.nb_sommets_dfs()
        return 0
