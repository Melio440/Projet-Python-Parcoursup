#lance le jeu
from database import * #on est dans le fichier main.py 
from game import *
from player import Player
import time
conn, cursor = connect()  # appel de la fonction
def menu():
    while True:
        menu = input("1- Ajouter un joueur\n2- Jouer une partie\n3- Classement\n4- Stats joueur\n5- Liste joueur\n6- Regle du jeu\n7- Enlever un joueur\n8- Quitter la partie\nVotre reponse :  ")
        if menu == '1':
            nom_joueur = input('Quelle est le nom du nouveau joueur?: ')
            if get_player_object_by_name(nom_joueur) is not None:
                print(f"{nom_joueur} a deja été choisi, choisissez en un autre")
            else:
                add_player(nom_joueur)
                print(f"Vous avez ajouter le joueur {nom_joueur}")
        elif menu == '2':
            nom_joueur = input("Nom du premier joueur  : ")
            nom_joueur2 = input("Nom du dexuieme joueur : ")
            player = get_player_object_by_name(nom_joueur)
            player2 = get_player_object_by_name(nom_joueur2)
            if player is None:
                print(f"{nom_joueur} n'est pas inscrit dans la base de donnée, ajoutez le en appuyant sur 1")
            if player2 is None:
                print(f"{nom_joueur2} n'est pas inscrit dans la base de donnée")
            elif player and player2 is not None:
                total_1, total_2 = jouer_partie(player,player2)
                if total_1 > total_2:
                    print(f"{nom_joueur} as gagné ! ")
                elif total_2 > total_1:
                    print(f"{nom_joueur2} as gagné ! ")
                else:
                    print(f"{nom_joueur} et {nom_joueur2} ayant le meme score, c'est donc une egalité !")
        elif menu == '3':
            top = classement()
            rang = 1
            print("VOICI LE CLASSEMENT BASE SUR VOTRE SCORE TOTALE DES PARTIES")
            for joueurs in top:
                print(f"{rang}: {joueurs[0]} -> {joueurs[1]} points")
                rang += 1
            time.sleep(3)
        elif menu == '4':
            joueur = input("Quelle joueur voulez vous avoir les stats : ")
            joueur_class = get_player_object_by_name(joueur)
            if joueur_class is None:
                print(f"{joueur} n'est pas inscrit en tant que joueur dans la base de donnée, pour voir la liste de joueur, appuyez 5")
            else:
              nb_partie,max_score,min_score = statistique_joueur(joueur_class)
              print(f" STATS DE {joueur}")
              print(f"Partie jouées : {nb_partie[0]}")
              if max_score[0] is None:
                print("Meilleur score obtenu : 0")
                print("Moins bon score obtenu : 0")
              else:
                print(f"Meilleur score obtenu : {max_score[0]}")  
                print(f"Moins bon score obtenu : {min_score[0]}")
            print(time.sleep(3))
        elif menu == '5':
            liste_j = get_all_players()
            for player in liste_j:
                print(player[1])
            time.sleep(3)
        elif menu == '6':
            print("C'est un jeu où 3 dé sont lancé par manches, une partie est composé de 3 manches.\n Lorsque la manche du premier joueur se finit, la manche du second joueur commence et inversement\nVoici les differents effets speciaux:\n1- Suite_Croissant : Si vos 3 dés forment une liste croissante, votre score augmentera de 4 points\n2- Triple_identique : Si vos 3 dés sont tombé sur la meme case, votre score augmentera de 5 points\n3- De_rouge :  il y'a 20% de chance qu'un dé rouge apparaisse, si il apparait, votre score se multipliera par 2\n4- De_bleu : il y'a 20ù de chance qu'un dé bleu apparaisse, si il apparait, votre score se divisera par 2\n5- Piece : Si votre score est inferieur à 8, une piece apparaitra, si vous choississez de tenter la piece et que vous trouvez la bonnne face de la piece, vous score augmentera de 2 points, si vous vous trompez, votre score diminuera de 2points")
            time.sleep(10)
        elif menu == '7':
            player_remove = input('Nom du joueur que voulez vous supprimez : ')
            player_remove_object = get_player_object_by_name(player_remove)
            if player_remove_object is None:
                print(f"{player_remove} n'est pas inscrit en tant que joueur dans la base de donnée, pour voir la liste de joueur, appuyez 5")
            else:
                remove_player(player_remove)
                print(f"{player_remove} a bien ete supprimer")
            time.sleep(3)
        elif menu == '8':
            return 'Vous venez de quitter la partie'

for player in get_all_players():
    print(player)