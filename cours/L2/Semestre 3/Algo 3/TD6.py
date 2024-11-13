
class Sommet:
    def __init__(self, val, fg=None, fd=None):
        self.__val = val
        self.__fg = fg
        self.__fd = fd
    def get(self):
        return self.__val
    def fd(self):
        return self.__fd
    def fg(slef):
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



class ArbreBinaire:
    
    def __init__(self):
        self.__racine = None


    def cherche_dfs(self,val):
        if not self.est_vide():
            return self.__racine.chercher_dfs(val)
        


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
    

    def lesfeuilles(self):
        feuilles = []
        if self.__racine is not None:
            f = File()
            f.ajouter(self.__racine)
            while not f.est_vide():
                sommet = f.supprimer()
                if sommet.estFeuille():
                    feuilles.append(sommet)
                if sommet.aFG():
                    f.ajouter(sommet.fg())
                if sommet.aFD():
                    f.ajouter(sommet.fd())
        return feuilles
    

    def plus_grande_valeur(self):
        if self.__racine is not None:
            max = self.__racine.get()
            f = File()
            f.ajouter(self.__racine)
            while not f.est_vide():
                sommet = f.supprimer()
                if sommet.get() > max:
                    max = sommet.get()
                if sommet.aFG():
                    f.ajouter(sommet.fg())
                if sommet.aFD():
                    f.ajouter(sommet.fd())
            return max
        return None
    
    def hauteur(self):
        if self.estfeuile():
            return 0
        h1, h2 = 0, 0
        if self.__fg != None:
            h1 = self.__fg.hauteur_dfs()
        if self.__fd != None:
            h2 = self.__fd.hauteur_dfs()
        return 1 + max(h1, h2)
    


    def valeur_superieur_k(self, k):
        if self.__racine is None:
            return []
        Res = []
        f = File()
        f.ajouter(self.__racine)
        while not f.est_vide():
            sommet = f.supprimer()
            val = sommet.get()
            if k<= val and val not in Res:
                Res.append(val)
            if sommet.aFG():
                f.ajouter(sommet.fg())
            if sommet.aFD():
                f.ajouter(sommet.fd())
        return Res