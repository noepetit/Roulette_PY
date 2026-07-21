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
def pari(soldeTotal, paris):
    affichage_Matrice()
    type = int(input("1- Numéro \n"
                     "2- Couleur \n"
                     "3- Pair / Impair \n"
                     "4- Douzaine \n"
                     "5- 1 à 18 ou 19 à 36 \n"
                     "0- Pour arrêter le pari"))
    match type:
        case 1:
            pariNumero(paris, soldeTotal)
        case "2":
            pariCouleur(paris)
        case "3":
            pariPairImpair(paris)
        case "4":
            paridouzaine(paris)
        case "5":
            pariManquePasse(paris)
        case "0":
            exit()

def choix_montant(soldeTotal):
    try :
        montant = int(input("Entrez le montant que vous souhaitez parier : "))
        if montant > soldeTotal:
            print("Vous n'avez pas assez de crédits ! \n")
            return choix_montant(soldeTotal)
        else:
            return montant

    except ValueError:
        return choix_montant(soldeTotal)

def pariNumero(paris, soldeTotal):
    while True:
        try:
            pariJ = int(input("Entrez un nombre sur lequel vous voulez parier : "))
            if pariJ == -1:
                return pari(soldeTotal, paris)
            if pariJ < 0 or pariJ > 36:
                print("Nombre indisponible sur une roulette allant de 0 à 36")
                return pariNumero(paris, soldeTotal)
            montant = choix_montant(soldeTotal)
            soldeTotal = soldeTotal - montant
            paris.append(("numéros" , pariJ, montant))
            print(paris)
            print(soldeTotal)
            if soldeTotal ==0:                  ### changer le return pour le faire correspondre
                return pari(soldeTotal, paris)  ### à la fin des paris
        except ValueError:
            return pariNumero(paris, soldeTotal)

def pariCouleur(paris):
    return 0

def pariPairImpair(paris):
    return 0


def paridouzaine(paris):
    return 0


def pariManquePasse(paris):
    return 0

def genererNombreAleatoire():
    nombreAleatoire = rnd.randint(0, 36)
    return nombreAleatoire



#---------------------      Main
def main(soldeTotal):
    solde = soldeTotal
    #while True :
    nombreAleatoire = genererNombreAleatoire()
    pari(soldeTotal, paris = [

    ])




if __name__ == '__main__':
    print("     |----------------------------------------------------------------|")
    print("     |    Ceci est une roulette européenne, Rien ne vas plus !        |")
    print("     |----------------------------------------------------------------|")
    print()
    soldeTotal = dmd_solde_total()
    print()
    start(soldeTotal)
