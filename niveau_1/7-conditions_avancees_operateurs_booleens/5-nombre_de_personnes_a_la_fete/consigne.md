Le gouverneur a organisé une petite fête à laquelle tous les notables étaient invités. Il souhaiterait à présent faire réaliser une petite affiche vantant le succès de la fête et indiquant en particulier le nombre de personnes présentes au moment le plus intense de la fête.

Ce que doit faire votre programme :
On vous décrit les arrivées et départs des participants d'une fête, et votre programme doit afficher le nombre maximum de personnes qui ont été présentes au même moment. Chacun des invités est identifié par un numéro.

Le premier entier à lire est nbPersonnes : le nombre total de personnes qui se sont rendues à la fête. Ensuite, il y a 2 × nbPersonnes entiers à lire, dans l'ordre chronologique des arrivées et départs. Si l'entier est positif, c'est que la personne de numéro correspondant vient d'arriver, s'il est négatif, elle vient de partir. Une fois qu'une personne est partie, elle ne revient pas.

Votre programme doit déterminer puis afficher le nombre maximum de personnes qui étaient là simultanément.

Exemple
entrée :

5
1
2
-1
3
4
-2
-4
5
-3
-5
sortie :

3
Commentaires
Au cours de la fête décrite par l'exemple, on a donc les flux suivants :

l'invité n°1 entre ;
l'invité n°2 entre ;
l'invité n°1 sort ;
l'invité n°3 entre ;
l'invité n°4 entre ;
l'invité n°2 sort…
Le nombre de présents est maximal lors de l'arrivée de la personne n°4 : il y a alors trois invités qui sont arrivés et restés.