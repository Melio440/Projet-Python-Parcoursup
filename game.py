#logique du jeu (dés,manche,effets)
import random as r
from database import *
from player import Player
import time
def roll_dice():
    liste_de = []
    relance = 1
    for _ in range(3):
        bad_word = 2
        print("~druum~")
        time.sleep(2)
        de = r.randint(1,6)
        if relance > 0:
            ask = input(f"Votre de est tombé sur la case {de}, voulez vous relancer? Vous pouvez relancez qu'une fois par manche o / n : ")
            if ask == 'o':
                de = r.randint(1,6)
                relance -= 1
                print("~druum~")
                time.sleep(2)
                print(f"Votre de est tombe sur la case {de}")
            elif ask == 'n':
                ...
            else:
                #permet que ça repete le programme si la lettre choisis est pas la bonne
                while ask  != 'n' and ask != 'o':
                    #permet qu'en cas de tentative eronnee repeter, ça cesse
                    if bad_word == 0:
                        print(f"Trop de tentative incorrect, nous allons donc gardez le resultat initaile de votre de, soit {de}")
                        break
                    print("Vous n'avez pas pris la bonne lettre, ressayez")
                    ask = input(f"Votre de est tombe sur la case {de}, voulez vous relancer? Vous pouvez relancez qu'une fois o / n : ")
                    if ask == 'o':
                        de = r.randint(1,6)
                        relance -= 1
                        print(f"Votre de est tombe sur la case {de}")
                        break
                    if ask == 'n':
                        relance -= 1
                    else:
                        bad_word -= 1
        else:
            time.sleep(2)
            print(f"Votre de est tombé sur la case {de}")
            
       
        
        liste_de.append(de)
    return liste_de
def calcul_score(des):
    score = 0
    for i in range(len(des)):
        score += des[i]
    return score
def play_manche():
    des = roll_dice()
    score = calcul_score(des)
    score = triple_identique(score,des)
    score = suite_croissante(score,des)
    score = proba_de(score)
    score = piece_de(score)
    return score
def play_manche_db(player,id_partie,numero_manche):
    score = play_manche()
    id_m = add_manche(id_partie,numero_manche)
    add_score(player.id,id_m,score)
    return score
def jouer_partie(joueur1,joueur2):
    id_partie = add_game('03/01/2025')
    numero_manche = 0
    resultats = []
    resultats2 = []
    total = 0
    total2 = 0
    for _ in range(3):
        numero_manche += 1
        res = play_manche_db(joueur1,id_partie,numero_manche)
        resultats.append((numero_manche,res,)) 
        #permet de crée une liste de tuple qui contient l'id de la manche et le score de la manche 
        total += res
        for r in resultats:
            print(f"Joueur : {joueur1.nom}\n Manche {r[0]} -- Score = {r[1]}")
        print(f"TOTAL: {total}")
        res2 = play_manche_db(joueur2,id_partie,numero_manche)
        resultats2.append((numero_manche,res2,))
        total2 += res2
        for r2 in resultats2:
            print(f"Joueur : {joueur2.nom}\n Manche {r2[0]} -- Score = {r2[1]}")
        print(f"TOTAL: {total2}")
    return total,total2



#effets:
#effet 1
def triple_identique(score,des):
    verif = True
    relance = des[0]
    for i in range(len(des)):
        if relance != des[i]:
            verif = False
    if verif:
        print("L'effet triple_identique va etre appliqué ! +5 points")
        score += 5
    return score
#effets 2
def suite_croissante(score,des):
    verif = False
    des.sort()
    relance = 0
    for i in range(1,len(des)):
        if des[relance] + 1 != des[i] :
            verif = False
            break
        else:
            relance = i
            verif = True
    if verif:
        print("L'effet suite_croissante va etre appliqué ! +4 points")
        score += 4
    return score
def de_rouge(score):
    return score * 2
def de_bleu(score):
    return score // 2
def proba_de(score):
    chance_red = r.choice([1,1,0,1,1]) #permet de crée une probabilité de 20%
    chance_bleu = r.choice([1,1,0,1,1]) # permet de crée une probabilité de 20%
    if chance_red == 0:
        print("Vous etes tombé sur le dé rouge ! Votre score va etre multiplié par 2")
        return de_rouge(score)
    if chance_bleu == 0:
        print("Vous etes tombé sur le dé bleu ! Votre score va etre divisé par 2")
        return de_bleu(score)
    else:
        return score

def piece_de(score):
    bad_word = 2
    chance = r.choice([1,-1]) #permet de crée une probabilité de 50%
    if score <= 8:
        ask = input("Votre score est inferieur ou egal à 8 , voulez vous jouez a pile ou face? Pile = +2, Face = -2 o / n : ")
        if ask == 'o':
            if chance == 1:
                score += 2
                print("La piece est tombé sur pile, votre score a augmenter de deux points")
                return score
            elif chance == -1:
                score -= 2
                print("La piece est tombé sur face, votre score vient de diminuer de deux points")
                return score
        elif ask == 'n':
            return score
        else:
            #permet que ça repete le programme si la lettre choisis est pas la bonne
            while ask  != 'n' or ask != 'o':
                    #permet qu'en cas de tentative erronnée  repeter, ça cesse
                    if bad_word == 0:
                        print(f"Trop de tentative incorrect, nous allons donc gardez le resultat initaile de votre de, soit {score}")
                        return score
                    print("Vous n'avez pas pris la bonne lettre, ressayez")
                    ask = input("Votre score est inferieur ou egal à 8 , voulez vous jouez a pile ou face? Pile = +2, Face = -2. o / n : ")
                    if ask == 'o':
                        if chance == 1:
                            score += 2
                            print("La piece est tombé sur pile, votre score a augmenter de deux points")
                            return score
                        elif chance == -1:
                            score -= 2
                            print("La piece est tombé sur face, votre score vient de diminuer de deux points")
                            return score
                    elif ask == 'n':
                        return score
                    else:
                        bad_word -= 1
    else:
        return score
