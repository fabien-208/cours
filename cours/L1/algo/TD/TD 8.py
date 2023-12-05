
les_classes = {'C1': C1, 'C2': C2}
C1 = 

MOTS = {'TV': TV, 'radio': radio, 'rare' : rare, 'programme': programme}

def nettoie_et_aclate(phrase):
    for elt in phrase:
        if elt in ",.;:":
            phrase = phrase.replace(elt,'')
    return phrase.split()


def lire_document_classe(texte, classe, les_classes):
    udfr = nettoie_et_aclate(texte)
    if classe not in les_classes:
        les_classes[classe] = {}
        les_classes[classe][nb_mots] = 0
        les_classes[classe][nb_docs] = 0
        les_classes[classe][mots] = {}
    dictt = les_classes[classe]
    for elt in udfr:
        if elt in MOTS:
            dictt[MOTS][elt] = {}
            dictt[MOTS][elt]['nb_occ'] = 0
        else:
            dictt['nb_occ'] += 1
            dictt[MOTS][elt][nb_occ] += 1
            