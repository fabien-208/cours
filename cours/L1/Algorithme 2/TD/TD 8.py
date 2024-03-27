# exercice 1

def retirer_max(p):
    pile = Pile()
    if len(p) == 0:
        return None
    max = p.pop()
    while len(pile) != 0:
        elt = p.pop()
        if elt > max:
            pile.push(max)
            max = elt
        else:
            pile.pop(elt)
    while len(pile) != 0:
        p.push(pile.pop())
    return max



# exercice 2

def inverse_der_prem(mafile):
    last = mafile.pop()
    file = File()
    while not mafile.est_vide():
        elt = mafile.pop()
        if mafile.est_vide():
            first = elt
        else:
            file.push(elt)
    mafile.push(first)
    while not file.est_vide():
        mafile.push(file.pop())
    mafile.push(last)