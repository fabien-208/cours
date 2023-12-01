
#Quel est le séparateur utilisé dans les fichiers csv ?  ";"
#Combien y a-t-il de disciplines ? 14 matières
#Combien y a-t-il d’élève dans la classe ? 40 élèves
#Que dire de l’ordre des élèves dans les fichiers ? ils sont par ordre alphabetique
#Quel est le premier élève dans la liste ? Léa Abu
#Quel est le dernier élève dans la liste ? Sabrina Zazou

def moyenne(liste_notes):
    """
    Retourne la moyenne des notes contenus dans la liste : liste_notes
    :param liste_notes : (list) liste de note avec éventuellement des "A"
    :return : (int or str) moyenne des notes de liste_notes
    >>> moyenne(['A', '12', '5', '11', 'A'])
    9.33
    >>> moyenne(['10', '12', '5', '11', '15'])
    10.6
    >>> moyenne(['A', 'A'])
    'A'
    """
    pass
    somme = 0
    moyenne_matière = 0
    denominateur= 0

    for i in range(len(liste_notes)):
        if liste_notes[i] != 'A':
            somme += int(liste_notes[i])
            denominateur += 1
    if denominateur ==0:
        moyenne_matière = 'A'
    else:
        moyenne_matière = somme/denominateur
        moyenne_matière = int(moyenne_matière*100)/100
    return moyenne_matière


def traitement_csv(nom_du_fichier):
    discipline = []
    eleve = {}
    eleve2 = ()

    with open (nom_du_fichier) as fichier:
        lignes = fichier.readlines()
        for i in range(lignes):
            eleve = {'NOM':ligne[i][0], 'PRENOM':ligne[i][1], 'DATE_DE_NAISSANCE':ligne[i][2]}
            eleve2.append(eleve)
    for I in range(lignes):
        cle = eleve[NOM][PRENOM]
    return eleve2




if __name__=="__main__":
    import doctest
    doctest.testmod(verbose = True)


