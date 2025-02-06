import time
from tracemalloc import start


personne = {
    1: (2, 3, 4, 6),
    2: (1, 3, 5, 6),
    3: (1, 3, 5, 6),
    4: (1, 2, 3, 6),
    5: (2, 6),
    6: ()
}

def cherche_celebrité(personne):
    n = len(personne)
    for i in range(1, n + 1):
        est_celebre = True
        for j in personne:
            if j != i:
                if i not in personne[j] or i in personne[i]:
                    est_celebre = False
                    break
        if est_celebre:
            return i
    return -1

print("La célébrité est : {}".format(cherche_celebrité(personne)))


def cherche_celebrité_V2(personne):
    n = len(personne)
    candidat = 1

    for i in range(2, n + 1):
        if candidat in personne[i]:
            continue
        else:
            candidat = i

    for i in range(1, n + 1):
        if i != candidat and (candidat not in personne[i] or i in personne[candidat]):
            return -1

    return candidat

print("La célébrité efficace est : {}".format(cherche_celebrité_V2(personne)))



start = time.time()
cherche_celebrité(personne)
end = time.time()
print("Temps d'exécution de la première fonction : {}".format(end - start))
start = time.time()
cherche_celebrité_V2(personne)
end = time.time()
print("Temps d'exécution de la deuxième fonction : {}".format(end - start))