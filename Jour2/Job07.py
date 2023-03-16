'''
Créer une base de données SQL avec une table nommée “employes” contenant les
champs suivants :
- id, int, primary key, auto-incrémente
- nom, varchar
- prenom, varchar
- salaire, decimal
- id_service, int

Insérer des employées dans la table “employes”.

Écrire une requête SQL pour récupérer tout les employées dont le salaire est supérieur à
3 000 €. Exécuter la requête et afficher le résultat.
Ajouter la table “services” contenant les champs suivants :
- id, int, primary key, auto-incrémente
- nom, varchar
Insérer des services dans votre table.
Récupérer tous les employés et leur service respectif. Afficher le résultat en console.
Créer une classe qui permet d’effectuer différentes opérations (CRUD) sur la table
salariée. Vérifier que tout fonctionne correctement.
'''

import mysql.connector
# sepator = "----------------------------------------"
# # Créer une connexion à la base de données
# cnx = mysql.connector.connect(  user='root', password='Enzane0728*', host='localhost', database='Travail', auth_plugin='mysql_native_password')


# # Créer un curseur pour exécuter des requêtes SQL
# cursor = cnx.cursor()

# # Récupérer les données des employes
# req = "SELECT * FROM employes WHERE salaire > 3000;"
# cursor.execute(req)

# for (id, nom, prenom, salaire, id_service) in cursor:
#   print(salaire)
  
  
  
  
  
  
  
# #Créer une table employes
# req_create = "CREATE TABLE employes (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), prenom VARCHAR(255), salaire DECIMAL(10,2), id_service INT)"
# cursor.execute(req_create)
# #Créer une table services
# req_create = "CREATE TABLE services (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255))"
# cursor.execute(req_create)

# # # Insérer des services dans la table “services”.
# req_add_service = "INSERT INTO services (nom) VALUES (%s)"
# cursor.execute(req_add_service, ("Trader",))
# cursor.execute(req_add_service, ("Développeur",))
# cursor.execute(req_add_service, ("Designer",))
# cursor.execute(req_add_service, ("Chef de projet",))


# # # Insérer des employées dans la table “employes”.
# req_add = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
# cursor.execute(req_add, ("Giga", "Chad", 25000, 1))
# cursor.execute(req_add, ("Pardi", "Haut", 2000, 3))
# cursor.execute(req_add, ("Doe", "John", 5000, 4))
# cursor.execute(req_add, ("Doe", "Jane", 10000, 2))


class CRUD:
    
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Enzane0728*",
            database="Travail",
            auth_plugin='mysql_native_password'
        )
        self.cursor = self.db.cursor()
        
    def create(self, nom, prenom, salaire, id_service):
        sql = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(sql, values)
        self.db.commit()
        print("Salarié créé avec succès.")
        
    def read(self):
        self.cursor.execute("SELECT * FROM employes")
        result = self.cursor.fetchall()
        for row in result:
            print(row)
            
    def update(self, id, salaire):
        sql = "UPDATE employes SET salaire = %s WHERE id = %s"
        values = (salaire, id)
        self.cursor.execute(sql, values)
        self.db.commit()
        print("Salaire mis à jour avec succès.")
        
    def delete(self, id):
        sql = "DELETE FROM employes WHERE id = %s"
        value = (id,)
        self.cursor.execute(sql, value)
        self.db.commit()
        print("Salarié supprimé avec succès.")
        
        
salaries = CRUD()
salaries.create("Dupont", "Jean", 4000.00, 1)
salaries.read()
salaries.update(1, 4200.50)
salaries.delete(2)

