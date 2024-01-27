
class etudiant:
    
    def __init__(self, nom, prenom,formation, notes={}, diplome = False, saisie = True):
        """
        >>> etu  = etudiant('moi', 'frf','info')
        >>> etu.ajoute_note('MOMI', 9)
        True
        >>> etu.ajoute_note('MOMI', 12)
        True
        >>> etu.ajoute_note('MOMI', 6)
        True
        >>> etu.ajoute_note('Algo', 17)
        True
        >>> etu.ajoute_note('Anglais', 15)
        True
        >>> etu.moyenne_matière('MOMI')
        9.0
        >>> etu.les_matières()
        
        """
        
        self.__nom = nom
        self.__prenom = prenom
        self.__formation = formation
        self.__notes = notes
        self.__diplome = diplome
        self.__saisie = saisie
        
        
    def nom(self):
        return self.__nom
    
    def prenom(self):
        return self.__prenom
    
    def diplome(self):
        return self.__diplome
    
    
    def ajoute_note(self, matière, note):
        if self.__saisie == True:
            if matière not in self.__notes:
                self.__notes[matière] = []
            self.__notes[matière].append(note)
            print(True)
        else:
            print(False)
        
    def moyenne_matière(self, matière):
        
        somme = 0
        for note in self.__notes[matière]:
            somme += note
        return somme / len(self.__notes[matière])
        
        
        
    def les_matières(self):
        pass
    
        
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
