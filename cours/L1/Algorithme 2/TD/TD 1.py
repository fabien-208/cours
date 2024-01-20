# Exerice 1

def decomp_facteurs_premiers(nb: int) -> list[int]:
    diviseur = 2
    nb_premier = []
    while nb != 1:
        if nb % diviseur == 0:
            nb_premier.append(diviseur)
            nb = nb // diviseur
        else:
            diviseur += 1
    return nb_premier


# Exercice 2


def racinecarre(a: int, k: int)-> float:
    n = 1
    d = 1
    for i in range(k+1):
        n, d = n**2 + a* d**2, 2*n*d
    return n/d
        
   
# Exercice 3
   
def insere(base, titre, genre, durée):
    return base.append({'titre': titre, 'genre' : genre, 'durée' : durée})


# Exercice 4

def film_par_genre(genre, base):
    liste_film = []
    for i in range(len(base)):
        if genre == base[i]['genre']:
            liste_film.append(base[i]['titre'])
    return liste_film
        

# Exercice 5


def base_genre(base):
    genre = {}
    for film in base:
        if film['genre'] not in genre:
            genre[film['genre']] = []
            genre[film['genre']].append(film['titre'])
        else:
            genre[film['genre']].append(film['titre'])
    return genre


# Exercice 6


def film_plus_long(base):
    duree_max = base[0]['durée']
    film = base[0]['titre']
    for i in range(1, len(base)):
        if base[i]['durée'] > duree_max:
            duree_max = base[i]['durée']
            film = base[i]['titre']
    return film

# Exeerice 7


def present(liste_film, base):
    est_present = []
    for film in base:
        if film['titre'] in liste_film:
            est_present.append(film['titre'])
    return est_present
        
        
#Exercice 8


def meilleur_film(base):
    max_nb_entree = 0
    nom_film = ''
    for film in base:
        if film[1] > max_nb_entree:
            max_nb_entree = film[1]
            nom_film = film[0]
    return nom_film

# exerice 9
## specifiez puis ecrivez la foction ordonne qui recoit la base comme argument. la fonction doit renvoyer une liste de tuples représentant le titre de film et la durée. cette liste doit etre decroissante par rapport aux durée




def ordonne(base):
    duree = []
    liste = []
    for film in base:
        duree.append(film[1])
    sorted(duree)
    print(duree)
    
    for i in range(len(duree)):
        for film in base:
            if duree[i] == film[1]:
                liste.append(film)
    return liste


        
    




