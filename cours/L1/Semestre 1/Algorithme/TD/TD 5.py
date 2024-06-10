
# exercice 1
#  Question 1

def alphabet(mot):
    alphabet = {}
    for i in range(len(mot)):
        if mot[i] not in alphabet.keys():
            alphabet[mot[i]] = 1
        else:
            alphabet[mot[i]] += 1
    return alphabet

#  Question 2

def anagrame(mot1, mot2):
    return alphabet(mot1) == alphabet(mot2)

# exercice 2
#  Question 1

unechemine = {'Boris' : 'trotinette', 'Alice' : 'rollers', 'elliot' : 'rape a fromage'}
lahotte = {'rollers' : 2, 'trotinette' : 1, 'rape a fromage' : 2}

def donnecadeaux(unechemine, lahotte):
    for values in unechemine.values():
        if values not in lahotte:
            return False 
        lahotte[values] -= 1 
        if lahotte[values] == 0:
            del lahotte[values]
    return True

#  Question 2

leschemines = {' 5 rue Decrombecque, Lens' : {'luce': 'rollers', 'suzanne' : 'anthologie de poesie de francais', 'Marie' : 'rollers'}, '12 rue Jean Souvraz, Lens': unechemine}

def quelsenfantsontpourcadeau(chemine, cadeau):
    liste = []
    for elt in chemine.values():
        for keys, values in elt.items():
            if values == cadeau:
                liste.append(keys)
    return liste

#  Question 3


def constitutionhotte(chemine):
    hotte = {}
    for elt in chemine.values():
        for keys, values in elt.items():
            if values not in hotte:
                hotte[values] = 1
            if values in hotte:
                hotte[values] += 1
    return hotte
            
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              