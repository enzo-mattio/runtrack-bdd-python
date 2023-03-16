'''
Récupérer votre base de données “LaPlateforme” créée hier. À l’aide du module
“mysql-python-connector”, connectez-vous à votre base de données “LaPlateforme”.
Récupérer l’ensemble des étudiants et afficher le résultat de la requête en console.
'''
import mysql.connector

# Créer une connexion à la base de données
cnx = mysql.connector.connect(  user='root', password='Enzane0728*', host='localhost', database='LaPlateforme', auth_plugin='mysql_native_password')
print(cnx)

# Créer un curseur pour exécuter des requêtes SQL
cursor = cnx.cursor()

# Exécuter la requête SQL pour récupérer tous les étudiants
req = "SELECT * FROM etudiants"
cursor.execute(req)

# Afficher les résultats de la requête en console
for (id, nom, prenom, age, email) in cursor:
  print(f"ID: {id} \nNOM: {nom} \nPRENOM: {prenom} \nAGE: {age}")


# Fermer le curseur et la connexion
cursor.close()
cnx.close()
