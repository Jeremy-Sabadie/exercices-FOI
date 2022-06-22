Observez le programme suivant :

nbValeurs = int(input())
for iValeur in range(nbValeurs):
   laValeur = int(input())
print(laValeur)
Il demande un nombre nbValeurs, puis chacune des valeurs. À la fin, il affiche le dernier entier qui a été saisi. Voici un exemple d'exécution :

↳
2
10
25
↳
25
Ainsi, la variable laValeur, qui reçoit des valeurs au sein de la boucle, peut être réutilisée après la boucle. Cela peut s'avérer dangereux : en effet, que se passe-t-il dans le programme si 0 est saisi pour nbValeurs ? Dans ce cas, laValeur n'est jamais initialisée, et on obtient l'erreur suivante :

↳
Traceback (most recent call last):
  File "./run/exe", line 4, in <module>
    print(laValeur)
NameError: name 'laValeur' is not defined
On appelle portée d'une variable l'ensemble des endroits du programme où elle existe. En Python, la portée d'une variable s'étend donc dans tout le programme dès qu'elle reçoit sa première valeur. Toutefois, nous verrons plus tard des cas où la portée d'une variable est limitée à un bloc, par exemple dans une fonction.