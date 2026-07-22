import random as rnd

from Affichage import affichage_Matrice

#---------------------      Mise ne place
def dmd_solde_total():
    print("----    solde minimum : 1€ || solde maximum 5000€    ----")
    try :
        solde = int(input("Entrez votre solde : "))
    except ValueError:
        return  dmd_solde_total()
    if solde < 1 or solde > 5000:
        return dmd_solde_total()
    print("Vous avez : ", solde, "€ !")
    return solde


def start(soldeTotal):
    try:
        ready = input("Êtes vous près ? (oui/non)")
        if ready == "oui":
            main(soldeTotal)
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
    print(paris)
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
                exit()
    except ValueError:
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
    if soldeTotal == 0:  ### changer le return pour le faire correspondre
        return pari(paris, soldeTotal)  ### à la fin des paris
    while True:
        try:
            pariJ = int(input("Entrez un nombre sur lequel vous voulez parier : "))
            if pariJ == -1:
                return pari(paris, soldeTotal)
            if pariJ < 0 or pariJ > 36:
                print(f"\033[31m{"Nombre indisponible sur une roulette allant de 0 à 36"}\033[0m")
                return pariNumero(paris, soldeTotal)
            montant = choix_montant(soldeTotal)
            soldeTotal = soldeTotal - montant
            paris.append(("numéros" , pariJ, montant))
            print(f"\033[32m{"Pari ajouté !"}\033[0m")
            if soldeTotal ==0:                  ### changer le return pour le faire correspondre
                return pari(paris, soldeTotal)  ### à la fin des paris
        except ValueError:
            print(f"\033[31m{"Nombre invalide !"}\033[0m")
            return pariNumero(paris, soldeTotal)

def pariCouleur(paris, soldeTotal):
    try:
        pariJ = str(input("Entrez une couleur sur laquel vous voulez parier : "))
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
        if soldeTotal == 0: return pari(paris, soldeTotal)      ### aller sur la fin de pari -> solde à 0
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
        if pariJ == "noir": paris.append(("P/I", "impair", montant))
        # else: return pari(paris, soldeTotal)
        print(f"\033[32m{"Pari ajouté !"}\033[0m")
        if soldeTotal == 0: return pari(paris, soldeTotal)  ### aller sur la fin de pari -> solde à 0
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
        if pariJ == "1ere12": paris.append(("Douzaine", "1ere12", montant))
        if pariJ == "2eme12": paris.append(("Douzaine", "2eme12", montant))
        if pariJ == "3eme12": paris.append(("Douzaine", "3eme12", montant))
        # else: return pari(paris, soldeTotal)
        print(f"\033[32m{"Pari ajouté !"}\033[0m")
        if soldeTotal == 0: return pari(paris, soldeTotal)  ### aller sur la fin de pari -> solde à 0
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
        if soldeTotal == 0: return pari(paris, soldeTotal)  ### aller sur la fin de pari -> solde à 0
        return pari(paris, soldeTotal)
    except ValueError:
        print(f"\033[31m{"Pari invalide !"}\033[0m")
        return pariManquePasse(paris, soldeTotal)

def genererNombreAleatoire():
    nombreAleatoire = rnd.randint(0, 36)
    return nombreAleatoire



#---------------------      Main
def main(soldeTotal):
    solde = soldeTotal
    #while True :
    nombreAleatoire = genererNombreAleatoire()
    pari(paris = [], soldeTotal = soldeTotal)




if __name__ == '__main__':
    print("     |----------------------------------------------------------------|")
    print("     |    Ceci est une roulette européenne, Rien ne vas plus !        |")
    print("     |----------------------------------------------------------------|")
    print()
    soldeTotal = dmd_solde_total()
    print()
    start(soldeTotal)
