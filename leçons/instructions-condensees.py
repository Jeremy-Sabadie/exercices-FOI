longueur = int(input("entrez la longeur:"))
largeur = int(input("entrez la largeur:"))
périmètre = (longueur + largeur) * 2
aire = longueur * largeur
aire=str(aire)
périmètre=str(périmètre)
print("le périmètre="+périmètre, end = " ")
"""
En fait, avec un seul print, il est possible d'afficher autant de valeurs que l'on veut ! Il suffit pour cela de les séparer par une virgule entre les parenthèses. On pourrait en effet écrire le programme précédent ainsi :

longueur = int(input())
largeur = int(input())
périmètre = (longueur + largeur) * 2
aire = longueur * largeur
print(périmètre, aire)
Mais où est passée l'espace ? Les différentes valeurs sont automatiquement séparées par une espace à l'affichage. Cela permet d'écrire facilement de jolies phrases :

âge = 20
tempsProgrammation = 8
print("J'ai", âge, "ans et je programme depuis", tempsProgrammation, "ans")
sans risque d'oublier l'espace au bout des chaînes de caractères.

En fait, tout comme le retour à la ligne à la fin, cette espace séparatrice peut être affectée par une option : sep. Juste avant de fermer la parenthèse d'une instruction print, on peut indiquer les valeurs de sep et de end. Par exemple :

print(1, 2, 3, 4, 5, sep = ",", end = " | ")
print(6, 7, 8, 9, 10, sep = ";")
↳
1,2,3,4,5 | 6;7;8;9;10
Toutefois, dans certains cas, il peut être difficile de se repérer dans une instruction print très longue. N'hésitez donc pas à en utiliser plusieurs à la suite si cela rend la lecture plus agréable !

De manière générale, le langage de programmation permet de formuler la même chose de différentes façons. Certaines écritures sont cependant plus agréables pour un humain : c'est à vous de les trouver ; en aucun cas l'ordinateur ne vous y aidera !

Lorsqu'une écriture vous est inhabituelle, prenez un peu de temps pour chercher comment l'écrire de sorte qu'elle soit la plus « propre » (jolie, optimale, demandant moins d'effort de lecture à une personne quelconque) possible, afin de vous en servir automatiquement la prochaine fois. Les codes que nous présentons dans les cours et les corrections sont généralement de bonnes références (sachant que nous n'utilisons que les notations que nous avons vues jusqu'alors).


