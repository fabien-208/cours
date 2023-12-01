#!/usr/bin/env python
# -*- coding: utf-8 -*-




def char2bin8(char):
    """
    convertit un charactere en chaine binaire
    >>> char2bin8('N')
    '01001110'
    """
    char= ord(char)
    binaire = ''
    poids = 128
    while poids !=0:
        if char >= poids:
            char -=poids
            binaire +='1'
        else:
            binaire +='0'
        poids = poids//2
    return binaire

def str2bin8(texte):
    """
    convertit un string en chaine binaire
    
    >>> str2bin8('NSI')
    '010011100101001101001001'
    """
    binaire = ''
    for i in range(len(texte)):
        char= ord(texte[i])
        poids = 128
        while poids !=0:
            if char >= poids:
                char -=poids
                binaire +='1'
            else:
                binaire +='0'
            poids = poids//2
    return binaire

def bin8_to_int(chaine_binaire8):
    """
    convertit du binaire en integer
    >>> bin8_to_int('01101111')
    111

    """
    n = 0
    for i in range(8):
        n += int(chaine_binaire8[i]) * 2 ** (7 - i)
    return n


def int2char(entier):
    """
    convertit un integer en un caractère
    >>> int2char(46)
    '.'
    """
    return chr(entier)


def bits2string(bits):
    """
    Convertit des bits en string
    >>> bits2string('011000010110001001100011')
    'abc'
    """
    t = ""
    for i in range(0, len(bits), 8):
        t += int2char(bin8_to_int(bits[i:i+8]))
    return t

def chiffre_bin_xor(chaine_binaire, clef_binaire):
    """
    Permet de chiffrer du binaire en le convertissant en xor
    """
    chiffre = ""
    for i in range(len(chaine_binaire)):
        chiffre += str(int(chaine_binaire[i]) ^ int(clef_binaire[i % len(clef_binaire)]))
    return chiffre


def bits2hex(chaine_binaire8):
    
    dict = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    d = bin8_to_int(chaine_binaire8)
    hexa = ''
    while d > 0:
        remain = d % 16
        hexa = dict[remain] + hexa
        d = d // 16
    return hexa

def genere_clefs_publique_et_privee(a, b, c, d):
    """
    >>> genere_clefs_publique_et_privee(5, 2, 8, 6)
    ((77, 479.0), (56, 479.0))
    """
    M = a * b - 1
    e = c * M + a
    f = d * M + b
    n = (e * f - 1) / M
    return (e, n), (f, n)


def chiffre_char(a, clef):
    """
    chiffre unn caractere avec un clé publique
    >>> chiffre_char('z', (24, 38))
    '\\x02'
    """
    return chr(ord(a) * int(clef[0]) % int(clef[1]))





def dechiffre_char(a, clef):
    
    return chr(ord(a) * int(clef[0]) % int(clef[1]))



def chiffre_message(message, clef):
    message_chiffre = ''
    for m in message:
        message_chiffre += chiffre_char(m, clef)
    return message_chiffre





def dechiffre_message(message, clef):
    
    message_dechiffre = ''
    for i in message:
        message_dechiffre += dechiffre_char(i, clef)
    return message_dechiffre


if __name__ == __name__:
    import doctest
    doctest.testmod(verbose=True)


