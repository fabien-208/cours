
class etudiant:
    
    def __init__(self, prenom, nom,formation, notes={}, diplome = False, saisie = True):
        """
        >>> etu = etudiant('fanny', 'bravo','info')
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
        ['MOMI', 'Algo', 'Anglais']
        >>> etu.stop_saisie_notes()
        >>> etu.ajoute_note('Anglais', 19)
        False
        >>> etu.str()
        'fanny bravo'
        >>> coef = {}
        >>> coef['Anglais'] = 7
        >>> coef['MOMI'] = 3
        >>> coef['Algo'] = 5
        >>> etu.moyenne_gen(coef)
        14.466666666666667
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
        liste = []
        for elt in self.__notes.keys():
            liste.append(elt)
        return liste

    
    def stop_saisie_notes(self):
        self.__saisie = False


    def str(self):
        return '{} {}'.format(self.__prenom, self.__nom)
    

    def moyenne_gen(self, coef):
        somme = 0
        co = 0
        for k, v in self.__notes.items():
            somme += self.moyenne_matière(k) * coef[k]
            co += coef[k]
        return somme / co






class Formation:

    def __init__(self, formation, coef) -> None:
        """
        >>> coef = {}
        >>> coef['Anglais'] = 7
        >>> coef['MOMI'] = 3
        >>> coef['Algo'] = 5
        >>> form  = Formation("semestre - 2 Lic. Informatique, coef")
        >>> form.ajoute_etudiant("Kevin", "Dupont")
        >>> form.ajoute_etudiant("Gabrielle", "Durant")
        >>> form.ajoute_etudiant("Yakoub", "Duchemin")
        >>> form.ajoute_etudiant("Léa", "Dupuis")
        >>> form.affiche_etudiant()

        """
        self.__formation = formation
        self.__coef = coef
        self.__etudiant = []


    def ajoute_etudiant(self, prenom, nom):
        self.__etudiant.append(etudiant(prenom, nom, self.__formation))


    def affiche_etudiant(self):
        for i in range(len(self.__etudiant)):
            print('{} - {} {}'.format(i+1, self.__etudiant[i].__prenom, self.__etudiant[i].__nom))




        
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
