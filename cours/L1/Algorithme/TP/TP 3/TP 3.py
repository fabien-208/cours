from string import ascii_letters, digits
ACCENTS = 'àâäèéêëîïòôöùûüç'
SYMBOLES = ',.!?:; \n\t&"\'@%+-/\\*_()[]{}'
ALPHABET = ascii_letters + ACCENTS + digits + SYMBOLES

#exercice 2

def input_mode(choix= ''):
    while choix != 'c' and choix != 'd' and choix != 'D' and choix!= 'C':
        choix = input('Voulez-vous chiffrer ou dechiffrer un message (c/d) ?')
    return choix


#  exercice 3

def input_cle(choix = 0):
    while choix < 1:
        choix = int(input('Entrez la cle de chiffrement (1-104)'))
    return choix


# exercice 4


def pos(c):
    """
    >>> pos('G')
    32
    >>> pos('a')
    0
    >>> pos('azerty')
    -1
    """
    
    if c not in ALPHABET:
        return -1
    else:
        for i in range(len(ALPHABET)):
            if c == ALPHABET[i]:
                return i
            
# exercice 5


def car(n):
    """
    >>> car(23)
    'x'
    """
    return ALPHABET[n]

# exercice 6

def chiffre_car(c, n):
    """
    >>> chiffre_car('W',23)
    '3'
    >>> chiffre_car('g',23)
    'D'
    """
    c = (pos(c))
    return(car((c + n)% len(ALPHABET)))


# exercice 7

def cesar(message, mode, cle):
    """
    >>> cesar('help me obi wan kanobi you are my only hope.','c',23)
    'EBIMdJBdLyFdTxKdHxKLyFdVLRdxOBdJVdLKIVdELMB{'
    >>> cesar('EBIMdJBdLyFdTxKdHxKLyFdVLRdxOBdJVdLKIVdELMB{','d',23)
    'help me obi wan kanobi you are my only hope.'
    """
    c = ''
    mot= ''
    if mode == 'c' or mode == 'C':
        for elt in message:
            c = chiffre_car(elt, cle)
            mot += c
        return mot
    else:
        for elt in message:
            c = chiffre_car(elt, -cle)
            mot += c
        return mot
    

# exercice 8

def input_methode(choix = ''):
    while choix != 'c' and choix!= 'v':
        choix = input('Quelle methode voulez-vous utiliser : Cesar (c) ou Vigenere (v) ?')
    return choix



# exercice 9

def dechiffre_car(c, n):
    c = (pos(c))
    return(car((c - n)% len(ALPHABET)))


def vigenere(message, mode, mot_cle):
    """
    >>> vigenere('help me obi wan kanobi you are my only hope.','c','python')
    'wCEw(zteHiw_LyG%ynCMup(LDS}hFr)KR%CAAW}oCCt}'
    >>> vigenere('wCEw(zteHiw_LyG%ynCMup(LDS}hFr)KR%CAAW}oCCt}','d','python')
    'help me obi wan kanobi you are my only hope.'
    """
    c = ''
    mot= ''
    if mode == 'c' or mode == 'C':
        for i in range(len(message)):
            c = chiffre_car(message[i], pos(mot_cle[i % len(mot_cle)]))
            mot += c
        return mot
    else:
        for i in range(len(message)):
            c = dechiffre_car(message[i], pos(mot_cle[i % len(mot_cle)]))
            mot += c
        return mot
    
    
# exercice 10

    
def main():
    mot = ''
    while mot == '':
        mot = input("Entrez votre message :")
        print(mot)
    choix = input_mode()
    methode  = input_methode()
    if methode == 'c':
        cle = input('Entrez la cle :')
        return('resultat :'+ cesar(mot, choix, cle))
    else:
        mot_cle = input('Entrez le mot-cle :')
        return('resultat :'+ vigenere(mot, choix, mot_cle))

    
    
    
    
    
if __name__ =="__main__":
    import doctest
    doctest.testmod(verbose = True)
    
