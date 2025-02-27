import copy

billet = [1, 5, 10, 50, 100]

def nb_echange_pos(s:int, billet:list[int], index:int = 0 ) -> int:
    if s == 0:
        return 1
    if s < 0 or index >= len(billet):
        return 0

    return nb_echange_pos(s - billet[index], billet, index) + nb_echange_pos(s, billet, index + 1)



def nb_chiffre_int(n:int, nb:int = 1) ->int:
    if n < 10:
        return nb
    else:
        return nb_chiffre_int(n//10, nb + 1)



def copie_rec(liste):
    pass


def main():
    print(nb_echange_pos(90, billet))
    print(nb_chiffre_int(1234))
    print(nb_chiffre_int(3456789))




main()