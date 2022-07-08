Mémoriser des informations
Supposons que l'on souhaite écrire un programme qui affiche la distance qui séparait la Terre et Mars le 27 août 2003 (55 758 000 km), puis la distance à parcourir par la lumière pour faire l'aller-retour depuis la Terre (le double). On pourrait utiliser les instructions suivantes :

Afficher 55758000
Afficher 2 * 55758000
Cela fonctionnera parfaitement bien. Toutefois, si l'on veut afficher ces informations pour un autre jour, alors que la distance entre les deux planètes a changé, il faudra modifier le programme à deux endroits différents, puisque l'on y a écrit deux fois la distance 55 758 000.

Pour éviter de devoir faire des modifications en double, on va utiliser une variable, appelée distance, pour représenter la valeur 55 758 000. On peut alors exprimer notre programme de cette façon :

distance <- 55758000
Afficher distance
Afficher 2 * distance
La première ligne signifie « distance reçoit 55 758 000 ». La flèche <- matérialise le mouvement du nombre 55 758 000 qui va se placer dans distance.

Ce programme est un peu plus long, mais offre deux avantages :

si l'on veut modifier la distance, on n'aura qu'une seule valeur à modifier dans notre programme ;
la valeur porte un nom, qui permet de comprendre à quoi elle correspond.
En Python, cela s'écrit comme suit :