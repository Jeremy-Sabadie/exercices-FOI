Les enfants du village vous ont posé beaucoup de questions sur ce que font les enfants sur Terre. Ils ont été supris d'apprendre que, comme eux, les enfants terriens doivent aller à l'école. Et ils ont trouvé très étonnant que ceux-ci doivent lever le doigt pour demander la permission de parler en classe, car eux doivent pencher la tête pour cela.

Ce que vous n'aviez pas prévu, c'est qu'une petite fille trouverait amusant de lever le doigt comme une terrienne. Sa maîtresse n'a pas du tout apprécié car, pour cette tribu, lever le doigt de cette manière est une grave insulte au grand sorcier ! La petite fille a été sévèrement punie et vous la retrouvez en pleurs. Vous vous sentez un peu responsable et décidez de l'aider à faire sa punition.

Ce que doit faire votre programme :
Votre programme doit écrire 135 fois la phrase : "Je dois respecter le Grand Sorcier.", en plaçant cette phrase exactement une fois sur chaque ligne. Attention, si votre programme n'affiche pas exactement cette phrase avec les points et la majuscule là où il faut, il faudra tout recommencer.

Important : votre programme ne doit pas faire plus d'une douzaine de lignes.



Répéter une action
Si pour vous il est rébarbatif de répéter une tâche de nombreuses fois, cela ne pose aucun problème à votre robot. Celui-ci est donc très pratique pour cela.

Ainsi, imaginons que l'on souhaite écrire 5 fois « Coucou ». On pourrait le faire avec le programme suivant :

print("Coucou")
print("Coucou")
print("Coucou")
print("Coucou")
print("Coucou")
C'est plutôt convenable ici… Mais si on veut effectuer par exemple 1 000 affichages, cela va devenir bien plus fastidieux !

Pour plus d'efficacité, on aimerait indiquer directement que l'on souhaite répéter l'affichage en boucle, de la même manière qu'on pourrait écrire en français :

Répéter 5 fois
   Afficher "Coucou"
On décale l'instruction à répéter vers la droite avec des espaces, pour indiquer qu'elle « appartient » à l'instruction précédente. Effectuer des décalages comme ceci est très courant en programmation : on appelle ça l'indentation.

Ainsi, en Python, pour répéter 5 fois l'instruction qui affiche « Coucou », on va écrire le programme ci-dessous.

for loop in range(5):
   print("Coucou")
↳
Coucou
Coucou
Coucou
Coucou
Coucou
Pour coder la répétition, nous avons utilisé la structure suivante :

for loop in range(5):
   ...
et nous avons mis l'instruction à répéter à la place des ..., après trois espaces. Cette indentation est obligatoire.

Vous pouvez donc écrire une boucle de cette façon, en indiquant le nombre de répétitions à la place du chiffre 5. Nous éluciderons par la suite les mystères de cette écriture. Prenez garde à ne pas oublier le deux-points « : » à la fin de la ligne.