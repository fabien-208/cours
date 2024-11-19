
# TD5 - Listes chaînées

class Maillon:

    def __init__(self, val, suivant=None):
        """
        >>> m = Maillon(1)
        >>> m.get_valeur()
        1
        >>> m2 = Maillon(2, m)
        >>> m2.get_valeur()
        2
        >>> m2.suivant().get_valeur()
        1
        """
        self.__valeur = val
        self.__suivant = suivant

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
    
    




class Listechaine:

    def __init__(self):
        """
        >>> l = Listechaine()
        >>> print(l)
        []
        >>> l.est_vide()
        True
        >>> l.append(1)
        >>> print(l)
        [1]
        >>> l.est_vide()
        False
        >>> l.append(2)
        >>> l.append(3)
        >>> print(l)
        [1, 2, 3]
        >>> len(l)
        3
        >>> l.get(0)
        1
        >>> l.get(1)
        2
        >>> l.delete(1)
        >>> print(l)
        [1, 3]
        >>> l.insert(1, 5)
        >>> print(l)
        [1, 5, 3]
        >>> l.appartient(5)
        True
        >>> l.appartient(2)
        False
        >>> l.append(3)
        >>> l.nb_occurences(3)
        2
        >>> l.append(1)
        >>> print(l)
        [1, 5, 3, 3, 1]
        >>> l.ind_min()
        [0, 4]
        >>> l.append(0)
        >>> print(l)
        [1, 5, 3, 3, 1, 0]
        >>> l.permute_tete_queu()
        >>> print(l)
        [0, 5, 3, 3, 1, 1]
        >>> l.premiere_repetition()
        3
        >>> l.supprime_paire()
        >>> print(l)
        [5, 3, 1]
        >>> l.append(3)
        >>> l.append(4)
        >>> l.append(1)
        >>> print(l)
        [5, 3, 1, 3, 4, 1]
        >>> l.suprimer_doublons()
        >>> print(l)
        [5, 3, 4, 1]
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


    def appartient(self, val):
        m = self.__tete
        while m != None:
            if m.get_valeur() == val:
                return True
            m = m.suivant()
        return False
    

    def nb_occurences(self, val):
        m = self.__tete
        n = 0
        while m != None:
            if m.get_valeur() == val:
                n += 1
            m = m.suivant()
        return n
    


    def val_maximal(self):
        assert self.__tete != None
        m = self.__tete
        max = m.get_valeur()
        while m != None:
            if m.get_valeur() > max:
                max = m.get_valeur()
            m = m.suivant()
        return max


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
    

    def supprime_maillon(self, val):
        if self.__tete is None:
            return
        
        if self.__tete.get_valeur() == val:
            self.__tete = self.__tete.suivant()
            return
        
        prev = self.__tete
        curr = self.__tete.suivant()
        
        while curr is not None:
            if curr.get_valeur() == val:
                prev.set_suivant(curr.suivant())
                return
            prev = curr
            curr = curr.suivant()

    def ajoute_maillon(self, valeur):
        if self.__tete is None:
            self.__tete = Maillon(valeur)
        courant = self.__tete
        while courant.suivant() is not None:
            courant = courant.suivant()
        courant.set_suivant(valeur)
        
    
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
        i = 0
        courant = liste[i]
        while courant is not None:
            courant.ajoute_maillon(courant.valeur)
            courant = courant[i+1]


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
                    

    def suprimer_doublons(self):
        prec =self.__tete
        lis = []
        while prec != None:
            if prec.get_valeur() in lis: 
                self.supprime_maillon(prec.get_valeur())
            else:
                lis.append(prec.get_valeur())
            prec = prec.suivant()

    def supprimer(self, n, m):
        assert n > 0 and m > 0 and n+m <= self.__len__()
        prec = self.__tete
        for i in range(m-1):
            prec = prec.suivant()
        prec2 = prec
        for i in range(n+1):
            prec2 = prec2.suivant()
        prec.set_suivant(prec2)



    def permute(self, k):
        n = self.__len__()
        assert 0 <= k < n
        val =self.get(k)
        self.set(k, self.get(n-k-1))
        self.set(n-k-1, val)

    def set(self, i, val):
        assert 0 <= i <self.__len__()
        prec = self.__tete
        for i in range(i-1):
            prec = prec.suivant()
        prec.set_suivant(Maillon(val, prec.suivant()))

    def inverser(self):
        if self.__tete is None or self.__tete.suivant() is None:
            return
        prec = None
        courant, suivant = self.__tete, self.__tete.suivant()  
        while courant is not None:
            suivant = courant.suivant()
            courant.set_suivant(prec)
            prec = courant
            courant = suivant




if __name__ == '__main__':
    import doctest
    doctest.testmod()