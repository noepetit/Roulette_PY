import random as rnd
import couleur
from Affichage import affichageMatrice

#---------------------      Mise ne place
def genererNombreAleatoire():
    nombreAleatoire = rnd.randint(0, 36)
    return nombreAleatoire

def dmdSoldeTotal():
    while True:
        print("----    solde minimum : 1€ || solde maximum 5000€    ----")
        try :
            solde = int(input("Entrez votre solde : "))
        except ValueError:
            print(f"\033[31m{"Montant invalide !"}\033[0m")
            continue
        if solde < 1 or solde > 5000:
            print(f"\033[31m{"Montant invalide !"}\033[0m")
            continue
        print("Vous avez : ", solde, "€ !")
        return solde

def start(soldeTotal):
    while True:
        if soldeTotal == 0:
            print(f"\033[31m{"Vous n'avez plus de crédit, au revoir..."}\033[0m")
            exit()
        ready = input("Êtes vous près ? (oui/non)")
        if ready == "oui":
            soldeTotal = pari(paris = [], soldeTotal = soldeTotal)
        elif ready == "non":
            print("Dommage !")
            exit()
        else:
            continue

#---------------------      fonction de main
def pari(paris, soldeTotal):
    while True:
        if soldeTotal == 0:
            return finPari(paris, soldeTotal)
        affichageMatrice()
        print("Il vous reste ", soldeTotal, " crédits !")
        try :
            choixPari = int(input("1- Numéro \n"
                         "2- Couleur \n"
                         "3- Pair / Impair \n"
                         "4- Douzaine \n"
                         "5- 1 à 18 ou 19 à 36 \n"
                         "0- Pour arrêter le pari \n"
                                  "Votre choix : "))

            match choixPari:
                case 1:
                    soldeTotal = pariNumero(paris, soldeTotal)
                case 2:
                    soldeTotal = pariCouleur(paris, soldeTotal)
                case 3:
                    soldeTotal = pariPairImpair(paris, soldeTotal)
                case 4:
                    soldeTotal = pariDouzaine(paris, soldeTotal)
                case 5:
                    soldeTotal = pariManquePasse(paris, soldeTotal)
                case 0:
                    soldeTotal = finPari(paris, soldeTotal)
                    return soldeTotal
                case _:
                    print(f"\033[31m{"Saisi invalide !"}\033[0m")
                    continue
        except ValueError:
            print(f"\033[31m{"Saisi invalide !"}\033[0m")
            continue

def choixMontant(soldeTotal):
    while True:
        try :
            montant = int(input("Entrez le montant que vous souhaitez parier : "))
            if montant > soldeTotal:
                print(f"\033[31m{"Vous n'avez pas assez de crédits ! \n"}\033[0m")
                continue
            elif montant < 1:
                print(f"\033[31m{"Et non ! ça ne marche pas comme ça..."}\033[0m")
                continue
            else:
                return montant

        except ValueError:
            print(f"\033[31m{"Nombre invalide !"}\033[0m")
            continue

#set pari :

def pariNumero(paris, soldeTotal):
    while True:
        try:
            if soldeTotal == 0:
                return soldeTotal
            pariJ = int(input("Entrez un nombre sur lequel vous voulez parier : "))
            if pariJ == -1:
                return soldeTotal
            if pariJ < 0 or pariJ > 36:
                print(f"\033[31m{"Nombre indisponible sur une roulette allant de 0 à 36"}\033[0m")
                continue
            montant = choixMontant(soldeTotal)
            soldeTotal = soldeTotal - montant
            paris.append(("Numéros" , pariJ, montant))
            print(f"\033[32m{"Pari ajouté !"}\033[0m")
        except ValueError:
            print(f"\033[31m{"Nombre invalide !"}\033[0m")
            continue


def pariCouleur(paris, soldeTotal):
    while True:
        pariJ = str(input("Entrez une couleur sur laquelle vous voulez parier : "))
        if pariJ == "-1":
            return soldeTotal
        if pariJ != "rouge" and pariJ != "noir":
            print(f"\033[31m{"Couleur invalide !"}\033[0m")
            continue
        montant = choixMontant(soldeTotal)
        soldeTotal = soldeTotal - montant
        if pariJ == "rouge": paris.append(("Couleur", "rouge", montant))
        if pariJ == "noir": paris.append(("Couleur","noir", montant))
        print(f"\033[32m{"Pari ajouté !"}\033[0m")
        return soldeTotal

def pariPairImpair(paris, soldeTotal):
    while True:
        pariJ = str(input("Le numero tiré va être \"pair\" ou \"impair\" "))
        if pariJ == "-1":
            return soldeTotal
        if pariJ != "pair" and pariJ != "impair":
            print(f"\033[31m{"Pari invalide !"}\033[0m")
            continue
        montant = choixMontant(soldeTotal)
        soldeTotal = soldeTotal - montant
        if pariJ == "pair": paris.append(("P/I", "pair", montant))
        if pariJ == "impair": paris.append(("P/I", "impair", montant))
        print(f"\033[32m{"Pari ajouté !"}\033[0m")
        return soldeTotal


def pariDouzaine(paris, soldeTotal):
    while True:
        pariJ = str(input("Le numero tiré va être dans la 1ere12 (1), 2eme12 (2) ou 3eme12 (3) "))
        if pariJ == "-1":
            return soldeTotal
        if pariJ != "1" and pariJ != "2" and pariJ != "3":
            print(f"\033[31m{"Pari douzaine invalide !"}\033[0m")
            continue
        montant = choixMontant(soldeTotal)
        soldeTotal = soldeTotal - montant
        if pariJ == "1": paris.append(("Douzaine", "1ere12", montant))
        if pariJ == "2": paris.append(("Douzaine", "2eme12", montant))
        if pariJ == "3": paris.append(("Douzaine", "3eme12", montant))
        print(f"\033[32m{"Pari ajouté !"}\033[0m")
        return soldeTotal

def pariManquePasse(paris, soldeTotal):
    while True:
        pariJ = str(input("Pour parier sur 1 à 18 c'est un \"manque\" \nPour parier sur 19 à 36 c'est un \"passe\" \n"))
        if pariJ == "-1":
            return soldeTotal
        if pariJ != "manque" and pariJ != "passe":
            print(f"\033[31m{"Pari manque / passe invalide !"}\033[0m")
            continue
        montant = choixMontant(soldeTotal)
        soldeTotal = soldeTotal - montant
        if pariJ == "manque": paris.append(("Manque/passe", "manque", montant))
        if pariJ == "passe": paris.append(("Manque/passe", "passe", montant))
        print(f"\033[32m{"Pari ajouté !"}\033[0m")
        return soldeTotal

#---------------------      Validation pari

def finPari(paris, soldeTotal):
    print("-------------------------    FIN DU PARI    --------------------------")
    if paris == []:
        print(f"\033[31m{"Vous n'avez pas parié !"}\033[0m")
    else :
        print("Vos paris : ", end=" ")
        for element in paris:
            for i in element:
                print(i, end=" | ")
        soldeTotal = identificationPari(paris, soldeTotal)
    return soldeTotal

def identificationPari(paris, soldeTotal):
    nombreAleatoire = genererNombreAleatoire()
    print("\nLe nombre tiré est : ", nombreAleatoire)
    for pariJ in paris:
        for pariNum in pariJ:

            match pariNum:
                case "Numéros":
                    soldeTotal = pariIdNumero(pariJ, soldeTotal, nombreAleatoire)
                case "Couleur":
                    soldeTotal = pariIdCouleur(pariJ, soldeTotal, nombreAleatoire)
                case "P/I":
                    soldeTotal = pariIdPairImpair(pariJ, soldeTotal, nombreAleatoire)
                case "Douzaine":
                    soldeTotal = pariIdDouzaine(pariJ, soldeTotal, nombreAleatoire)
                case "Manque/passe":
                    soldeTotal = pariIdManquePasse(pariJ, soldeTotal, nombreAleatoire)
    return soldeTotal

# Identification des paris fait :

def pariIdNumero(pariJ, soldeTotal, nombreAleatoire):
    numeroJ = pariJ[1]
    montantJN = pariJ[2]
    if numeroJ == nombreAleatoire:
        soldeTotal = soldeTotal + (montantJN * 36)
        print(f"\033[32m{"Pari gagnant !"}\033[0m", "Vous avez choisi le nombre", numeroJ, ".")
        print("La couleur de", nombreAleatoire, "est \"", couleur.getCouleur(nombreAleatoire), "\"")
        print("Vous avez donc : ", soldeTotal, "€\n")
    else:
        print(f"\033[31m{"Pari perdu,"}\033[0m","votre pari portant sur le numéro \"", numeroJ, "\" est perdant !\n")
    return soldeTotal

def pariIdCouleur(pariJ, soldeTotal, nombreAleatoire):
    couleurJ = pariJ[1]
    montantJC = pariJ[2]
    if nombreAleatoire == 0:
        print(f"\033[31m{"Pari perdu,"}\033[0m", "le nombre était : \"", nombreAleatoire,
                      "\", il n'est donc pas rouge, ni noir, mais vert !\n")
        return soldeTotal

    if couleurJ == couleur.getCouleur(nombreAleatoire):
        soldeTotal = soldeTotal + (montantJC * 2)
        print(f"\033[32m{"Pari gagnant !"}\033[0m", "Vous avez choisi la couleur",couleurJ,".")
        print("La couleur de",nombreAleatoire,"est \"",couleur.getCouleur(nombreAleatoire), "\"")
        print("Vous avez donc : ", soldeTotal, "€\n")
    else:
        print(f"\033[31m{"Pari perdu,"}\033[0m", "le nombre était : \"", nombreAleatoire,
              "\" ce qui ne correspond pas à votre pari !\n")
    return soldeTotal

def pariIdPairImpair(pariJ, soldeTotal, nombreAleatoire):
    montantJPI = pariJ[2]
    if nombreAleatoire == 0:
        print(f"\033[31m{"Pari perdu"}\033[0m", "le nombre était : \"", nombreAleatoire,
                      "\", il n'est donc pas pair ou impair !\n")
        return soldeTotal

    if nombreAleatoire % 2 == 0 and pariJ[1] == "pair":
        soldeTotal = soldeTotal + (montantJPI * 2)
        print(f"\033[32m{"Pari gagnant !"}\033[0m", "Vous avez parié sur \"pair\".")
        print("Le numéro", nombreAleatoire, "est \"pair\"")
        print("Vous avez donc : ", soldeTotal, "€\n")
    elif nombreAleatoire % 2 != 0 and pariJ[1] == "impair":
        soldeTotal = soldeTotal + (montantJPI * 2)
        print(f"\033[32m{"Pari gagnant !"}\033[0m", "Vous avez parié sur \"impair\".")
        print("Le numéro", nombreAleatoire, "est \"impair\"")
        print("Vous avez donc : ", soldeTotal, "€\n")
    else :
        print(f"\033[31m{"Pari perdu,"}\033[0m", "le nombre était : \"", nombreAleatoire,
              "\" ce qui ne correspond pas à votre pari !\n")
    return soldeTotal

def pariIdDouzaine(pariJ, soldeTotal, nombreAleatoire):
    montantJD = pariJ[2]
    verif = False
    if nombreAleatoire == 0:
        print(f"\033[31m{"Pari perdu,"}\033[0m", "le nombre était : \"", nombreAleatoire,
                      "\", il n'est donc pas compris dans les douzaines !\n")
        return soldeTotal
    match pariJ[1]:
        case "1ere12":
            for premiere in couleur.premiereDouxaine:
                if nombreAleatoire == premiere:
                    soldeTotal = soldeTotal + (montantJD * 3)
                    print(f"\033[32m{"Pari gagnant !"}\033[0m", "Vous avez parié sur la \"première douzaine\".")
                    print("Le numéro", nombreAleatoire, "est bien dans la \"première douzaine\"")
                    print("Vous avez donc : ", soldeTotal, "€\n")
                    verif = True
                else:
                    continue
        case "2eme12":
            for deuxieme in couleur.deuxiemeDouxaine:
                if nombreAleatoire == deuxieme:
                    soldeTotal = soldeTotal + (montantJD * 3)
                    print(f"\033[32m{"Pari gagnant !"}\033[0m", "Vous avez parié sur la \"deuxième douzaine\".")
                    print("Le numéro", nombreAleatoire, "est bien dans la \"deuxième douzaine\"")
                    print("Vous avez donc : ", soldeTotal, "€\n")
                    verif = True
                else:
                    continue
        case "3eme12":
            for troisieme in couleur.troisiemeDouxaine:
                if nombreAleatoire == troisieme:
                    soldeTotal = soldeTotal + (montantJD * 3)
                    print(f"\033[32m{"Pari gagnant !"}\033[0m", "Vous avez parié sur la \"troisème douzaine\".")
                    print("Le numéro", nombreAleatoire, "est bien dans la \"troisème douzaine\"")
                    print("Vous avez donc : ", soldeTotal, "€\n")
                    verif = True
                else:
                    continue
    if not verif:
        print(f"\033[31m{"Pari perdu,"}\033[0m", "le nombre était : \"", nombreAleatoire,
              "\" ce qui ne correspond pas à votre pari !\n")

    return soldeTotal

def pariIdManquePasse(pariJ, soldeTotal, nombreAleatoire):
    montantJD = pariJ[2]
    if nombreAleatoire == 0:
        print(f"\033[31m{"Pari perdu,"}\033[0m", "le nombre était : \"", nombreAleatoire,
                      "\", il n'est donc pas entre 1 et 36 !\n")
        return soldeTotal
    match pariJ[1]:
        case "manque":
            if 1 <= nombreAleatoire <= 18:
                soldeTotal = soldeTotal + (montantJD * 2)
                print(f"\033[32m{"Pari gagnant !"}\033[0m", "Vous avez parié sur \"manque\" donc de \"1 à 18\".")
                print("Le numéro", nombreAleatoire, "est bien dans l'intervalle de \"1 à 18\"")
                print("Vous avez donc : ", soldeTotal, "€\n")
            else:
                print(f"\033[31m{"Pari perdu,"}\033[0m", "le nombre était : \"", nombreAleatoire,
                      "\", il n'est donc pas entre 1 et 18 !\n")
        case "passe":
            if 19 <= nombreAleatoire <= 36:
                soldeTotal = soldeTotal + (montantJD * 2)
                print(f"\033[32m{"Pari gagnant !"}\033[0m", "Vous avez parié sur \"passe\" donc de \"19 à 36\".")
                print("Le numéro", nombreAleatoire, "est bien dans l'intervalle de \"19 à 36\"")
                print("Vous avez donc : ", soldeTotal, "€\n")
            else:
                print(f"\033[31m{"Pari perdu,"}\033[0m", "le nombre était : \"", nombreAleatoire,
                      "\", il n'est donc pas entre 19 et 36 !\n")
    return soldeTotal


if __name__ == '__main__':
    print("     |----------------------------------------------------------------|")
    print("     |    Ceci est une roulette européenne, Rien ne vas plus !        |")
    print("     |----------------------------------------------------------------|")
    print()
    soldeTotal = dmdSoldeTotal()
    print()
    start(soldeTotal)

