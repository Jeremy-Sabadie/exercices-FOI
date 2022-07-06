Effectuer des mouvements
Afin que vous puissiez manipuler le robot dans votre langage de programmation, nous avons créé un module appelé « robot ».

Quand un sujet exige que le robot effectue des mouvements, l'énoncé contiendra un cadre « Commandes pour cet exercice » décrivant les instructions à utiliser.

Pour disposer de ces instructions en Python, vous devez inclure la ligne suivante en haut de votre programme :

from robot import *
Si elle est nécessaire, vous la trouverez dans le squelette à compléter.



Commandes pour cet exercice
Pour déplacer le robot dans le fourré, nous proposons les quatre instructions suivantes :

Aller en haut
Aller en bas
Aller à gauche
Aller à droite
chacune demandant au robot de se déplacer d'une case dans une direction sur la grille.

En Python, vous devrez les écrire comme suit :

haut()
bas()
gauche()
droite()
Notez bien que le robot ne tourne pas : il se déplace de case en case sur la grille, vers le haut, le bas, la gauche ou la droite.