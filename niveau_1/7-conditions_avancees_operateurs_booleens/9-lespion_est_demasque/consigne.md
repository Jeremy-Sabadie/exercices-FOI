Grâce à un certain nombre d'informateurs plus ou moins fiables, le chef de la police a recueilli des indications qui devraient lui permettre enfin de démasquer cet espion qui lui échappe depuis des semaines. La population de la ville étant relativement importante, il vous demande votre aide afin d'automatiser un peu les choses. Vous devez estimer la probabilité qu'une personne soit un espion.

Ce que doit faire votre programme :
Votre programme doit lire entier : un nombre de personnes à considérer. Ensuite, pour chaque personne, il doit lire son signalement sous la forme de cinq entiers : sa taille en centimètres, son âge en années, son poids en kilogrammes, un entier valant 1 si la personne possède un cheval et 0 sinon, et un entier valant 1 si la personne à les cheveux bruns et 0 sinon.

On veut déterminer pour chaque personne à quel point elle correspond aux 5 critères suivants :

il aurait une taille supérieure ou égale à 178 cm et inférieure ou égale à 182 cm ;
il aurait au moins 34 ans ;
il pèserait strictement moins de 70 kg ;
il n'a pas de cheval ;
il a les cheveux bruns.
Lorsque cela n'est pas précisé explicitement, les inégalités sont au sens large.

Pour chaque personne, vous devez tester tous les critères. S'ils sont vérifiés tous les 5, vous devez afficher « Très probable ». Si seulement 3 ou 4 sont vérifiés, vous devez afficher « Probable ». Si aucun n'est vérifié, vous devez afficher « Impossible », et dans les autres cas, vous devez afficher « Peu probable ».

Exemple
entrée :

1
180
40
65
0
1
sortie :

Très probable