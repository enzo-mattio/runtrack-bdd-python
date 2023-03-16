'''
Écrire un programme qui récupère tous les noms et les capacités de la table “salles” et
afficher le résultat en console.
'''

import mysql.connector
sepator = "----------------------------------------"
# Créer une connexion à la base de données
cnx = mysql.connector.connect(  user='root', password='Enzane0728*', host='localhost', database='LaPlateforme', auth_plugin='mysql_native_password')
print(cnx)

# Créer un curseur pour exécuter des requêtes SQL
cursor = cnx.cursor()

# Récupérer les données des salles
req = "SELECT * FROM salles"
cursor.execute(req)

# Afficher les résultats de la requête en console

for (id, nom, id_etages, capacité) in cursor:
  print(f"{sepator} \nNom: {nom} \nEtage: {id_etages} \nCapacité: {capacité}")