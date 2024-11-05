
# TP5 - Listes chaînées

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
        """
        >>> l = Listechaine()
        >>> l.est_vide()
        True
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
        >>> l.contient(3)
        True
        >>> l.append(-3)
        >>> l.append(5)
        >>> l.append(-3)
        >>> print(l)
        [5, 3, 1, -3, 5, -3]
        >>> l.indice_minimum()
        [3, 5]
        >>> l2 = Listechaine()
        >>> l2.append(1)
        >>> l2.append(2)
        >>> l2.append(10)
        >>> l2.append(5)
        >>> l2.append(-2)
        >>> l2.append(5)
        >>> l2.append(12)
        >>> l2.append(10)
        >>> print(l2)
        [1, 2, 10, 5, -2, 5, 12, 10]
        >>> l2.permutes_paires()
        >>> print(l2)
        [2, 1, 5, 10, 5, -2, 10, 12]
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


    # exercie 3

    def contient(self, ind, prec = None):
        if prec == None:
            prec = self.__tete
        if ind == prec.get_valeur():
            return True
        if prec.suivant() == None:
            return False
        else:
            return self.contient(ind, prec.suivant())

    # exercice 4

    def indice_minimum(self, m=None, min=None, indices=[], cpt=0):
        if m is None:
            m = self.__tete
            min = m.get_valeur()

        if m is None:
            return indices

        if m.get_valeur() < min:
            min = m.get_valeur()
            indices = [cpt]
        elif m.get_valeur() == min:
            indices.append(cpt)

        if m.suivant() == None:
            return indices
        else:
            return self.indice_minimum(m.suivant(), min, indices, cpt + 1)


    # exercice 5

    def permutes_paires(self, m=None):
        if m == None and self.__tete == None:
            m = self.__tete

        if m.suivant() == None and m == None:
            return

        tru = m.get_valeur()
        m.__valeur = m.suivant().get_valeur()
        m.suivant().__valeur = tru
        self.permutes_paires(m.suivant().suivant())





if __name__ == '__main__':
    import doctest
    doctest.testmod()