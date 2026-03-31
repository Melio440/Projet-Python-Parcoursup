#gestion des joueurs
class Player:
    def __init__(self, nom, id=None):
        self.id = id      # id dans la base, peut être None au début
        self.nom = nom    # nom du joueur
    def __str__(self):
        return f"Joueurs : {self.nom} (id={self.id})"

