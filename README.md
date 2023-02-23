# bataille navale


Ce code est une implémentation simplifiée du jeu de bataille navale. Le jeu se joue à deux joueurs et chaque joueur possède une grille de jeu où sont disposés ses bateaux. Le but est de couler les bateaux de l'adversaire en jouant tour à tour et en devinant les positions des bateaux adverses.


Fonctions

init_grille(): Initialise une grille vide 10x10.
transforme_pos(pos): Convertit une position sous forme de chaîne de caractères en un tuple de coordonnées.
demande_pos(): Demande à l'utilisateur une position où jouer et la convertit en coordonnées.
pos_bateaux(nom_fichier): Lit un fichier CSV contenant la position des bateaux et les stocke dans un dictionnaire.
touche_coule(position, bateaux): Vérifie si une position touche ou coule un bateau et met à jour la liste des positions du bateau touché.
affiche_grille(grille): Fonction qui affiche la grille de jeu.
maj_grille(grille, coup, position): Fonction qui met à jour la grille de jeu avec le coup joué.
partie_finie(bateaux): Fonction qui vérifie si tous les bateaux ont été coulés.
bataille(): Fonction qui gère le déroulement du jeu de bataille navale.


Utilisation

Le code peut être utilisé en l'état en exécutant la fonction bataille(). Cependant, pour jouer une partie complète, il est nécessaire de créer un fichier CSV contenant la position des bateaux. Ce fichier doit se trouver dans le dossier data et doit être nommé bateaux.csv. Le format du fichier est le suivant:

Le nom du bateau (une chaîne de caractères).
Les positions du bateau (une ou plusieurs chaînes de caractères représentant les coordonnées du bateau sur la grille de jeu).
Les positions des bateaux doivent être séparées par des virgules.

Exemple:

porte-avion,A1,A2,A3,A4,A5
croiseur,B1,B2,B3,B4
contre-torpilleur,D5,D6,D7
sous-marin,H1,H2,H3
torpilleur,J3,J4
