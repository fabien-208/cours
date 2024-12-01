
def est_dans_arbre(noeud, ent):
    if noeud is None:
        return False
    if noeud.val == ent:
        return True
    if noeud.val < ent:
        return est_dans_arbre(noeud.right, ent)
    return est_dans_arbre(noeud.left, ent)

def maximum(noeud):
    current = noeud
    while current.right is not None:
        current = current.right
    return current.val


def un_fils(noeud):
    if noeud is None:
        return []
    result = []
    if (noeud.left is None) != (noeud.right is None):
        result.append(noeud.val)
    result.extend(un_fils(noeud.left))
    result.extend(un_fils(noeud.right))
    return result


def internes(noeud):
    if noeud is None or (noeud.left is None and noeud.right is None):
        return []
    result = [noeud.val]
    result.extend(internes(noeud.left))
    result.extend(internes(noeud.right))
    return result




def feuilles_negatives(noeud):
    if noeud is None:
        return []
    if noeud.left is None and noeud.right is None:
        return [noeud.val] if noeud.val < 0 else []
    result = []
    result.extend(feuilles_negatives(noeud.left))
    result.extend(feuilles_negatives(noeud.right))
    return result


def hauteur(noeud):
    if noeud is None:
        return -1
    left_height = hauteur(noeud.left)
    right_height = hauteur(noeud.right)
    return 1 + max(left_height, right_height)




def nombre_sommets(noeud):
    if noeud is None:
        return 0
    return 1 + nombre_sommets(noeud.left) + nombre_sommets(noeud.right)