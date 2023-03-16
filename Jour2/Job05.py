'''
À l’aide d’un requête calculer la superficie de l’ensemble des étages et afficher “La
superficie de La Plateforme est de X m2”, X étant le résultat de la requête.
'''

import mysql.connector
sepator = "----------------------------------------"
superficie_total = 0
# Créer une connexion à la base de données
cnx = mysql.connector.connect(  user='root', password='Enzane0728*', host='localhost', database='LaPlateforme', auth_plugin='mysql_native_password')
print(cnx)

# Créer un curseur pour exécuter des requêtes SQL
cursor = cnx.cursor()

# Récupérer les données des etages

req = "SELECT superficie FROM etage"
cursor.execute(req)

# Afficher les résultats de la requête en console
for (superficie) in cursor:
  superficie_total =  superficie_total + int(superficie[0])
print(f"{sepator} \nLa superficie de La Plateforme est de {superficie_total} m2")