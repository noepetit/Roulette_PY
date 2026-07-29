import numpy as np
import couleur

# aide de claude pour les codes couleurs et remplacer ce que j'avais fais dans affichage_matrice

def colorier(nombre, color):
    if color == "rouge":
        return f"\033[31m{nombre:2}\033[0m"
    if color == "noir":
        return f"\033[37m{nombre:2}\033[0m"
    if color == "vert":
        return f"\033[32m{nombre:2}\033[0m"
    return f"\033[0m"

def affichageMatrice():
    ligne1      = ["   |  ",f"\033[33m{"1ere 12"}\033[0m","  |  ",f"\033[33m{"2eme 12"}\033[0m","  |  ",f"\033[33m{"3eme 12"}\033[0m","  |"]
    separation  = ["---|-------------|-------------|-------------|"]
    pari_bas    = ["   | ",f"\033[33m{"1-18"}\033[0m"," | ",f"\033[33m{"PAIR"}\033[0m",
                   " | ",f"\033[31m{'RED'}\033[0m"," | ", f"\033[37m{"BLACK"}\033[0m",
                   " |",f"\033[33m{'IMPAIR'}\033[0m","| ",f"\033[33m{'19-36'}\033[0m","|"]
    matrice = np.array([[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36],
                        [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
                        [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]])
    matrice_z = np.array([[" "], [0], [" "]])

    matrice_cote_D = np.array([[f"\033[33m{"3èmeL"}\033[0m"], [f"\033[33m{"2èmeL"}\033[0m"], [f"\033[33m{"1èreL"}\033[0m"]])
    for ligne in ligne1:
        print(ligne, end=" ")
    print()
    for ligne in separation:
        print(ligne)

    for ligne1, ligne2, ligne3 in zip(matrice_z, matrice, matrice_cote_D):
        for nombre in ligne1:
            if nombre == " ":
                print("  ", end=" ")
            else:
                coul = couleur.getCouleur(int(nombre))
                print(colorier(nombre, coul), end=" ")
            print("|", end=" ")

        for index, nombre in enumerate(ligne2):
            color = couleur.getCouleur(int(nombre))
            print(colorier(nombre, color), end=" ")
            if index == 3 or index == 7 or index == 11:
                print("|", end=" ")
        for ligne in ligne3:
            print(ligne, end=" ")
        print()

    for ligne in separation:
        print(ligne, end=" ")
    print()
    for ligne in pari_bas:
        print(ligne, end="")
    print()