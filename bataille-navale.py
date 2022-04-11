from pprint import pprint
import csv
import os

def init_grille():
    grille = []
    for i in range(10):
        grille.append([" "] * 10)
    return grille

def transforme_pos(pos):
    numero_ligne = int(pos[1:]) - 1
    liste_lettres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    numero_colonne = liste_lettres.index(pos[0])
    return (numero_ligne, numero_colonne)

def demande_pos():
    pos = input("Entrez une position pour jouer ")  #B10
    (numero_ligne, numero_colonne) = transforme_pos(pos)
    return (numero_ligne, numero_colonne)

def pos_bateaux(nom_fichier):
    fp = open(nom_fichier, "r", encoding="utf-8")
    bateaux = {}
    for ligne in csv.reader(fp, delimiter=","):
        nom_bateau = ligne[0]
        positions = ligne[1:]
        bateaux[nom_bateau] = []
        for pos in positions:
            l, c = transforme_pos(pos)
            bateaux[nom_bateau].append((l, c))
    return bateaux

def touche_coule(position, bateaux):
    for nom, liste_pos in bateaux.items():
        if position in liste_pos:
            liste_pos.remove(position)
            if len(liste_pos) == 0:
                print("Bateau ", nom, " coulé")
            else:
                print("Touché")
            return "O", bateaux
    print("A l'eau")
    return "X", bateaux

def affiche_grille(grille):
    print("   ABCDEFGHIJ")
    for i, ligne in enumerate(grille):
        print("{:02d}:".format(i + 1), end="")
        for lettre in ligne:
            print(lettre, end="")
        print()

def maj_grille(grille, coup, position):
    l, c = position
    grille[l][c] = coup
    return grille

def partie_finie(bateaux):
    for positions in bateaux.values():
        if len(positions) > 0:
            return False
    return True

def bataille():
    fichier = os.path.join("data", "bateaux.csv")
    bateaux = pos_bateaux(fichier)
    grille = init_grille()
    cpt = 0
    while not(partie_finie(bateaux)):
        pos = demande_pos()
        coup, bateaux = touche_coule(pos, bateaux)
        grille = maj_grille(grille, coup, pos)
        affiche_grille(grille)
        cpt +=1
    print("Partie gagnée en {} tours".format(cpt))

# pprint(init_grille())
# print(demande_pos())
# chemin = os.path.join("data", "pos_bateaux.csv")
# bateaux = pos_bateaux(chemin)
# resultat, bateaux = touche_coule((0, 0), bateaux)
# print(resultat, bateaux)
# resultat, bateaux = touche_coule((0, 3), bateaux)
# resultat, bateaux = touche_coule((1, 3), bateaux)
# resultat, bateaux = touche_coule((2, 3), bateaux)
# print(resultat, bateaux)

# grille = init_grille()
# grille = maj_grille(grille, "X", (3, 7))
# affiche_grille(grille)

bataille()

