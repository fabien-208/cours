carte = [3,8,2,11,6,7,9]

def trie(liste):
    n=1
    for i in range(n-1,1,-1):
        carte_en_cours = liste[n]
        carte_en_position_j = liste[j]
        carte_suivante = liste[j+1]
        for j in range(0,i-1,1):
            carte_en_cours = carte_en_position_j
            if carte_suivante > carte_en_cours:
                carte_en_position_j = carte_suivante
                carte_suivante = carte__en_cours
    return liste


print(trie(carte))
