
# TD5 - Listes chaînées

class Maillon:

    def __init__(self, val, suivant=None):
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



#------------------------------------------------------------



class maillonREC :

    def __init__(self):
        self.val = None
        self.suivant = None

    def suivant(self):
        return self.suivant

    def set_suivant(self, suivant):
        self.suivant = suivant

    def val(self):
        return self.val

    def __str__(self):
        return str(self.val)


    def construire(self, liste):
        if len(liste) != 0:
            m = Maillon(liste[0])
            self.suivant = m
            self.suivant.construire(liste[1:])


    def maximum(self):
        if self.suivant == None:
            return self.val
        maxi1 = self.suivant.maximum()
        return max(self.val, maxi1)
    

    def inserer_liste(self, liste, ind):
        if len(liste) != 0:
            if ind == 1:
                self.suivant = Maillon(liste[0], self.suivant)
                self.suivant.inserer_liste(liste[1:], ind+1)
            else:
                self.suivant.inserer_liste(liste, ind-1)



class listechaineeREC :

    def __init__(self):
        """
        >>> l = listechaineeREC()
        >>> l.est_vide()
        True
        >>> l.construire([1, 0, 7, 3])
        >>> l.est_vide()
        False
        >>> print(l)
        [1, 0, 7, 3]
        """
        self.tete = None

    def est_vide(self):
        return self.tete == None


    def __str__(self, str = "["):
        if self.est_vide():
            return str + "]"
        else:
            return self.__str__(str + str(self.tete.val) + " -> ")


    def construire(self, liste):
        assert self.est_vide(), "liste non vide"
        if len(liste) != 0:
            self.tete = maillonREC(liste[0])
            self.tete.construire(liste[1:])

    def maximum(self):
        assert not self.est_vide(), "liste vide"
        return self.tete.maximum()


    def inserer_liste(self, liste, ind):
        assert not self.est_vide(), "liste vide"
        if len(liste) != 0:
            m = maillonREC(liste[0])
            if ind == 0:
                m.set_suivant(self.tete)
                self.tete = m
            else:
                prec = self.tete
                for i in range(ind-1):
                    prec = prec.suivant
                m.set_suivant(prec.suivant)
                prec.set_suivant(m)
            self.inserer_liste(liste[1:], ind+1)






if __name__ == "__main__":
    import doctest
    doctest.testmod()