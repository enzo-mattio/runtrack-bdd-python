CREATE TABLE etage (
  id INT NOT NULL AUTO_INCREMENT,
  nom VARCHAR(255),
  numero INT,
  superficie INT,
  PRIMARY KEY (id)
);

CREATE TABLE salles (
  id INT NOT NULL AUTO_INCREMENT,
  nom VARCHAR(255),
  id_etage INT,
  capacite INT,
  PRIMARY KEY (id),
  FOREIGN KEY (id_etage) REFERENCES etage(id)
);
