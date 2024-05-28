import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python_exemp01.db')
    cursor = sqliteConnection.cursor()
    print("La base a été crée avec succès et/ou la connexion à la base SQLite s'est faite avec succès.")
    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version : ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Erreur de connexion à la base SQLite.", error)

finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("Fermeture de la connexion à la base SQLite.")