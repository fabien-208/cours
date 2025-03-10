
-- EXERCICE 1

SELECT titre FROM Livre; -- Question 1

SELECT titre FROM Livre WHERE Langue is 'FR'; -- Question 2

SELECT titre FROM Livre JOIN Emprunter ON cote.Emprunter = cote.Livre; -- Question 3

SELECT nom, prenom FROM Etudiant, Emprunter WHERE Etudiant.num_etu=Emprunter.num_etu; -- Question 4

SELECT titre FROM Livre JOIN Ecrire JOIN Auteur ON Auteur.num_aut = Ecrire.num_aut AND Ecrire.cote = Auteur.cote WHERE Auteur.nom is 'Tanenbaum' AND Auteur.prenom is 'Andrew'; -- Question 5

SELECT nom FROM Etudiant WHERE date_nais(SELECT MIN(date_nais) FROM Etudiant); -- Question 6

SELECT titre FROM Livre JOIN cote USING(cote) GROUP BY cote HAVING COUNT(*) = (SELECT MAX(N) FROM (SELECT COUNT(*) N FROM Emprunter GROUP BY cote));-- Question 7

SELECT ISBN FROM Livre JOIN Etudiant JOIN Emprunter ON livre.cote = Emprunter.cote AND Emprunter.num_etu = Etudiant.num_etu WHERE Etudiant.prenom = 'Julien' AND Etudiant.nom = 'Dallet' -- Question 8

SELECT titre FROM Livre JOIN Emprunter ON livre.cote = Emprunter.cote WHERE YEAR(Date_emprunt) = 2011 AND MONTH(Date_emprunt) = 1;-- question 9

SELECT COUNT(*) FROM Ecrire GROUP BY num_aut; -- Question 14

-- EXERCICE 2

SELECT AVG(duree) FROM (SELECT Date_restitution - Date_emprunt duree FROM Emprunter);-- Question 1

SET LC_Time = 'FRENCH'
SELECT TO_CHAR(Date_emprunt, 'TMDay') FROM Emprunter WHERE num_etu = 22109870001;-- Question 2

SELECT * FROM Livre JOIN Emprunter USING(cote) WHERE TO_CHAR(Date_emprunt, 'TMDAy') = 'Lundi'; -- Question 3

SELECT * FROM Livre JOIN Emprunter USING(cote) WHERE TO_CHAR(Date_emprunt, 'TMDAy') = 'Lundi' AND TO_CHAR(Date_restitution, 'TMDAY') = 'mardi'; -- Question 4

SELECT titre FROM livre JOIN Emprunter USING(cote) WHERE MONTH(Date_emprunt) = 3; -- Question 5

SELECT titre FROM livre JOIN Emprunter USING(cote) WHERE MONTH(Date_emprunt)  IN (1,2,3,4); -- Question 6

SELECT AVG(duree) FROM (SELECT Date_restitution - Date_emprunt duree FROM Emprunter WHERE YEAR(Date_emprunt) = 15) GROUP BY MONTH(Date_emprunt);-- Question 7

SELECT DISTINCT titre FROM livre JOIN Emprunter ON livre.cote = Emprunter.cote WHERE EXTRACT(DAY FROM Date_emprunt = 1) AND EXTRACT(YEAR FROM Date_emprunt = 2015);-- Question 8