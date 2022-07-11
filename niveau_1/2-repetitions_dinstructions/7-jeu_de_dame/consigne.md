Répétitions imbriquées
Imaginons qu'on souhaite écrire un programme dessinant un rectangle rempli de X, haut de 5 lignes et large de 10 colonnes, c'est-à-dire :

↳
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
On se dit d'abord que l'on va utiliser une boucle pour afficher chacune des cinq lignes du programme, ce qui donnerait une structure comme ci-dessous.

Répéter 5 fois
   Afficher une ligne de 10 "X"
À présent, comment afficher une ligne de 10 « X » ? Avec une boucle bien sûr :

Répéter 10 fois
   Afficher "X" (sans retour à la ligne)
Aller à la ligne
Ce bout d'algorithme affiche 10 lettres « X » collées, puis revient à la ligne.

Au final, pour dessiner notre rectangle, il nous faut une boucle dans une boucle ! Car on veut :

Répéter 5 fois
   Répéter 10 fois
      Afficher "X" (sans retour à la ligne)
   Aller à la ligne
Ainsi, on répète 5 fois les instructions permettant d'afficher une ligne, ce qui permet d'obtenir 5 lignes.

On arrive donc au programme Python suivant :

for loop in range(5):
   for loop in range(10):
      print("X", end = "")
   print()
Lorsqu'une boucle apparaît à l'intérieur d'une autre boucle comme c'est le cas ici, on parle de boucle imbriquée.

Soyez sûr(e) de vous
Prenez du temps pour étudier ce programme, et comprendre comment il affiche un rectangle de X. Pour cela, vous pouvez vous mettre à la place du robot : suivez les instructions, et écrivez les « X » successifs sur une feuille de papier, ainsi que les fins de ligne. Quand vous écrivez un programme, vous pouvez donc anticiper son résultat, avant de le soumettre.