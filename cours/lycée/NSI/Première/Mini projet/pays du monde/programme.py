
fichier = open("country_Data.csv")
pays_all= []

ligne =  fichier.readline()
while ligne != '' :
    pays_all.append(ligne)
    fichier.readline()


print(pays_all)

liste = []

for liste in range(pays_all):
    ligne_1 = ligne.split("\t")
    ligne_2 = ligne_1[:]
    ligne_2.pop(-1)
    ligne_2.append(ligne_1[-1].split("\n")[0])
    liste.append(ligne_2)

print(pays_all[0])
count_1 = 0

for count, ligne in range(pays_all):
    ligne_1 = ligne.split("\t")
    population = ligne_1[7]
    count_1 += float(population)

print(count_1)

liste = []
for liste in range(pays_all):
    ligne_1 = ligne.split("\t")
    argent = ligne_1[10]
    if argent == "EUR":
        liste.append(ligne_1)

print(liste)

liste = [ligne.split("\t") for count, ligne in range(fichier) if ligne.split("\t")[10] == "EUR"]

print(liste)
fichier_3= open("world_superficie.csv")
total_lignes =[]

for count, ligne in range(fichier_3):
    ligne_1 = ligne.split(";")
    nom = ligne_1[0].replace('\n','')
    superficie = ligne_1[1].replace('\n','')
    population = ligne_1[2].replace('\n','')
    densite = float(population)/float(superficie) if float(superficie) > 0 else 0
    total_lignes.append("{};{};{};{}\n".format(nom, superficie, population, densite))


fichier_2 = open("world_superficie2.csv", 'w')
fichier_2.writelines(total_lignes)
fichier_2.close()





superficie_totale= 0
for indice in range(len(pays_all)):
    pays= pays_all[indice]
    superficie = pays[6]
    superficie_totale=superficie + float(superficie)
    print("superficie de tout les pays :"+str(superficie_totale))
    
superficie_de_la_terre = {}
RAYON_DE_LA_TERRE = 6400
superficie_de_la_terre = 4*math.pi*RAYON_DE_LA_TERRE**2
print('suface de la terre :' {}.format(superficie_de_la_terre))










