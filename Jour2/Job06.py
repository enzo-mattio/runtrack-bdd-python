'''
À l’aide d’une requête, calculer la somme des capacités des salles et afficher le résultat
en console.
'''

import mysql.connector
sepator = "----------------------------------------"
# Créer une connexion à la base de données
cnx = mysql.connector.connect(  user='root', password='Enzane0728*', host='localhost', database='LaPlateforme', auth_plugin='mysql_native_password')
print(cnx)

# Créer un curseur pour exécuter des requêtes SQL
cursor = cnx.cursor()

# Récupérer les données des salles
req = "SELECT capacite FROM salles"
cursor.execute(req)

# Faire la somme des capacités
capacite_total = 0
for (capacite) in cursor:
  capacite_total = capacite_total + int(capacite[0])
  
# Afficher les résultats de la requête en console
print(f"{sepator} \nLa capacité totale de La Plateforme est de {capacite_total} personnes")