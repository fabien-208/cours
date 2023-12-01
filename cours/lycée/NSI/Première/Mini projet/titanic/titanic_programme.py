# Créé par 1SI, le 31/01/2022 en Python 3.7
#|------------------------------------|
#|           exercice 1               |
#|------------------------------------|
import csv
reader = csv.DictReader(open('titanic.csv','r'))
titanic=[]
for row in reader:
    titanic.append(dict(row))
print(len(titanic))
print(titanic[53])



nombre_survivant= 0
for i in range(len(titanic)):
    if  titanic[i]['Survived']=='1':
        nombre_survivant+=1
print("le nombre de survivant est de : "+str(nombre_survivant))


dico1 = {}
dico1=titanic
passager_class_1 = 216
passager_class_2 = 184
passager_class_3 = 491
survivant_classe_1= 0
survivant_classe_2= 0
survivant_classe_3= 0
pourcentage_survivant_1 =0
pourcentage_survivant_2 =0
pourcentage_survivant_3 =0

for i in range(len(dico1)):
    dico1=titanic[i]
    if  dico1['Survived']=='1':
        if dico1['Pclass']=='1':
            survivant_classe_1 += 1
        elif dico1['Pclass']=='2':
            survivant_classe_2 += 1
        elif  dico1['Pclass']=='3':
            survivant_classe_3+= 1
pourcentage_survivant_1 =int(survivant_classe_1*100/passager_class_1)
pourcentage_survivant_2 =int(survivant_classe_2*100/passager_class_2)
pourcentage_survivant_3 =int(survivant_classe_3*100/passager_class_3)

print("le nombre de survivant en première classe est de : "+str(survivant_classe_1))
print("le nombre de survivant en seconde classe est de : "+str(survivant_classe_2))
print("le nombre de survivant en 3ème classe est de : "+str(survivant_classe_3))
print("le pourcentage de survivant en première classe  est de : "+str(pourcentage_survivant_1))
print("le pourcentage de survivant en seconde classe est de : "+str(pourcentage_survivant_2))
print("le pourcentage de survivant en 3 ème classe est de : "+str(pourcentage_survivant_3))


dico1 = titanic
survivant_cherbourg = 0
for i in range(len(dico1)):
    dico1=titanic[i]
    if  dico1['Survived']=='1':
        if dico1['Embarked']=='C':
            survivant_cherbourg += 1
print("le nombre de survivant embarqué a cherbourg est de : "+str(survivant_cherbourg))


