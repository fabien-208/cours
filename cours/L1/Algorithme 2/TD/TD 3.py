
class etudiant:
    
    def __init__(self, prenom: str, nom: str,formation: str, notes={}, diplome: bool = False, saisie: bool = True) -> None:
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
        ['Anglais', 'Algo', 'MOMI']
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
        12.8
        """
        
        self.__nom = nom
        self.__prenom = prenom
        self.__formation = formation
        self.__notes = notes
        self.__diplome = diplome
        self.__saisie = saisie
        
        
    def nom(self)-> str:
        return self.__nom
    
    def prenom(self)-> str:
        return self.__prenom
    
    def diplome(self) -> bool:
        return self.__diplome
    
    
    def ajoute_note(self, matière: str, note: int)-> bool:
        if self.__saisie == True:
            if matière not in self.__notes:
                self.__notes[matière] = []
            self.__notes[matière].append(note)
            return True
        else:
             return False
        
    def moyenne_matière(self, matière: str)-> float:
        
        somme = 0
        for note in self.__notes[matière]:
            somme += note
        return somme / len(self.__notes[matière])
        
        
        
    def les_matières(self)->list[str]:
        liste = []
        for elt in self.__notes.keys():
            liste.append(elt)
        return liste

    
    def stop_saisie_notes(self)-> None:
        self.__saisie = False


    def str(self)-> str:
        return '{} {}'.format(self.__prenom, self.__nom)
    

    def moyenne_gen(self, coef:dict)-> float:
        somme = 0
        co = 0
        for k in self.__notes.keys():
            somme += self.moyenne_matière(k) * coef[k]
            co += coef[k]
        return somme / co




class Formation:

    def __init__(self, formation:str, coef:dict) -> None:
        """
        >>> coef = {}
        >>> coef['Anglais'] = 7
        >>> coef['MOMI'] = 3
        >>> coef['Algo'] = 5
        >>> form  = Formation("semestre - 2 Lic. Informatique", coef)
        >>> form.ajoute_etudiant("Kevin", "Dupont")
        >>> form.ajoute_etudiant("Gabrielle", "Durant")
        >>> form.ajoute_etudiant("Yakoub", "Duchemin")
        >>> form.ajoute_etudiant("Léa", "Dupuis")
        >>> form.affiche_etudiant()
        1 - Kevin Dupont
        2 - Gabrielle Durant
        3 - Yakoub Duchemin
        4 - Léa Dupuis
        >>> form.ajoute_notes_etudiant(1, 'Anglais', 10)
        True
        >>> form.ajoute_notes_etudiant(1, 'Algo', 12)
        True
        >>> form.ajoute_notes_etudiant(1, 'Anglais', 16)
        True
        >>> form.ajoute_notes_etudiant(2, 'Algo', 11)
        True
        >>> form.ajoute_notes_etudiant(2, 'Algo', 17)
        True
        >>> form.ajoute_notes_etudiant(2, 'Anglais', 13)
        True
        >>> form.ajoute_notes_etudiant(3, 'Anglais', 18)
        True
        >>> form.ajoute_notes_etudiant(3, 'Algo', 18)
        True
        >>> form.ajoute_notes_etudiant(4, 'Algo', 15)
        True
        >>> form.ajoute_notes_etudiant(4, 'Anglais', 8)
        True
        >>> form.ajoute_notes_etudiant(4, 'Anglais', 10)
        True
        >>> form.calcule_diplome()
        13.375
        >>> form.ajoute_notes_etudiant(4, 'Anglais', 10)
        False
        >>> form.les_diplomes()
        ['Kevin Dupont', 'Gabrielle Durant', 'Yakoub Duchemin', 'Léa Dupuis']
        """
        self.__formation = formation
        self.__coef = coef
        self.__etudiant = []


    def ajoute_etudiant(self, prenom: str, nom:str)-> None:
        self.__etudiant.append(etudiant(prenom, nom, self.__formation))


    def affiche_etudiant(self):
        for i in range(len(self.__etudiant)):
            print('{} - {} {}'.format(i+1, self.__etudiant[i].prenom(), self.__etudiant[i].nom()))


    def ajoute_notes_etudiant(self, etu, matière, notes):
        self.__etudiant[etu -1].ajoute_note(matière, notes)



    def calcule_diplome(self):
        somme_moy = 0
        for i in range(len(self.__etudiant)):
            self.__etudiant[i].stop_saisie_notes()
            somme_moy += self.__etudiant[i].moyenne_gen(self.__coef)
        return somme_moy / len(self.__etudiant)
    

    def les_diplomes(self):
        liste = []
        for i in range(len(self.__etudiant)):
            if self.__etudiant[i].moyenne_gen(self.__coef) > 10:
                liste.append(self.__etudiant[i].str())
        return liste


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)