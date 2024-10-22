
class Maillon:

    def __init__(self, valeur, suivant = None):
        self.valeur = valeur
        self.suivant = suivant

    def get_valeur(self):
        return self.__valeur
    
    def suivant(self):
        return self.__suivant
    

    def set_suivant(self, suivant):
        self.__suivant = suivant


    def __str__(self):
        mess = str(self.__valeur)
        if self.__suivant is not None:
            mess += ', '
        return mess

    # exercice 1


    def suprime_maillon(self, valeur):
        if self.tete != None:
            if self.tete == valeur:
                self.tete = self.tete.suivant()
            else:
                prec = self.tete
                while prec.suivant() != None and prec.suivant().valeur != valeur:
                    prec = prec.suivant()
                if prec != None:
                    prec.set_suivant(valeur.suivant()) 

    def ajoute_maillon(self, valeur):
        if self.tete is None:
            self.tete = Maillon(valeur)
        courant = self.tete
        while courant.suivant() is not None:
            courant = courant.suivant()
        courant.set_suivant(valeur)

    











class Listechaine:

    def __init__(self):
        """
        >>> lc = Listechaine()
        >>> lc.append(-1)
        >>> lc.append(5)
        >>> lc.append(-3)
        >>> lc.append(8)
        >>> lc.append(14)
        >>> m = maillon(5)
        >>> lc.ajoute_maillon(m)
        >>> print(lc)
        [-1, 5, -3, 8, 14, 5]
        >>> lc.suprime_maillon(5)
        >>> print(lc)
        [-1, -3, 8, 14]
        """
        self.__tete = None


    def est_vide(self):
        return self.__tete is None
    

    def append(self, val):
        if self.__tete is None:
            self.__tete = Maillon(val)
        else:
            m = self.__tete
            while m.suivant() != None:
                m = m.suivant()
            m.set_suivant(Maillon(val))


    def __str__(self):
        mess = '['
        m = self.__tete
        while m != None:
            mess += str(m)
            m = m.suivant()
        mess += ']'
        return mess
    

    def __len__(self):
        m = self.__tete
        n = 0
        while m != None:
            n += 1
            m = m.suivant()
        return n
    

    def get(self, i):
        assert self.__tete != None
        cpt = 0
        m = self.__tete
        while cpt < i:
            m = m.suivant()
            cpt += 1
        return m.get_valeur()
    

    def delete(self, i):
        assert i < self.__len__()
        if i == 0:
            self.__tete = self.__tete.suivant()
        else:
            m = self.__tete
            for j in range(i-1):
                m = m.suivant()
            m.set_suivant(m.suivant().suivant())



    def insert(self, i, val):
        if i == 0:
            self.__tete = Maillon(val, self.__tete)
        else:
            m = self.__tete
            for j in range(i-1):
                m = m.suivant()
            m.set_suivant(Maillon(val, m.suivant()))

    # Exercice 3

    def appartient(self, val):
        m = self.__tete
        while m != None:
            if m.get_valeur() == val:
                return True
            m = m.suivant()
        return False
    
    # Exercice 4

    def nb_occurences(self, val):
        m = self.__tete
        n = 0
        while m != None:
            if m.get_valeur() == val:
                n += 1
            m = m.suivant()
        return n
    
    # Exercice 5

    def val_maximal(self):
        assert self.__tete != None
        m = self.__tete
        max = m.get_valeur()
        while m != None:
            if m.get_valeur() > max:
                max = m.get_valeur()
            m = m.suivant()
        return max

    # Exercice 6

    def ind_min(self):
        assert self.__tete != None
        m = self.__tete
        min = m.get_valeur()
        ind = []
        cpt = 0
        while m != None:
            if m.get_valeur() <= min:
                if m.get_valeur() < min:
                    ind = [cpt]
                    min = m.get_valeur()
                else:
                    ind.append(cpt)
            m = m.suivant()
            cpt += 1
        return ind
    
    # Exercice 7

    def permute_tete_queu(self):
        
        if self.__tete is None or self.__tete.suivant() is None:
            return
        
        m = self.__tete
        prev = None
        while m.suivant() is not None:
            prev = m
            m = m.suivant()
        
        m.set_suivant(self.__tete.suivant())
        prev.set_suivant(self.__tete)
        self.__tete.set_suivant(None)
        self.__tete = m
        
    # Exercice 8

    def premiere_repetition(self):
        m = self.__tete
        liste = []
        while m != None:
            if m.get_valeur() in liste:
                return m.get_valeur()
            else:
                liste.append(m.get_valeur())
                m = m.suivant()
        return None
    
    # Exercice 9
        
    
    def supprime_paire(self):
        if self.__tete is None:
            return
        
        index = 0
        m = self.__tete
        prev = None
        
        while m is not None:
            if index % 2 == 0:
                if prev is None:
                    self.__tete = m.suivant()
                    m = self.__tete
                else:
                    prev.set_suivant(m.suivant())
                    m = m.suivant()
            else:
                prev = m
                m = m.suivant()
            index += 1



    
    def ajoute_liste(self, liste):
        courant = liste.tete
        while courant is not None:
            self.ajoute_maillon(courant.valeur)
            courant = courant.suivant()

    # exercice 3


    def plus_grand(self, min, max):
        assert not self.est_vide() and min < max
        trouve = False
        prec = self.tete
        maxi = None
        while prec != None:
            if min <= prec.valeur <= max:
                if not trouve:
                    maxi = prec.get_valeur()
                    trouve = True
                else:
                    maxi = prec.get_valeur()
        return maxi



    def supprimer_négatifs(self):
        if self.tete != None:
            prec = self.__tete
            pos = 0
            while prec != None:
                if prec.valeur < 0:
                    self.delete(pos)
                else:
                    pos += 1
                    



if __name__ == '__main__':
    import doctest
    doctest.testmod()