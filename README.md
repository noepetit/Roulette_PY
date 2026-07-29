# Roulette en python

Ce projet à pour but de m'entrainer et de me sentir plus à l'aise en developpement en utilisant le langage informatique "python".


## CARACTÉRISTIQUE

* roulette visuel dans le terminal
* pari personalisé sur le terminal
    * pari sur numéro(s) avec mise personnalisable sur chaque numéro(s)
    * paris sur la couleur avec mise personnalisable
    * paris sur PAIR ou IMPAIR avec mise personnalisable
    * paris sur "1ere douzaine", "2eme douzaine" et "3eme douzaine" avec mise personnalisable
    * paris 1 à 18 ou 19 à 36 avec mise personnalisable
    * (peut-être sur lignes)
* Gestion du solde de l'utilisateur
* Gestion des nombres avec un dictionnaire pour lier les chiffres à leur couleur atitré
* (peut-être une gestion du temps pour réspecté le lien avec les casinos où il y a 40 secondes pour faire un paris)

## RÈGLES
Les règle sont identique à la roulette européenne en casino :
* pari sur numéro, si gagnant (mise * 35) ;
* pari sur la couleur, si pair ou impair, manque ou passe, si gagnant (mise * 2) ;
    * Si 0 tombe, mise perdu
* pari sur les douzaines, si gagnant (mise * 3);
    * Si 0 tombe, mise perdu

## COMMENT JOUER ?
Tout d'abord, vous allez devoir rentrer le solde que vous souhaité. Il doit obligatoirement être entre 1€ et 5000€ (crédits fictif).

Vous allez ensuite être amené à parier, une roulette vous est présenté sur le terminal, votre solde vous est affiché. Un menu vous montre les différents type de pari disponible : 
* "numéros",
* "couleur",
* "pair/impair",
* "douzaine",
* "manque/passe"

Ensuite, dans chaque type de pari vous pouvez revenir en arrière (sur le menu) avec "-1" en cas d'erreur, Si vous avez terminé vos paris et qu'il vous reste des crédits, vous pouvez finir le(s) pari(s) avec "0" dans le menu.



## AIDE UTILISÉ

****Utilisation des LLM modéré :****

***Pas de code généré directement par un LLM et ensuite copié-collé***, utilisation de "Claude" pour aide sur la façon de réaliser certaine fonctionnalité. 

Le lien de la conversation
[ici](https://claude.ai/share/8a232e05-a2fe-4f06-be75-e90979ca8952).
## Authors

- [@noepetit](https://www.github.com/noepetit)

-------------------------------

# Roulette_mini_jeu_PY
création d'un roulette anglaise de casino en python

## Chose faite
* un affichage pour demander un nombre compris entre 0 et 36
* Attribuer une couleur au nombre choisi
* tirer un nombre "aleatoire" avec random entre 0 et 36
* comparer le nombre choisi par l'utilisateur avec le nombre tiré au hasard.
* afficher le résultat
* deuxième mini-jeu ou il faut deviner une couleur

## à completer ultérieurement
* associer directement chiffre à couleur 
* faire apparaitre une matrice pour que ce soit plus parlant
* ajouter un système de mise


# Roulette.py
* affichage de la roulette sous forme de matrice V
* trouver comment parcourir la string de pari et associer les pari a leur gain
  * parcourir string, séparateur entre chaque pari "&" si plusieurs paris
