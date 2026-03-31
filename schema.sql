--- structure
PRAGMA FOREIGN_keys = ON;
DROP TABLE IF EXISTS resultats;
DROP TABLE IF EXISTS manches;
DROP TABLE IF EXISTS parties;
DROP TABLE IF EXISTS joueurs;
CREATE TABLE joueurs(
    id INTEGER PRIMARY KEY, 
    nom TEXT UNIQUE NOT NULL);
CREATE TABLE parties(
    id INTEGER PRIMARY KEY ,
    date TEXT);
CREATE TABLE manches(
    id INTEGER PRIMARY KEY,
    id_partie INTEGER,
    numero_manche INTEGER,
    FOREIGN KEY (id_partie) REFERENCES parties(id)
    ON DELETE CASCADE
    ); 
CREATE TABLE resultats(
    id INTEGER PRIMARY KEY,
    id_joueur INTEGER,
    id_manche INTEGER,
    score INTEGER,
    FOREIGN KEY(id_joueur) REFERENCES joueurs(id)
    ON DELETE CASCADE,
    FOREIGN KEY(id_manche) REFERENCES manches(id)
    UNIQUE(id_joueur,id_manche)
    );
