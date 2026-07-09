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
    ready = input("Êtes vous près ? (oui/non)")
    if ready == "oui":
        main(soldeTotal)
    elif ready == "non":
        print("pourquoi faire ??????")
        exit()
    else :
        start()


#---------------------      fonction de main
def pari(soldeTotal, nombreAleatoire):
    paris = []

    type = int(input("1- Numéro \n"
                     "2- Couleur \n"
                     "3- Pair / Impair \n"
                     "4- Douzaine \n"
                     "5- 1 à 18 ou 19 à 36 \n"
                     "0- Pour arrêter le pari"))
    match type:
        case "1":
            pariNumero(paris)
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



def pariNumero(paris):

    while True:
        try:
            pari = int(input("Entrez un nombre : "))
            paris.append(pari)
        except ValueError:
            return pari(), paris

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
    affichage_Matrice()
    nombreAleatoire = genererNombreAleatoire()
    pari(soldeTotal, nombreAleatoire)




if __name__ == '__main__':
    print("     |----------------------------------------------------------------|")
    print("     |    Ceci est une roulette européenne, Rien ne vas plus !        |")
    print("     |----------------------------------------------------------------|")
    print()
    soldeTotal = dmd_solde_total()
    print()
    start(soldeTotal)
