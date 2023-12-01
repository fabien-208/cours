# Créé par fpiat, le 13/10/2022 en Python 3.7

import sqlite3
try:
    sqliteConnection = sqlite3.connect('SQLite_Python_exemp01.db')
    sqlite_create_table_query = '''CREATE TABLE SqliteDb_eleves (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email text NOT NULL UNIQUE
    );'''
    cursor = sqliteConnection.cursor()
    print("Connexion SQLite réussie")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit() # obligation permet de réaliser les opérations sur la base.
    print("La table a été créée avec succès.")
    #données#
    cursor.close()

except sqlite3.Error as error:
    print("Erreur lors de la création de la table SQLite: ", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("Fermeture de la connexion à la base de données SQLite.")
