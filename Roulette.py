import random as rnd
import couleur
from Affichage import affichage_Matrice

#---------------------      Mise ne place
def genererNombreAleatoire():
    nombreAleatoire = rnd.randint(0, 36)
    return nombreAleatoire

def dmd_solde_total():
    print("----    solde minimum : 1€ || solde maximum 5000€    ----")
    try :
        solde = int(input("Entrez votre solde : "))
    except ValueError:
        print(f"\033[31m{"Montant invalide !"}\033[0m")
        return  dmd_solde_total()
    if solde < 1 or solde > 5000:
        print(f"\033[31m{"Montant invalide !"}\033[0m")
        return dmd_solde_total()
    print("Vous avez : ", solde, "€ !")
    return solde


def start(soldeTotal):
    if soldeTotal == 0:
        print(f"\033[31m{"Vous n'avez plus de crédit, au revoir..."}\033[0m")
        exit()
    try:
        ready = input("Êtes vous près ? (oui/non)")
        if ready == "oui":
            pari(paris = [], soldeTotal = soldeTotal)
        if ready == "non":
            print("pourquoi faire ??????")
            exit()
        else:
            start(soldeTotal)
    except ValueError:
        start(soldeTotal)


#---------------------      fonction de main
def pari(paris, soldeTotal):
    affichage_Matrice()
    print("Il vous reste ", soldeTotal, " crédits !")
    try :
        type = int(input("1- Numéro \n"
                     "2- Couleur \n"
                     "3- Pair / Impair \n"
                     "4- Douzaine \n"
                     "5- 1 à 18 ou 19 à 36 \n"
                     "0- Pour arrêter le pari \n"))

        match type:
            case 1:
                pariNumero(paris, soldeTotal)
            case 2:
                pariCouleur(paris, soldeTotal)
            case 3:
                pariPairImpair(paris, soldeTotal)
            case 4:
                paridouzaine(paris, soldeTotal)
            case 5:
                pariManquePasse(paris, soldeTotal)
            case 0:
                return finPari(paris, soldeTotal)
            case _:
                print(f"\033[31m{"Saisi invalide !"}\033[0m")
                return pari(paris, soldeTotal)
    except ValueError:
        print(f"\033[31m{"Saisi invalide !"}\033[0m")
        return pari(paris, soldeTotal)

def choix_montant(soldeTotal):
    try :
        montant = int(input("Entrez le montant que vous souhaitez parier : "))
        if montant > soldeTotal:
            print(f"\033[31m{"Vous n'avez pas assez de crédits ! \n"}\033[0m")
            return choix_montant(soldeTotal)
        else:
            return montant

    except ValueError:
        print(f"\033[31m{"Nombre invalide !"}\033[0m")
        return choix_montant(soldeTotal)

def pariNumero(paris, soldeTotal):

    while True:
        if soldeTotal == 0:  ### changer le return pour le faire correspondre
            return finPari(paris, soldeTotal)  ### à la fin des paris
        try:
            pariJ = int(input("Entrez un nombre sur lequel vous voulez parier : "))
            if pariJ == -1:
                return pari(paris, soldeTotal)
            if pariJ < 0 or pariJ > 36:
                print(f"\033[31m{"Nombre indisponible sur une roulette allant de 0 à 36"}\033[0m")
                return pariNumero(paris, soldeTotal)
            montant = choix_montant(soldeTotal)
            soldeTotal = soldeTotal - montant
            paris.append(("Numéros" , pariJ, montant))
            print(f"\033[32m{"Pari ajouté !"}\033[0m")
        except ValueError:
            print(f"\033[31m{"Nombre invalide !"}\033[0m")
            return pariNumero(paris, soldeTotal)

def pariCouleur(paris, soldeTotal):
    try:
        pariJ = str(input("Entrez une couleur sur laquelle vous voulez parier : "))
        if pariJ == "-1":
            return pari(paris, soldeTotal)
        if pariJ != "rouge" and pariJ != "noir":
            print(f"\033[31m{"Couleur invalide !"}\033[0m")
            return pariCouleur(paris, soldeTotal)
        montant = choix_montant(soldeTotal)
        soldeTotal = soldeTotal - montant
        if pariJ == "rouge": paris.append(("Couleur", "rouge", montant))
        if pariJ == "noir": paris.append(("Couleur","noir", montant))
        #else: return pari(paris, soldeTotal)
        print(f"\033[32m{"Pari ajouté !"}\033[0m")
        if soldeTotal == 0: return finPari(paris, soldeTotal)   ### aller sur la fin de pari -> solde à 0
        return pari(paris, soldeTotal)
    except ValueError:
        print(f"\033[31m{"Couleur invalide !"}\033[0m")
        return pariCouleur(paris, soldeTotal)


def pariPairImpair(paris, soldeTotal):
    try:
        pariJ = str(input("Le numero tiré va être \"pair\" ou \"impair\" "))
        if pariJ == "-1":
            return pari(paris, soldeTotal)
        if pariJ != "pair" and pariJ != "impair":
            print(f"\033[31m{"Pari invalide !"}\033[0m")
            return pariPairImpair(paris, soldeTotal)
        montant = choix_montant(soldeTotal)
        soldeTotal = soldeTotal - montant
        if pariJ == "pair": paris.append(("P/I", "pair", montant))
        if pariJ == "impair": paris.append(("P/I", "impair", montant))
        # else: return pari(paris, soldeTotal)
        print(f"\033[32m{"Pari ajouté !"}\033[0m")
        if soldeTotal == 0: return finPari(paris, soldeTotal)  ### aller sur la fin de pari -> solde à 0
        return pari(paris, soldeTotal)
    except ValueError:
        print(f"\033[31m{"Pari invalide !"}\033[0m")
        return pariPairImpair(paris, soldeTotal)


def paridouzaine(paris, soldeTotal):
    try:
        pariJ = str(input("Le numero tiré va être dans la 1ere12 (1), 2eme12 (2) ou 3eme12 (3) "))
        if pariJ == "-1":
            return pari(paris, soldeTotal)
        if pariJ != "1" and pariJ != "2" and pariJ != "3":
            print(f"\033[31m{"Pari douzaine invalide !"}\033[0m")
            return paridouzaine(paris, soldeTotal)
        montant = choix_montant(soldeTotal)
        soldeTotal = soldeTotal - montant
        if pariJ == "1": paris.append(("Douzaine", "1ere12", montant))
        if pariJ == "2": paris.append(("Douzaine", "2eme12", montant))
        if pariJ == "3": paris.append(("Douzaine", "3eme12", montant))
        # else: return pari(paris, soldeTotal)
        print(f"\033[32m{"Pari ajouté !"}\033[0m")
        if soldeTotal == 0: return finPari(paris, soldeTotal)  ### aller sur la fin de pari -> solde à 0
        return pari(paris, soldeTotal)
    except ValueError:
        print(f"\033[31m{"Pari invalide !"}\033[0m")
        return paridouzaine(paris, soldeTotal)


def pariManquePasse(paris, soldeTotal):
    try:
        pariJ = str(input("Pour parier sur 1 à 18 c'est un \"manque\" \nPour parier sur 19 à 36 c'est un \"passe\" \n"))
        if pariJ == "-1":
            return pari(paris, soldeTotal)
        if pariJ != "manque" and pariJ != "passe":
            print(f"\033[31m{"Pari manque / passe invalide !"}\033[0m")
            return pariManquePasse(paris, soldeTotal)
        montant = choix_montant(soldeTotal)
        soldeTotal = soldeTotal - montant
        if pariJ == "manque": paris.append(("Manque/passe", "manque", montant))
        if pariJ == "passe": paris.append(("Manque/passe", "passe", montant))
        # else: return pari(paris, soldeTotal)
        print(f"\033[32m{"Pari ajouté !"}\033[0m")
        if soldeTotal == 0: return finPari(paris, soldeTotal)  ### aller sur la fin de pari -> solde à 0
        return pari(paris, soldeTotal)
    except ValueError:
        print(f"\033[31m{"Pari invalide !"}\033[0m")
        return pariManquePasse(paris, soldeTotal)

#---------------------      Validation pari
def finPari(paris, soldeTotal):
    print("-------------------------    FIN DU PARI    --------------------------")
    if paris == []:
        print(f"\033[31m{"Vous n'avez pas parié !"}\033[0m")
        exit()
    else :
        print("Vos paris : ", end=" ")
        for tuple in paris:
            for i in tuple:
                print(i, end=" | ")
        identificationPari(paris, soldeTotal)

def identificationPari(paris, soldeTotal):
    nombreAleatoire = genererNombreAleatoire()
    print("\nLe nombre tiré est : ", nombreAleatoire)
    for pariJ in paris:
        for pariNum in pariJ:

            match pariNum:
                case "Numéros":
                    soldeTotal = pariIDNumero(pariJ, soldeTotal, nombreAleatoire)
                case "Couleur":
                    soldeTotal = pariIDCouleur(pariJ, soldeTotal, nombreAleatoire)
                case "P/I":
                    soldeTotal = pariIDPairImpair(pariJ, soldeTotal, nombreAleatoire)
                case "Douzaine":
                    soldeTotal = pariIDDouzaine(pariJ, soldeTotal, nombreAleatoire)
                case "Manque/passe":
                    soldeTotal = pariIDManquePasse(pariJ, soldeTotal, nombreAleatoire)
    start(soldeTotal)



def pariIDNumero(pariJ, soldeTotal, nombreAleatoire):
    numeroJ = pariJ[1]
    montantJN = pariJ[2]
    if numeroJ == nombreAleatoire:
        soldeTotal = soldeTotal + (montantJN * 35)  # verifié si 35 ou 36
        print(f"\033[32m{"Pari gagnant !"}\033[0m", "Vous avez choisi le nombre", numeroJ, ".")
        print("La couleur de", nombreAleatoire, "est \"", couleur.getCouleur(nombreAleatoire), "\"")
        print("Vous avez donc : ", soldeTotal, "€\n")
    else:
        print(f"\033[31m{"Pari perdu,"}\033[0m","votre pari portant sur le numéro \"", numeroJ, "\" est perdant !\n")
    return soldeTotal

def pariIDCouleur(pariJ, soldeTotal, nombreAleatoire):
    couleurJ = pariJ[1]
    montantJC = pariJ[2]
    if couleurJ == couleur.getCouleur(nombreAleatoire):
        soldeTotal = soldeTotal + (montantJC * 2)
        print(f"\033[32m{"Pari gagnant !"}\033[0m", "Vous avez choisi la couleur",couleurJ,".")
        print("La couleur de",nombreAleatoire,"est \"",couleur.getCouleur(nombreAleatoire), "\"")
        print("Vous avez donc : ", soldeTotal, "€\n")
    else:
        print(f"\033[31m{"Pari perdu,"}\033[0m", "le nombre était : \"", nombreAleatoire,
              "\"ce qui ne correspond pas à votre pari !\n")
    return soldeTotal

def pariIDPairImpair(pariJ, soldeTotal, nombreAleatoire):
    montantJPI = pariJ[2]
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

def pariIDDouzaine(pariJ, soldeTotal, nombreAleatoire):
    montantJD = pariJ[2]
    verif = False
    match pariJ[1]:
        case "1ere12":
            for premiere in couleur.premiere_douxaine:
                if nombreAleatoire == premiere:
                    soldeTotal = soldeTotal + (montantJD * 3)
                    print(f"\033[32m{"Pari gagnant !"}\033[0m", "Vous avez parié sur la \"première douzaine\".")
                    print("Le numéro", nombreAleatoire, "est bien dans la \"première douzaine\"")
                    print("Vous avez donc : ", soldeTotal, "€\n")
                    verif = True
                else:
                    continue
        case "2eme12":
            for deuxieme in couleur.deuxieme_douxaine:
                if nombreAleatoire == deuxieme:
                    soldeTotal = soldeTotal + (montantJD * 3)
                    print(f"\033[32m{"Pari gagnant !"}\033[0m", "Vous avez parié sur la \"deuxième douzaine\".")
                    print("Le numéro", nombreAleatoire, "est bien dans la \"deuxième douzaine\"")
                    print("Vous avez donc : ", soldeTotal, "€\n")
                    verif = True
                else:
                    continue
        case "3eme12":
            for troisieme in couleur.troisieme_douxaine:
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

def pariIDManquePasse(pariJ, soldeTotal, nombreAleatoire):
    montantJD = pariJ[2]
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


#---------------------      Main
#def main(soldeTotal):
#    pari(paris = [], soldeTotal = soldeTotal)




if __name__ == '__main__':
    print("     |----------------------------------------------------------------|")
    print("     |    Ceci est une roulette européenne, Rien ne vas plus !        |")
    print("     |----------------------------------------------------------------|")
    print()
    soldeTotal = dmd_solde_total()
    print()
    start(soldeTotal)
