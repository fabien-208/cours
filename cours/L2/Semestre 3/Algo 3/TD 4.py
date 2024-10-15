def fusionner(liste1, liste2):
    if not liste1:
        return liste2
    if not liste2:
        return liste1
    if liste1[0] < liste2[0]:
        return [liste1[0]] + fusionner(liste1[1:], liste2)
    else:
        return [liste2[0]] + fusionner(liste1, liste2[1:])



def tri_par_dénombrement(liste):
    pass





def main():
    liste1 = [1, 3, 5, 7, 9]
    liste2 = [2, 4, 6, 8, 10]
    print(fusionner(liste1, liste2))



main()