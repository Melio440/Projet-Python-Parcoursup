#gestion sqlite
import sqlite3
from player import Player
def connect():
    conn = sqlite3.connect('jeu_de_de.db') #ça m'a crée un fichier jeu_de_de.db
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    return conn,cursor

def add_player(nom):
    conn,cursor = connect()
    add = cursor.execute('INSERT OR IGNORE INTO joueurs(nom) VALUES(?)',(nom,)) 
    #faire (...,) signifie que ça se transforme en tuple
    conn.commit()
    conn.close()
    return add
def get_all_players():
    conn,cursor = connect()
    cursor.execute("SELECT * FROM joueurs;")
    joueurs = cursor.fetchall()
    conn.close()
    return joueurs
def get_player_by_name(nom):
    conn,cursor = connect()
    cursor.execute(f"SELECT * FROM joueurs WHERE nom = ?;",(nom,))
    joueur = cursor.fetchone()
    if joueur == []:
        conn.close()
        return None
    conn.close()
    return joueur
def remove_player(nom):
    conn,cursor=connect()
    verif_remove = False
    rows = get_all_players()
    for row in rows:
        id,noms = row
        if nom == noms:
            verif_remove = True
    cursor.execute(f"DELETE FROM joueurs WHERE nom = ?;",(nom,))
    conn.commit()
    conn.close()
    return verif_remove
def get_player_object_by_name(nom):
    conn,cursor = connect()
    cursor.execute("SELECT id,nom FROM joueurs where nom = ?;",(nom,))
    rows = cursor.fetchone()
    conn.close()
    if rows is None:
        return None
    id,noms = rows
    player = Player(noms,id)
    return player
def add_game(date):
    conn,cursor = connect()
    cursor.execute("INSERT INTO parties(date) VALUES (?);",(date,))
    conn.commit()
    recup_id = cursor.lastrowid
    conn.close()
    return recup_id
def add_manche(id_partie,numero):
    conn,cursor = connect()
    cursor.execute("INSERT INTO manches(id_partie,numero_manche) VALUES (?,?);",(id_partie,numero,))
    conn.commit()
    recup_id = cursor.lastrowid
    conn.close()
    return recup_id

def add_score(id_joueur, id_manche, score):
    conn,cursor = connect()
    cursor.execute("INSERT OR IGNORE INTO resultats(id_joueur,id_manche,score) VALUES (?,?,?);",(id_joueur,id_manche,score,))
    conn.commit()
    conn.close()

def classement():
    conn,cursor = connect()
    cursor.execute("""SELECT joueurs.nom,sum(score) from resultats
                   JOIN joueurs ON joueurs.id == resultats.id_joueur
                   GROUP BY joueurs.id
                   ORDER BY sum(score) DESC;""")
    
    classement = cursor.fetchall()
    conn.close()
    return classement
def statistique_joueur(nom):
    conn,cursor = connect()
    cursor.execute("""SELECT COUNT(DISTINCT id_partie) FROM resultats JOIN manches ON  resultats.id_manche == manches.id WHERE resultats.id_joueur == ?;""", (nom.id,))
    nb_p = cursor.fetchone()
    cursor.execute("""SELECT MAX(score) FROM resultats where resultats.id_joueur == ?;""",(nom.id,))
    max_s = cursor.fetchone()
    cursor.execute("""SELECT MIN(score) FROM resultats where resultats.id_joueur == ?;""",(nom.id,))
    min_s = cursor.fetchone()
    conn.close()
    return nb_p,max_s,min_s



