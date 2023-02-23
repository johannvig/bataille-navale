from pprint import pprint
import csv
import os


def init_grille():
    """
    Initialise une grille vide 10x10.

    Returns:
        list: Une grille vide.
    """
    grille = []
    for i in range(10):
        grille.append([" "] * 10)
    return grille


def transforme_pos(pos):
    """
    Convertit une position sous forme de chaîne de caractères en un tuple de coordonnées.

    Args:
        pos (str): La position à convertir (ex: "B10").

    Returns:
        tuple: Les coordonnées correspondantes sous forme de tuple (ex: (1, 9) pour "B10").
    """
    numero_ligne = int(pos[1:]) - 1
    liste_lettres = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    numero_colonne = liste_lettres.index(pos[0])
    return (numero_ligne, numero_colonne)


def demande_pos():
    """
    Demande à l'utilisateur une position où jouer et la convertit en coordonnées.

    Returns:
        tuple: Les coordonnées correspondantes sous forme de tuple (ex: (1, 9) pour "B10").
    """
    pos = input("Entrez une position pour jouer ")  # B10
    (numero_ligne, numero_colonne) = transforme_pos(pos)
    return (numero_ligne, numero_colonne)


def pos_bateaux(nom_fichier):
    """
    Lit un fichier CSV contenant la position des bateaux et les stocke dans un dictionnaire.

    Args:
        nom_fichier (str): Le nom du fichier CSV à lire.

    Returns:
        dict: Un dictionnaire contenant les positions de chaque bateau.
    """
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
    """
    Vérifie si une position touche ou coule un bateau et met à jour la liste des positions du bateau touché.

    Args:
        position (tuple): Les coordonnées du coup joué.
        bateaux (dict): Le dictionnaire des positions des bateaux.

    Returns:
        tuple: Le résultat du coup ("O" pour touché, "X" pour à l'eau) et le dictionnaire des bateaux mis à jour.
    """
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


# Fonction qui affiche la grille de jeu
def affiche_grille(grille):
    print("   ABCDEFGHIJ")
    for i, ligne in enumerate(grille):
        print("{:02d}:".format(i + 1), end="")
        for lettre in ligne:
            print(lettre, end="")
        print()

# Fonction qui met à jour la grille de jeu avec le coup joué
def maj_grille(grille, coup, position):
    l, c = position
    grille[l][c] = coup
    return grille

# Fonction qui vérifie si tous les bateaux ont été coulés
def partie_finie(bateaux):
    for positions in bateaux.values():
        if len(positions) > 0:
            return False
    return True

# Fonction qui gère le déroulement du jeu de bataille navale
def bataille():
    # Lecture des positions des bateaux à partir du fichier CSV
    fichier = os.path.join("data", "bateaux.csv")
    bateaux = pos_bateaux(fichier)

    # Initialisation de la grille de jeu
    grille = init_grille()

    # Compteur de tours de jeu
    cpt = 0

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

