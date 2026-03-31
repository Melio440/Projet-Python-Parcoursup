# Projet-Python-Parcoursup
Durée : 7 semaines
Debut : 28/11/2025
Fin : 16/01/2025

Contraintres

Python obligatoire
SQL valorisé

Notre idée
Idée principal :Un jeu multijoueurs où ils lancent des dés en un temps de tour limité, on veut savoir qui aura le + grand score. Chaque partie se joue en 3 manche, il existe 6 effets speciaux, certains effet speciaux sont forcement la tant que les conditions sont presente , d'autre c'est en fonction du hasard . voici les effets speciaux
Effet speciaux :
1)lorsque 3 dé ont le meme score,  +5 point au score de la manche
2)lorsque 3 dé forme une suite croissante (1-2-3), +4 pt
3)un dé rouge peut apparitre lors de la manche, ça double le score finale de la manche
4)un dé bleu peut apparaître lors de la manche, ça divise le score par 2
5)lorque le joueur relance par tour, il garde son nouveau score
6)i le score est ≤ 6 , le joueur peut lancer une piece et peut gagner + 2 point ou -2
But : avoir le plus grand score sur 3 manches .
Notres avancée :
05/12 on a crée le plus important de notre projet (voir python.py) qui fait en sorte que le joueur 1,2 lancent leurs dés
12/12 Ajout de foncionnalité pour different scores qui pourrais rendre le jeux plus amusant
22/12/2025:

jeu structuré en plusieurs partie pour plus de clarté
codage sur la partie schema.sql
approfondissement connaissance sql
23/12/2025 :
approfondissement connaissance sql
27/12/2025 :
approfondissement connaissance sql library
28/12/2025 :
approfondissement connaissance sql library
30/12/2025 :
Création des differents effets sépciaux (voir tickets 1,2)
31/12/2025 :
Création de Player en language POO
Diffucultés :
Pour ma par (Dani) j'ai des difficultés avec le langagues POO et savoir se qu'il fait dans le programme
8/01/2025 :
ajout des fonction add_player,get_player_objet_name,remove_player,get_player_by_name,get_all_player
creation class player permettant d'identifier le player et son id dans la BDD
approfondissement connaissance sql library
difficulté : faire la classe player pour que ça identifie l'id de la BDD et le nom

10/01/2025:


Creation et ajout des fonction ajouter une manche, ajouter une partie, ajouter un score


mise a jour de la BDD sur schema.sql


Difficulté : rien
11/01/2025 :


creation des fonction roll_dice,calcul_score,play_manche et play_manche_db dans gmae.py


creation des fonction de tout les effets


test des fonctions nouvelle


difficulté : liée le POO a play_manche_db , faire en sorte que ça affiche 3 manche par parties
17/01/2025 :


creation 50% de chance de gagner des point ou perdre des points dans lancer_piece()


suppression de la fonction relance_de


modification des fonctions roll_dice() et piece_de


creation 25% de chance que le de rouge ou de bleu apparait
18/01/2025:


effet speciaux fini


fonction fini, reste plus qu'as assembler dans main ces fonction et crée un systeme de classement


commencement du menu dans le terminal


creation fonction menu() qui permet pour l'instant de quitter la partie, jouer une partie, ajouter des joueurs


creation fonction jouer_partie


modificiation de la fonction play_manche_db()


ajout de # dans certains fonction pour m'aider a comprendre plus rapidement ce que fait les fonction le jour de l'oral


objectif : mettre plus de #


difficulté : creation de la fonction jouer_partie()
21/01/2026 :


creation fonction classement dans database


modification fonction jouer_partie dans game.py


ajout de classement dans menu()
22/01/2026 :


ajout fonction statistique


implementation de la fonction statistique dans menu()


ajout fonctionnalité d'enlever un joueur dans menu


ajout fonctionnalité de voir la liste de joueur dans menu
25/01/2026:


ajout de import time pour avoir un meilleur rendu


PROJET FINI
