import random as rdm

# mode de jeu pour deviner le nmobre
def couleurDuNombre(nb):
    rouge = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    noir = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    if nb == 0:
        return "vert"
    if nb in rouge:
        return "rouge"
    if nb in noir:
        return "noir"

def choix_nombre():
    try:
        nombre_c = int(input("Veuillez choisir un nombre entre 0 et 36 : "))
    except ValueError:
        return choix_nombre()
    if nombre_c < 0 or nombre_c > 36:
        return choix_nombre()
    else:
        return nombre_c

def nombre_aleatoire():
    nb_al = rdm.randint(0,36)
    return nb_al

def compare(nombre_choisi, nombre_aleatoire,couleur):
    if nombre_choisi == nombre_aleatoire:
        return winner1(nombre_aleatoire,couleur)
    else:
        return loser1(nombre_aleatoire, couleur)

def loser1(nombre_aleatoire, couleur):
    print()
    print("---> Vous avez perdu ! ""\n ","Le nombre tiré etait : ", nombre_aleatoire, "couleur : ", couleur)

def winner1(nombre_aleatoire, couleur):
    print()
    print("---> Vous avez gagné ! ", "\n ","Le nombre tiré etait : ", nombre_aleatoire, "|| couleur : ", couleur)

def restart(prenom):
    print()
    print("Voulez-vous rejouer ?")
    choix = input(" oui || non && si vous voulez changer de mode (1) ")
    match choix:
        case "1":
            main(prenom)
        case "o":
            main1(prenom)
        case "oui":
            main1(prenom)
        case "n":
            print("merci d'avoir joué", prenom, "à bientot !")
            exit()
        case "non":
            print("merci d'avoir joué", prenom, "à bientot !")
            exit()
    restart(prenom)

def main1(prenom):
    nombre_choisi = choix_nombre()
    couleur = couleurDuNombre(nombre_choisi)
    print("|--------------------|")
    print("| Nombre choisi : ", nombre_choisi, "|")
    print("| couleur : ", couleur, "   |")
    print("|--------------------|")
    nombre_genere = nombre_aleatoire()
    compare(nombre_choisi, nombre_genere, couleur)

# mode de jeu pour deviner la couleur

def main2(prenom):
    couleur = choix_couleur()
    print("|--------------------|")
    print("| Couleur choisi : ", couleur, "|")
    print("|--------------------|")
    couleur_genere = couleur_aleatoire()
    compare_couleur(couleur, couleur_genere, prenom)


def loser2(couleur):
    print()
    print("---> Vous avez perdu ! ""\n ","La couleur tiré etait : ", couleur)

def winner2(couleur):
    print()
    print("---> Vous avez gagné ! ", "\n ","La couleur tiré etait : ", couleur)


def compare_couleur(couleur, couleur_genere, prenom):
    if couleur == couleur_genere:
        return winner2(couleur_genere)
    else:
        return loser2(couleur_genere)

def choix_couleur():
    couleur = ["vert", "rouge", "noir"]
    try:
        couleur_c = input("Veuillez choisir une couleur : ")
    except ValueError:
        return choix_couleur()
    if couleur_c not in couleur:
        return choix_couleur()
    else:
        return couleur_c

def couleur_aleatoire():
    couleur = ["vert", "rouge", "noir"]
    nb = rdm.randint(0, 2)
    couleur = couleur[nb]
    return couleur

def main(prenom):
    while True:
        print("deux mode sont disponibles :", "\n", "1- DEVINETTE NOMBRE", "\n", "2- DEVINETTE COULEUR")
        choix = int(input("Veuillez choisir un mode de jeu : "))
        match choix:
            case 1:
                main1(prenom)
            case 2:
                main2(prenom)
        restart(prenom)


if __name__ == '__main__':
    prenom = input("Entrez votre prenom : ")
    print("Bienvenue " + prenom + " !")
    print()
    print("     |----------------------------------------------------------------|")
    print("     |    Ceci est une roulette anglaise, faite le bon pronostique !  |")
    print("     |----------------------------------------------------------------|")
    print()
    main(prenom)


