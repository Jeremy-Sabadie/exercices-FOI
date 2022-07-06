Vous avancez prudemment sur une corniche le long d'une falaise ; vous devez accéder au sommet de la paroi.

Vous tombez finalement sur un renfoncement. Au fond de cette petite grotte se trouve un magnifique empilement de quatre gros disques de pierre ! En déplaçant cette pile de disques sur la corniche, vous pourrez l'escalader et atteindre le haut de la falaise.


Structure actuelle de la grotte

Résultat recherché
L'empilement est malheureusement très lourd, même pour votre robot : celui-ci ne peut porter qu'un seul disque à la fois. De plus, il semble évident qu'un disque ne pourra pas supporter un disque plus gros que lui. Moyennant cela, il va vous falloir reformer l'empilement à l'entrée de la grotte, dans un espace très exigu.

Ce que doit faire votre programme :
On peut considérer qu'il y a trois zones dans la grotte :

zone 1 : le fond, où se trouvent les quatre cylindres, empilés du plus large au plus étroit ;
zone 2 : le centre, où vous pouvez placer temporairement des disques les uns au-dessus des autres ;
zone 3 : l'entrée de la grotte, où vous devez reformer l'empilement complet.
Le but est de déplacer tous les disques de la zone 1 à la zone 3 en respectant ces deux règles :

on ne peut déplacer qu'un disque à la fois, car ils sont très lourds ;
on ne peut jamais poser un disque sur un disque plus petit que lui, car sinon l'empilement s'effondrerait !

Commandes pour cet exercice
Le robot peut exécuter cette instruction :

Déplacer zoneSource -> zoneDestination
Lorsqu'il la reçoit, le robot prend le disque se situant au sommet de la zone désignée par zoneSource et le place au sommet de la zone désignée par zoneDestination (au sol si la zone est vide).

Pour identifier une zone, écrivez à la place de zoneSource et zoneDestination le numéro de la zone concernée.

En Python, l'instruction s'écrit :

deplacer(zoneSource, zoneDestination)
N'oubliez pas d'inclure la ligne suivante en haut de votre programme pour l'utiliser :

from robot import *

En guise d'exemple, voici un programme qui effectue quelques déplacements : de la zone 1, il déplace le premier disque dans la zone 3 et le deuxième dans la zone 2 ; puis il remet le premier dans la zone 1.